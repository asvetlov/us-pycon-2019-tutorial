from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    user = request.match_info.get("user", "Anonymous")
    return web.Response(text=f"Hello, {user}")


async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes([web.get("/", handler)])
    app.add_routes([web.get("/{user}", handler)])
    return app


web.run_app(init_app())
