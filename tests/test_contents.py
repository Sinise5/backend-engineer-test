import pytest

@pytest.fixture
async def created_content_id(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.post("/contents/", headers=headers, json={
        "title": "Test Judul",
        "body": "Ini body konten"
    })
    assert res.status_code in [200, 201]
    data = res.json()
    return data["id"]  # pastikan endpoint return id


@pytest.mark.anyio
async def test_create_content(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.post("/contents/", headers=headers, json={
        "title": "Berita terkini",
        "body": "Selamat datang kawan.!"
    })
    assert res.status_code in [200, 201]


@pytest.mark.anyio
async def test_edit_content(client, auth_token, created_content_id):
    headers = {"Authorization": auth_token}
    res = await client.put(f"/contents/{created_content_id}", headers=headers, json={
        "title": "Berita Update",
        "body": "Isi terbaru"
    })
    assert res.status_code in [200, 404]


@pytest.mark.anyio
async def test_get_all_contents(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.get("/contents/", headers=headers)
    assert res.status_code == 200


@pytest.mark.anyio
async def test_get_contents_by_user(client, auth_token):
    headers = {"Authorization": auth_token}
    res = await client.get("/contents/user/", headers=headers)
    assert res.status_code in [200, 404]


@pytest.mark.anyio
async def test_get_content_by_id(client, auth_token, created_content_id):
    headers = {"Authorization": auth_token}
    res = await client.get(f"/contents/{created_content_id}", headers=headers)
    assert res.status_code in [200, 404]


@pytest.mark.anyio
async def test_delete_content(client, auth_token, created_content_id):
    headers = {"Authorization": auth_token}
    res = await client.delete(f"/contents/{created_content_id}", headers=headers)
    assert res.status_code in [200, 404]
