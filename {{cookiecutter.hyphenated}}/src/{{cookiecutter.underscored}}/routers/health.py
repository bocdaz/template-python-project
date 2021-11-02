"""Health Check API endpoints and functions."""
import shutil

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from ..config import Settings, get_settings

router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)


class Disk(BaseModel):
    """Models a disk check."""

    total: str
    used: str
    free: str


class Health(BaseModel):
    """Models a health check response."""

    status: str
    disk: Disk


def disk_check(settings: Settings) -> Disk:
    """Return a Disk object which gives info on the disk status."""
    (total, used, free) = shutil.disk_usage(settings.root_dir)
    disk = Disk(total=total, used=used, free=free)

    return disk


@router.get("/", response_model=Health)
def health_check(settings: Settings = Depends(get_settings)):
    """Returns the health status of this resource and whether it's fully operational."""
    return Health(status="GREEN", disk=disk_check(settings))
