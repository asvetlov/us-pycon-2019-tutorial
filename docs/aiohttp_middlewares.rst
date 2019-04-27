aiohttp middleware
==================


A middleware is a coroutine that can modify either the request or response. For
example, here’s a simple middleware which appends 😃 to the response::

    from aiohttp.web import middleware

    @middleware
    async def middleware(request, handler):
        resp = await handler(request)
        resp.text = f"{resp.text} 😃"
        return resp




