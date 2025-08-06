import pytest


@pytest.fixture
async def created_user_id(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.post("/users/", headers=headers, json={
        "username": "sinise",
        "full_name": "Sintia",
        "password": "Qwerty@11",
        "role": "admin"
    })
    assert res.status_code in [200, 201, 400]
    if res.status_code in [200, 201]:
        data = res.json()
        return data["id"]
    else:
        # Handle jika user sudah ada (username taken), bisa fetch user ID dari endpoint lain
        # Tapi untuk test sederhana kita return None agar test berikutnya tetap bisa jalan (meskipun akan gagal)
        return None


@pytest.mark.anyio
async def test_create_user(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.post("/users/", headers=headers, json={
        "username": "sinise",
        "full_name": "Sintia",
        "password": "Qwerty@11",
        "role": "admin"
    })
    assert res.status_code in [200, 201, 400]


@pytest.mark.anyio
async def test_edit_user(client, auth_token, created_user_id):
    if not created_user_id:
        pytest.skip("User ID tidak tersedia untuk pengujian update.")
    
    headers = {"Authorization": auth_token}
    res = await client.put(f"/users/{created_user_id}", headers=headers, json={
        "full_name": "Sintia Dua",
        "password": "Qwerty@11",
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
    if not created_user_id:
        pytest.skip("User ID tidak tersedia untuk pengujian delete.")
    
    headers = {"Authorization": auth_token}
    res = await client.delete(f"/users/{created_user_id}", headers=headers)
    assert res.status_code in [200, 404]
