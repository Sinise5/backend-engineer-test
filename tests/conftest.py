import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

BASE_URL = "http://127.0.0.1:8003"

@pytest.fixture
def anyio_backend():
    return "asyncio"

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=BASE_URL) as ac:
        yield ac

@pytest.fixture
async def auth_token(client):
    # Register user (boleh gagal 400 jika sudah ada)
    await client.post("/register", json={
        "username": "testuser",
        "full_name": "Test User",
        "password": "Qwerty@11",
        "role": "admin"
    })

    # Login user
    res = await client.post("/token", json={
        "username": "testuser",
        "password": "Qwerty@11"
    })
    print(res)

    token = res.json()["access_token"]
    return f"Bearer {token}"
