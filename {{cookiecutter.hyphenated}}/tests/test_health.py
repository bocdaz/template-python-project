from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.{{cookiecutter.underscored}}.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def test_get_health(client: TestClient):
    response = client.get("/health")
    json_response = response.json()

    assert response.status_code == 200
    assert json_response["status"] == "GREEN"
    assert json_response["disk"]
