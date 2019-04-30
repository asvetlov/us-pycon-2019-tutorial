aiohttp templates
=================

In our examples so far, we've only been returning plain text. You can return
more complex HTML if you have templates. For this, templates can be used to
render HTML templates.


aiohttp is a core library without embedded templating tool, third party libraries need
to be installed to provide such functionality.

Let's use officially supported ``aiohttp_jinja2`` for famous ``jinja2`` template engine (http://aiohttp_jinja2.readthedocs.org/).


aiohttp-jinja2
--------------

Install the dependencies::


    (.venv) python3.7 -m pip install -U jinja2 aiohttp-jinja2


Code structure::

    /jinja_server.py
    /templates/base.html


Sample HTML template:

.. literalinclude:: ../code/06-templates/templates/example.html


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
now. ``@aiohttp_jinja2.template()`` decorator renders the context and returns
``web.Response`` object automatically.


Render posts list
-----------------

.. literalinclude:: ../code/06-templates/yy-full.py
   :pyobject: index

``index.html`` template:

.. literalinclude:: ../code/06-templates/templates/index.html

``base.html`` for template inheritance:

.. literalinclude:: ../code/06-templates/templates/base.html
   :language: html

Post editing
------------

Show edit form
^^^^^^^^^^^^^^

.. literalinclude:: ../code/06-templates/yy-full.py
   :pyobject: edit_post

``edit.html`` template:

.. literalinclude:: ../code/06-templates/templates/edit.html

Multipart content
^^^^^^^^^^^^^^^^^

We use ``method="POST" enctype="multipart/form-data"`` to send form data.

Sent body looks like::

    ------WebKitFormBoundaryw6YN2HqrOi6hewhP
    Content-Disposition: form-data; name="title"

    title 1
    ------WebKitFormBoundaryw6YN2HqrOi6hewhP
    Content-Disposition: form-data; name="text"

    text of post
    ------WebKitFormBoundaryw6YN2HqrOi6hewhP--

Applying edited form data
^^^^^^^^^^^^^^^^^^^^^^^^^

There is ``POST`` handler for ``/{post}/edit`` along with ``GET`` to apply a new data:

.. literalinclude:: ../code/06-templates/yy-full.py
   :pyobject: edit_post_apply

.. note::

   ``POST`` handler doesn't render HTML itself but returects to ``GET /{post}/edit``
   page.

HTML site endpoints
-------------------

`GET /`
  List posts.

`GET /new`
  Show form for adding post

`POST /new`
  Apply post adding

`GET /{post}/view`
  Show post

`GET /{post}/edit`
  Edit post

`GET /{post}/edit`
  Show edit post form

`POST /{post}/edit`
  Apply post editing

`GET /{post}/delete`
  Delete post



.. note::

   URLs order does matter: ``/new`` should lead ``/{post}``, otherwise ``/{post}`` web
   handler is called with ``new`` post id.

Full example for templated server
---------------------------------

Example for HTML version of blogs server: :ref:`full-template-server`


.. toctree::
   :hidden:

   aiohttp_templates_full
