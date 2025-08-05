import pytest


@pytest.fixture
async def created_user_id(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.post("/users/", headers=headers, json={
       "username": "sinise",
        "full_name": "Sintia",
        "password": "Qwerty1",
        "role": "admin"
    })
    assert res.status_code in [200, 201]
    data = res.json()
    return data["id"]  # pastikan endpoint return id


@pytest.mark.anyio
async def test_create_user(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.post("/users/", headers=headers, json={
        "username": "sinise",
        "full_name": "Sintia",
        "password": "Qwerty1",
        "role": "admin"
    })
    assert res.status_code in [200, 201, 400]

@pytest.mark.anyio
async def test_edit_user(client, auth_token, created_user_id):
    headers = {"Authorization": auth_token}
    res = await client.put("/users/{created_user_id}", headers=headers, json={
        "full_name": "Sintia Dua",
        "password": "Qwerty1",
        "role": "admin",
        "is_active": True
    })
    assert res.status_code in [200, 404]

@pytest.mark.anyio
async def test_get_all_users(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.get("/users/", headers=headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)

@pytest.mark.anyio
async def test_delete_user(client, auth_token, created_user_id):
    headers = {"Authorization": auth_token}
    res = await client.delete("/users/{created_user_id}", headers=headers)
    assert res.status_code in [200, 404]
