from typing import Any

from aiohttp import web

from proj.client import Client


async def test_get_post(aiohttp_server: Any) -> None:
    async def handler(request: web.Request) -> web.Response:
        data = await request.json()
        assert data["title"] == "test title"
        assert data["text"] == "test text"
        return web.json_response(
            {
                "status": "ok",
                "data": {
                    "id": 1,
                    "title": "test title",
                    "text": "test text",
                    "owner": "test_user",
                    "editor": "test_user",
                },
            }
        )

    app = web.Application()
    app.add_routes([web.post("/api", handler)])
    server = await aiohttp_server(app)
    async with Client(server.make_url("/"), "test_user") as client:
        post = await client.create("test title", "test text")

        assert post.id == 1
        assert post.title == "test title"
        assert post.text == "test text"
        assert post.owner == "test_user"
        assert post.editor == "test_user"
