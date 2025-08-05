import pytest

@pytest.mark.anyio
async def test_register_user(client):
    response = await client.post("/register", json={
        "username": "newuser",
        "full_name": "New User",
        "password": "Qwerty1",
        "role": "admin"
    })
    assert response.status_code in [200, 201, 400]

@pytest.mark.anyio
async def test_login(client):
    response = await client.post("/token", data={
        "username": "testuser",
        "password": "Qwerty1"
    })
    assert response.status_code == 200
    assert response
    assert "access_token" in response.json()
