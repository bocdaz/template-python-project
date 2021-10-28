from typing import Dict

from fastapi.testclient import TestClient


def user_authentication_headers(
    *, client: TestClient, username: str, password: str, scope: str
) -> Dict[str, str]:
    login_data = {
        "grant_type": "",
        "username": username,
        "password": password,
        "scope": scope,
        "client_id": "",
        "client_secret": "",
    }

    r = client.post("/token", data=login_data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers
