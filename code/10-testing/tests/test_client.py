from pathlib import Path
from typing import Any, AsyncIterator

import aiosqlite
import pytest
from aiohttp.test_utils import TestServer as _TestServer

from proj.client import Client
from proj.server import init_app


@pytest.fixture
async def server(aiohttp_server: Any, db_path: Path) -> _TestServer:
    app = await init_app(db_path)
    return await aiohttp_server(app)


@pytest.fixture
async def client(server: _TestServer) -> AsyncIterator[Client]:
    async with Client(server.make_url("/"), "test_user") as client:
        yield client


async def test_get_post(client: Client, db: aiosqlite.Connection) -> None:
    post = await client.create("test title", "test text")

    async with db.execute(
        "SELECT title, text, owner, editor FROM posts WHERE id = ?", [post.id]
    ) as cursor:
        record = await cursor.fetchone()
        assert record["title"] == "test title"
        assert record["text"] == "test text"
        assert record["owner"] == "test_user"
        assert record["editor"] == "test_user"
