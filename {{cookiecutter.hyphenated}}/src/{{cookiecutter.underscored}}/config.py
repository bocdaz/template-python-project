"""API configuration settings.

See: https://fastapi.tiangolo.com/advanced/settings/?h=conf#the-config-file
"""
from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings


@lru_cache()
def get_settings():
    """Return the configuration settings.

    Since lru_cache is used, the settings are read once from the file
    and then returned from cache for all subsequent calls.
    """
    return Settings()


class Settings(BaseSettings):
    """Shared Application Settings."""

    # Settings for Security Dependencies
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    root_dir: str = str(Path(__file__).resolve().parent)
