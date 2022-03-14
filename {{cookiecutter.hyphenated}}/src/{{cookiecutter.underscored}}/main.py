{% if cookiecutter.project_type == 'Python package' %}"""{{ cookiecutter.project_name }} main."""


def hi():
    """Say hi in the terminal."""
    print("Hi from main.py!")


if __name__ == "__main__":
    hi(){% elif cookiecutter.project_type == 'FastAPI application' %}"""Main FastAPI application."""
import os
import sys
from datetime import timedelta

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger

from .config import Settings, get_settings
from .dependencies import (
    Token,
    authenticate_user,
    create_access_token,
    fake_users_db,
    get_current_active_user,
    logging_dependency,
)
from .routers import health, items, users

app = FastAPI(
    title="{{cookiecutter.project_name}}",
    description="## Overview\n\n"
    "## API Upgrades\n\n"
    "### Backwards-compatible changes\n\n"
    "The following changes are considered backwards-compatible:\n"
    "- Adding new API resources\n"
    "- Adding new optional rquest parameters to existing API methods.\n"
    "- Adding new properties to existing API responses.\n"
    "- Changing the order of properties in existing API responses.\n"
    "- Changing the length or format of opaque strings, such as object IDs,"
    " error messages, and other human-readable strings.\n"
    "- Adding new event types.\n"
    "\n",
    openapi_tags=[
        {
            "name": "items",
            "description": "Manage items.",
        },
    ],
)

# Setup the logger which can be injected into routers
logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>",
)

# Add the /users endpoints to our application
app.include_router(
    users.router, tags=["users"], dependencies=[Depends(logging_dependency)]
)
# Add the /items endpoints to our application. This depends on getting the active
# user, and for the user to have the "items" scope in order to access any of the
# endpoints in the items router
app.include_router(
    items.router,
    dependencies=[
        Security(get_current_active_user, scopes=["items"]),
        Depends(logging_dependency),
    ],
)
# Add the /health endpoint to our application
# This endpoint will return the status of the app, whether it is functional
#   and returns and self-diagnostics that can help with debugging
app.include_router(
    health.router,
    dependencies=[
        Depends(logging_dependency),
    ],
)


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    settings: Settings = Depends(get_settings),
):
    """Login as the provided user and return a JWT token."""
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/")
def read_root():
    """This path returns a simple greeting."""
    return {"Hello": "World"}


def dev_start():
    """Launched with `poetry run dev` at root level."""
    if os.name == "posix":
        uvicorn.run(
            "{{cookiecutter.underscored}}.main:app",
            host="0.0.0.0",  # noqa: S104
            port=8000,
            reload=True,
        )
    else:
        uvicorn.run(
            "{{cookiecutter.underscored}}.main:app", host="localhost", port=8000, reload=True
        ){% endif %}
