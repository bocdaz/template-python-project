"""Users API endpoints and functions."""
from fastapi import APIRouter, Security

from ..dependencies import User, get_current_active_user

router = APIRouter()


@router.get("/users/")
async def read_users():
    """Return a demo list of users."""
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me")
async def read_user_me(
    current_user: User = Security(get_current_active_user, scopes=["me"])
):
    """Return the current user."""
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: User = Security(get_current_active_user, scopes=["items"])
):
    """Return the demo items belonging to the current user."""
    return [{"item_id": "Foo", "owner": current_user.username}]


@router.get("/users/{username}")
async def read_user(username: str):
    """Return the provided username."""
    return {"username": username}
