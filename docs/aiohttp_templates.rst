aiohttp templates
=================

In our examples so far, we've only been returning plain text. You can return
more complex HTML if you have templates. For this, templates can be used to
render HTML templates.


aiohttp is a core library without embedded templating tool, third party libraries need
to be installed to provide such functionality.

Let's use officially supported ``aiohttp_jinja2`` for famous ``jinja2`` template engine.


aiohttp-jinja2
--------------

Install the dependencies::


    (tutorial_venv) python3.7 -m pip install -U jinja2 aiohttp-jinja2


Code structure::

    /jinja_server.py
    /templates/base.html


Sample HTML template:

.. literalinclude:: ../code/05-templating/templates/example.html


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
    async def greet_user(request: web.Request) -> web.Response:

        context = {
            'username': request.match_info.get("username", ""),
            'current_date': 'January 27, 2017'
        }
        response = aiohttp_jinja2.render_template("example.html", request,
                                              context=context)

        return response


Anouther alternative is applying ``@aiohttp_jinja2.template()`` decorator to
*web-handler*::

    @routes.get('/{username}')
    @aiohttp_jinja2.template("example.html")
    async def greet_user(request: web.Request) -> Dict[str, Any]:
        context = {
            'username': request.match_info.get("username", ""),
            'current_date': 'January 27, 2017'
        }
        return content

Note, the ``great_user`` signature has changed: it returns a *jinja2 context*
now. ``@aiohttp_jinja2.template()``decorator renders the context and returns
``web.Response`` object automatically.


TBD (by Mariatta)

- Introduce aiohttp-jinja2 renderer, and use it in the web server
- Provide example on how to structure the project (separating Python codebase and HTML templates directory)
- Documentation: http://aiohttp_jinja2.readthedocs.org/
- render the blog posts
