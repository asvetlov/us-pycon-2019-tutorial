from pathlib import Path
from typing import Any

import aiosqlite
import pytest
from aiohttp.test_utils import TestClient as _TestClient

from proj.server import init_app


@pytest.fixture
async def client(aiohttp_client: Any, db_path: Path) -> _TestClient:
    app = await init_app(db_path)
    return await aiohttp_client(app)


async def test_list_empty(client: _TestClient) -> None:
    resp = await client.get("/api")
    assert resp.status == 200, await resp.text()
    data = await resp.json()
    assert data == {"data": [], "status": "ok"}


async def test_add_post(client: _TestClient) -> None:
    POST_REQ = {"title": "test title", "text": "test text", "owner": "test user"}
    POST = {"id": 1, "editor": POST_REQ["owner"], **POST_REQ}
    resp = await client.post("/api", json=POST_REQ)
    assert resp.status == 200, await resp.text()
    data = await resp.json()
    assert data == {"data": POST, "status": "ok"}

    POST_WITHOUT_TEXT = POST.copy()
    del POST_WITHOUT_TEXT["text"]
    resp = await client.get("/api")
    assert resp.status == 200, await resp.text()
    data = await resp.json()
    assert data == {"data": [POST_WITHOUT_TEXT], "status": "ok"}


async def test_get_post(client: _TestClient, db: aiosqlite.Connection) -> None:
    async with db.execute(
        "INSERT INTO posts (title, text, owner, editor) VALUES (?, ?, ?, ?)",
        ["title", "text", "user", "user"],
    ) as cursor:
        post_id = cursor.lastrowid
    await db.commit()

    resp = await client.get(f"/api/{post_id}")
    assert resp.status == 200
    data = await resp.json()
    assert data == {
        "data": {
            "editor": "user",
            "id": "1",
            "owner": "user",
            "text": "text",
            "title": "title",
        },
        "status": "ok",
    }
