from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from src.{{cookiecutter.underscored}}.main import app
from tests.utils import user_authentication_headers


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def user_token_headers(
    client: TestClient,
    username: str = "johndoe",
    password: str = "secret",
    scope: str = "",
) -> Dict[str, str]:
    return user_authentication_headers(
        client=client,
        username=username,
        password=password,
        scope=scope,
    )


def test_get_item_proper_scopes(client: TestClient):
    """GET an item with the proper scopes.

    This should be succesful because we have the `items` scope needed by our
    `/items/{item_id}` endpoint, and the `me` scope required by
    `get_current_active_user`.
    """
    user_headers = user_token_headers(client, scope="me items")
    response = client.get("/items/1", headers=user_headers)
    assert response.status_code == 200


@pytest.mark.parametrize("scope", [(""), ("me"), ("items")])
def test_get_item_without_proper_scopes(client: TestClient, scope: str):
    """GET an item without the proper scopes.

    This should return 403 Forbidden since the `me` scope is required by
    `get_current_active_user` and the `item` scope is required for `items`
    endpoints.
    """
    user_headers = user_token_headers(client, scope=scope)
    response = client.get("/items/1", headers=user_headers)
    assert response.status_code == 403


def test_put_items(client: TestClient):
    user_headers = user_token_headers(client, scope="me items")
    response = client.put(
        "/items/1",
        headers=user_headers,
        json={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 1,
        "item": {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    }


def test_put_items_invalid(client: TestClient):
    user_headers = user_token_headers(client, scope="me items")
    response = client.put(
        "/items/1",
        headers=user_headers,
        json={
            "name": "Baz",
            "price": "thirty five point four",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "price"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            },
        ]
    }


def test_secret_item_headers(client: TestClient):
    user_headers = user_token_headers(client, scope="me items")
    response = client.get(
        "/items/secret/1",
        headers=user_headers,
        json={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    )
    assert response.status_code == 200
    assert "Secret" == response.headers["x-data-classification"]
