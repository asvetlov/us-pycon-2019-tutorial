import sqlite3
from pathlib import Path


HERE = Path(".")
while not (HERE / ".git").exists():
    if HERE == HERE.parent:
        raise RuntimeError("Cannot find root github dir")
    HERE = HERE.parent

SQLITE = HERE / "db.sqlite3"

with sqlite3.connect(SQLITE) as conn:
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE posts (
        id INTEGER PRIMARY KEY,
        title TEXT,
        text TEXT,
        owner TEXT,
        editor TEXT,
        image BLOB)
    """
    )
    conn.commit()
