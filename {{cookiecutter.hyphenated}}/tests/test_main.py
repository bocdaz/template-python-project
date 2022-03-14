{% if cookiecutter.project_type == 'Python package' %}import {{cookiecutter.underscored}}


def test_print_output(capfd):
    """Verify the print output of hi()."""
    {{cookiecutter.underscored}}.main.hi()
    out, err = capfd.readouterr()
    assert out == "Hi from main.py!\n"
{% elif cookiecutter.project_type == 'FastAPI application' %}from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.{{cookiecutter.underscored}}.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def test_get_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_token(client: TestClient):
    login_data = {
        "grant_type": "",
        "username": "johndoe",
        "password": "secret",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/token", data=login_data)
    tokens = response.json()
    assert response.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_get_token_invalid_password(client: TestClient):
    login_data = {
        "grant_type": "",
        "username": "johndoe",
        "password": "wrongsecret",
        "scope": "me items",
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/token", data=login_data)
    tokens = response.json()
    assert response.status_code == 401
    assert "access_token" not in tokens


def test_get_token_nonexistant_user(client: TestClient):
    login_data = {
        "grant_type": "",
        "username": "nobody",
        "password": "secret",
        "scope": "me items",
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/token", data=login_data)
    tokens = response.json()
    assert response.status_code == 401
    assert "access_token" not in tokens{% endif %}
