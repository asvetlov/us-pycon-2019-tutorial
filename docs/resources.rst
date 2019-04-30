Resources
=========

Tools and documentations that we'll use throughout this tutorial.

venv
----

See also: `Python venv tutorial`_ documentation.

It is recommended that you install the Python packages inside a virtual environment.
For this tutorial, we'll use ``venv``.

Create a new virtual environment using venv::

   python3.7 -m venv .venv

Activate the virtual environment. On Unix, Mac OS::

   source .venv/bin/activate

On Windows::

   .venv\Scripts\activate.bat


aiohttp
-------

- Installation: ``python3.7 -m pip install aiohttp``.

- `aiohttp documentation`_

- `aiohttp`_ source code

- Owner: `Andrew Svetlov <http://asvetlov.blogspot.ca/>`_


f-strings
---------

We will use some f-strings during this tutorial.

My `talk <https://speakerdeck.com/mariatta/pep-498-the-monologue>`_ about f-strings.

Example::

   first_name = "bart"
   last_name = "simpson"

   # old style %-formatting
   print("Hello %s %s" % (first_name, last_name))

   # str.format
   print("Hello {first_name} {last_name}".format(first_name=first_name, last_name=last_name))

   # f-string
   print(f"Hello {first_name} {last_name}")

asyncio
-------

`aiohttp` is async Python library. Read up the `quick intro <https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/>`_
to asyncio.


.. _`aiohttp documentation`: https://aiohttp.readthedocs.io

.. _`Python venv tutorial`: https://docs.python.org/3/tutorial/venv.html




