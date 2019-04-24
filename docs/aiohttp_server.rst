aiohttp Server
==============

Let's start writing our own web application using `aiohttp`_.

Install aiohttp and Python 3.7 if you have not already. Using a virtual environment
is recommended.

Example using ``venv``. In the command line::

   python3.7 -m venv tutorial_venv
   source tutorial_venv/bin/activate

   (tutorial_venv) python3.7 -m pip install -U pip aiohttp

A simple web server example
---------------------------

First we will define a request handler, and it is a coroutine.

::

    from aiohttp import web

    async def handler(request):
        return web.Response(text="Hello world")

The above is a coroutine that will return a Web Response, containing the text ``Hello world``.

Once we have the request handler, create an Application instance::


    app = web.Application()
    app.add_routes([web.get('/', handler)])

In the above snippet, we're creating an aiohttp web application, and registering
a URL route: ``/`` (usually the root of the app), and we're telling the app
to execute the ``handler`` coroutine.

To run the app::

    web.run_app(app)


Run the script, e.g. in the command line::

    (tutorial_venv) python server.py


You should see the following output in the command line::

    ======== Running on http://0.0.0.0:8080 ========
    (Press CTRL+C to quit)

You can now open your favorite web browser with the url http://0.0.0.0:8080. It should
display "Hello world".

The complete code can look like the following:

.. literalinclude:: ../code/04-server/01-simple-server.py


Using route decorators
----------------------

Notice in the previous example, we're registering the root url by calling ``add_routes``,
and passing it a list of one URL. If you have more than one URL, it is a matter of
creating another request handler coroutine.

There is another way to define urls, by using decorators.

::

    routes = web.RouteTableDef()

    @routes.get('/')
    async def handler(request):
        return web.Response(text="Hello world")

    app.add_routes(routes)

Both ways work, and it is a matter of your own personal choice.

URL Arguments and query parameters
----------------------------------

When building web applications, sometimes you need to handle dynamic urls,
instead of hardcoding.

Suppose we want to have urls for each users in our system, and greet the user,
by having the ``/{username}/`` url.


::

    @routes.get('/{username}')
    async def greet_user(request: web.Request) -> web.Response:
        user = request.match_info.get("username", "")
        return web.Response(text=f"Hello, {user}")


Now re-start the server and open http://0.0.0.0:8080/student in your favorite
browser.

Another way to parametrize resource is by using query parameters, for example
``?page=1&uppercase=true``.

::

    @routes.get('/{username}')
    async def greet_user(request: web.Request) -> web.Response:
        user = request.match_info.get("username", "")
        return web.Response(text=f"Hello, {user}")

Serving other methods (POST, PUT, etc)
--------------------------------------

Notice so far we've been serving ``GET`` resources. If you have resource that
needs to be accessed in other methods, like ``POST`` or ``PUT``:

    @routes.post('/add_user')
    async def add_user(request: web.Request) -> web.Response:
        data = await request.post()
        username = data.get('username')
        # Add the user
        # ...
        return web.Response(text=f"{username} was added")


Returning JSON Response
-----------------------

::

    @routes.get('/json')
    async def handler(request):
        data = {'some': 'data'}
        return web.json_response(data)




TBD

- Write our first aiohttp web server
- Introduce how to add routes/url
- Introduce how to handle GET and POST requests (useful for serving REST API)
- Provide example of how to handle file upload to the web server
- introduce db engine connection, in POST handler (eg store the blog to database)
  (use heroku, basic plan is free)


Story: build a blog website
Form:
Postgres? database


.. _`aiohttp`: https://aiohttp.readthedocs.io
