aiohttp middlewares
===================


A middleware is a coroutine that can modify either the request or response. For
example, here’s a simple middleware which appends 😃 to the response::

    from aiohttp import web

    @web.middleware
    async def middleware(request: web.Request,
                         handler: Callable[[web.Request], Awaitable[web.Response]]):
        resp = await handler(request)
        resp.text = f"{resp.text} 😃"
        return resp

The middleware is applied to *all* aiohttp application routes.

To setup middleware pass it to ``web.Application`` constructor::

    app = web.Application(middlewares=[middleware])

Let's make something useful!

Error handling
---------------

.. literalinclude:: ../code/08-middlewares/01-error-middleware.py
   :pyobject: error_middleware

``error-page.html`` template:

.. literalinclude:: ../code/08-middlewares/templates/error-page.html
