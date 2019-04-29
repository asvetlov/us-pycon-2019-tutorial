aiohttp session
===============


Session is a storage for saving temporary data like logged user info.

``aiohttp_session`` library actually uses a middleware for session control.

Setup session support::

    import aiohttp_session

    async def init_app() -> web.Application:
        app = web.Application()
        app.add_routes(...)
        aiohttp_session.setup(app, aiohttp_session.SimpleCookieStorage())

We use unsecured ``SimpleCookieStorage()`` for tutorial to save session data in browser
cookies.

More powerful alternatives are using ``EncryptedCookieStorage``, ``NaClCookieStorage``
or ``RedisStorage``. If you want to use another storage system like database please
implement ``AbstractStorage`` interface and enjoy.

Session object
--------------

Session is available as ``session = await aiohttp_session.get_session(request)`` call.

The returned ``session`` object has dict-like interface::

    session['NEW_KEY'] = value

The session is saved authomatically after finishing request handling.


Authorization
-------------

Create a middleware to check if a user is logged in::

    _WebHandler = Callable[[web.Request], Awaitable[web.StreamResponse]]


    def require_login(func: _WebHandler) -> _WebHandler:
        func.__require_login__ = True  # type: ignore
        return func


    @web.middleware
    async def check_login(request: web.Request,
                          handler: _WebHandler) -> web.StreamResponse:
        require_login = getattr(handler, "__require_login__", False)
        session = await aiohttp_session.get_session(request)
        username = session.get("username")
        if require_login:
            if not username:
                raise web.HTTPSeeOther(location="/login")
        return await handler(request)

It raises a redirection to ``/login`` page if *web-handler* requires authorization.

All sensitive web-handlers are marked by ``@require_login`` decorator::

    @router.get("/{post}/edit")
    @require_login
    @aiohttp_jinja2.template("edit.html")
    async def edit_post(request: web.Request) -> Dict[str, Any]:
        ...

Login and Logout
----------------

For login we use a simple HTML form::

    @router.get("/login")
    @aiohttp_jinja2.template("login.html")
    async def login(request: web.Request) -> Dict[str, Any]:
        return {}


    @router.post("/login")
    async def login_apply(request: web.Request) -> web.Response:
        session = await aiohttp_session.get_session(request)
        form = await request.post()
        session["username"] = form["login"]
        raise web.HTTPSeeOther(location="/")

``view.html`` template:

.. literalinclude:: ../code/09-sessions/templates/login.html


Logout is even simpler::

    @router.get("/logout")
    async def logout(request: web.Request) -> web.Response:
        session = await aiohttp_session.get_session(request)
        session["username"] = None
        raise web.HTTPSeeOther(location="/")


Getting username from post adding and modifying handlers
--------------------------------------------------------

Let's save logged in username as post's *editor*::

    @router.post("/{post}/edit")
    @require_login
    async def edit_post_apply(request: web.Request) -> web.Response:
        post_id = request.match_info["post"]
        session = await aiohttp_session.get_session(request)
        editor = session["username"]
        ...

.. note::

   Multiple ``get_session()`` calls returns the same session object if used for handling
   the same HTTP request.


Last neat: use session data in rendering username by Jinja2 context processors:

.. literalinclude:: ../code/09-sessions/01-login-session.py
   :pyobject: username_ctx_processor

Rendering in template::

    {% if username %}
    <div>[{{ username }}] <a href="/logout">Logout</a></div>
    {% else %}
    <div>[Anonymous] <a href="/login">Login</a></div>
    {% endif %}

Setup context processor::

    async def init_app() -> web.Application:
        app = web.Application()
        ...
        aiohttp_jinja2.setup(
            app,
            loader=...,
            context_processors=[username_ctx_processor],
        )


TBD (by Mariatta)

- Introduce how to handle user sessions/logging in and out on the web server (uses middleware, more complex example)
- simple authorization, eg username/password. Might be able to use GitHub
