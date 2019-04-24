from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    return web.Response(text="Hello world")


async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes([web.get("/", handler)])
    return app


web.run_app(init_app())
