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


def inactive_user_token_headers(
    client: TestClient,
    username: str = "alice",
    password: str = "secret2",
    scope: str = "",
) -> Dict[str, str]:
    return user_authentication_headers(
        client=client,
        username=username,
        password=password,
        scope=scope,
    )


def test_get_users(client: TestClient):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]


def test_get_users_me(client: TestClient):
    user_headers = user_token_headers(client, scope="me items")
    response = client.get(
        "/users/me",
        headers=user_headers,
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }


def test_get_users_username(client: TestClient):
    user_headers = user_token_headers(client, scope="me items")
    response = client.get(
        "/users/victor",
        headers=user_headers,
    )
    assert response.status_code == 200
    assert response.json() == {"username": "victor"}


def test_allow_user_to_get_their_own_items(client: TestClient):
    user_headers = user_token_headers(client, scope="me items")
    response = client.get(
        "/users/me/items",
        headers=user_headers,
    )
    assert response.status_code == 200
    assert response.json() == [{"item_id": "Foo", "owner": "johndoe"}]


def test_inactive_user_to_get_their_own_items(client: TestClient):
    user_headers = inactive_user_token_headers(client, scope="me items")
    response = client.get(
        "/users/me/items",
        headers=user_headers,
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Inactive user"}
