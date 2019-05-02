aiohttp Writing tests
=====================

There are several tools for testing Python code.

We show how to work with the most powerful and popular tool called pytest_ .

We need to install ``pytest`` itself and ``pytest-aiohttp`` plugin first::

   pip install pytest
   pip install pytest-aiohttp

.. note::

   ``pytest-aiohttp`` is not compatible with another pupular plugin ``pytest-asyncio``.


Making test asynchronous
------------------------

Just use ``async def test_*()`` instead of plain ``def test_*()``. ``pytest-aiohttp``
does all dirty work for you::

    async def test_a() -> None:
        await asyncio.sleep(0.01)
        assert 1 == 2  # False

Testing server code
-------------------


Let's sligtly modify application code to accept a path to database explicitly::

    async def init_app(db_path: Path) -> web.Application:
        app = web.Application()
        app["DB_PATH"] = db_path
        ...


    async def init_db(app: web.Application) -> AsyncIterator[None]:
        sqlite_db = app["DB_PATH"]
        db = await aiosqlite.connect(sqlite_db)
        ...


After that we can use a separate isolated *test database* for running unit tests.

We need handy fixtures to initialize test DB::

    @pytest.fixture
    def db_path(tmp_path: Path) -> Path:
        path = tmp_path / "test_sqlite.db"
        try_make_db(path)
        return path


    @pytest.fixture
    async def db(db_path: Path) -> aiosqlite.Connection:
        """DB connection to access test DB directly from tests"""
        conn = await aiosqlite.connect(db_path)
        conn.row_factory = aiosqlite.Row
        yield conn
        await conn.close()

.. note::

   Fixtures have *function* scope (default), that mean that every test gets a new fresh
   empty database.


Another fixtire instantiates our server and starts it on random local TCP port using
*aiohttp provided* ``aiohttp_client`` fixture::

    @pytest.fixture
    async def client(aiohttp_client: Any, db_path: Path) -> _TestClient:
        app = await init_app(db_path)
        return await aiohttp_client(app)

Test posts list::

    async def test_list_empty(client: _TestClient) -> None:
        resp = await client.get("/api")
        assert resp.status == 200, await resp.text()
        data = await resp.json()
        assert data == {"data": [], "status": "ok"}

Use ``db`` fixture to add a post before testing ``/api/{post_id}`` web-handler::

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




Testing client with fake server
-------------------------------

Working with HTTPS
------------------

Client mocking
--------------

There is ``aioresponses`` third-party library::

    pip install aioresponses

Usage::

    from aioresponses import aioresponses

    async def test_request() -> None:
        with aioresponses() as mocked:
            mocked.get('http://example.com', status=200, body='test')
            session = aiohttp.ClientSession()
            resp = await session.get('http://example.com')

            assert resp.status == 200
            assert "test" == await resp.text()



TBD (by Andrew)

- Writing tests for aiohttp client
- Writing tests for aiohttp server
- Tests using pytest and pytest-asyncio.


.. _pytest: https://docs.pytest.org
