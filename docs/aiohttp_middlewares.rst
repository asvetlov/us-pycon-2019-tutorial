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


Modify request
--------------

Rewrite protocol/host/remote-ip::

    @web.middleware
    async def middleware(request: web.Request,
                         handler: Callable[[web.Request], Awaitable[web.Response]]):
        real_ip = request.headers['X-Forwarded-For']
        real_host = request.headers['X-Forwarded-Host']
        real_proto = request.headers['X-Forwarded-Proto']
        new_request = request.clone(remote=real_ip,
                                    host=real_host,
                                    scheme=real_proto)
        return await handler(request)

See also https://github.com/aio-libs/aiohttp-remotes for such middlewares.

DB Transaction handling
-----------------------

::

    @web.middleware
    async def middleware(request: web.Request,
                         handler: Callable[[web.Request], Awaitable[web.Response]]):
        db = request.config_dict["DB"]
        await db.execute("BEGIN")
        try:
            resp = await handler(request)
            await db.execute("COMMIT")
            return resp
        except Exception:
            await db.execute("ROLLBACK")
            raise

Check for login
---------------

::

    @web.middleware
    async def middleware(request: web.Request,
                         handler: Callable[[web.Request], Awaitable[web.Response]]):
        user = await get_user(request)
        if user is not None:
            request['USER'] = user
        else:  # user is None
            if login_required(handler):
                raise web.HTTPSeeAlso(location='/login')
        return await handler(request)


Full example for server with error-page middleware
---------------------------------------------------

Example for HTML version of blogs server with images: :ref:`full-middleware-error-page`

.. toctree::
   :hidden:

   aiohttp_middlewares_full
