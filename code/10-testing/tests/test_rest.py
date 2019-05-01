from pathlib import Path
from typing import Any

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
