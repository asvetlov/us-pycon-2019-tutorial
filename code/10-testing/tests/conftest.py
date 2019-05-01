from pathlib import Path

import aiosqlite
import pytest

from proj.server import try_make_db


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    path = tmp_path / "test_sqlite.db"
    try_make_db(path)
    return path


@pytest.fixture
async def db(db_path):
    conn = await aiosqlite.connect(db_path)
    yield conn
    await conn.close()
