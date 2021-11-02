"""Items API endpoints and functions."""
from datetime import datetime
from enum import Enum
from typing import Dict, Optional

from fastapi import APIRouter, Body, Response
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


class DataCategorization(str, Enum):
    """Bank of Canada Data Categorization levels.

    https://intranet-en.bank-banque-canada.ca/wp-content/uploads/2021/03/information-categorization-guide.pdf"""  # noqa

    unclassified = "Unclassified"
    protected_a = "Protected A"
    protected_b = "Protected B"
    protected_c = "Protected C"
    classified_secret = "Secret"  # noqa: S105
    classified_confidential = "Confidential"
    classified_topsecret = "Top Secret"


class Item(BaseModel):
    """Models an item."""

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class SecretItem(Item):
    """Models a Secret item."""

    class Config:
        """Extra config that doesn't show up in the model."""

        schema_extra: Dict[str, DataCategorization] = {
            "x-data-classification": DataCategorization.classified_secret,
        }


@router.get("/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Return an item."""
    return {"item_id": item_id, "q": q}


@router.get("/secret/{item_id}", response_model=SecretItem)
def read_secret_item(item_id: int, response: Response):
    """Return an item that's been classified as Secret."""
    item = SecretItem(name="Foo", description="A Secret Item", price=35.4, tax=3.2)
    response.headers["X-Data-Classification"] = item.Config.schema_extra[
        "x-data-classification"
    ]
    return item


@router.put("/{item_id}")
def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings`"
                " to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    """Update an item by id."""
    results = {"item_id": item_id, "item": item}
    return results


@router.get("/deprecated/{items_id}", deprecated=True)
def read_old_item(response: Response, item_id: int, q: Optional[str] = None):
    """Return an item."""
    format = "%a, %d %b %Y %H:%M:%S GMT"
    deprecated = datetime.utcnow()
    sunset = datetime.utcnow()
    response.headers["Deprecated"] = deprecated.strftime(format)
    response.headers["Sunset"] = sunset.strftime(format)
    return {"item_id": item_id, "q": q}
