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


In our examples so far, we've only been returning plain text. You can return
more complex HTML if you have templates. For this, middleware can be used to
render HTML templates.


aiohttp-jinja2
--------------

Install the dependencies::


    (tutorial_venv) python3.7 -m pip install -U jinja2 aiohttp-jinja2


Code structure::

    /jinja_server.py
    /templates/base.html


Sample HTML template:

.. literalinclude:: ../code/05-middleware/templates/base.html


Template rendering
------------------


In jinja_server.py, set up aiohttp-jinja2 and template directory::


    import jinja2
    import aiohttp_jinja2


    app = web.Application()

    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "templates"))
    )


To render a page using the template::

    @routes.get('/{username}')
    async def greet_user(request):

        context = {
            'username': request.match_info.get("username", ""),
            'current_date': 'January 27, 2017'
        }
        template = "base.html"
        response = aiohttp_jinja2.render_template(template, request,
                                              context=context)

        return response



TBD (by Mariatta)

- Introduce aiohttp-jinja2 renderer, and use it in the web server
- Provide example on how to structure the project (separating Python codebase and HTML templates directory)
- Documentation: http://aiohttp_jinja2.readthedocs.org/
- render the blog posts
