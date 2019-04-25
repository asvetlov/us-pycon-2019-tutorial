import os

import jinja2
from aiohttp import web

import aiohttp_jinja2


routes = web.RouteTableDef()


@routes.get("/{username}")
async def greet_user(request: web.Request) -> web.Response:

    context = {
        "username": request.match_info.get("username", ""),
        "current_date": "January 27, 2017",
    }
    template = "base.html"
    response = aiohttp_jinja2.render_template(template, request, context=context)
    return response


async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)

    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "templates"))
    )

    return app


web.run_app(init_app())
