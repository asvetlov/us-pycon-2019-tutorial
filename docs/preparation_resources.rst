Preparation
===========

Before coming to the tutorial, please do the following:

1. Have Python 3.7 installed in your laptop. **Note:** It's important that you're running Python 3.7
   (or above) because we will use some of the new features added in 3.7 in this tutorial.

   * `Here's a tutorial that will help you get set up. <https://realpython.com/installing-python/>`__

2. Install the dependencies, preferably in a virtual environment. For this tutorial,
   we'll use ``venv``.

Create a new virtual environment using venv::

    python3.7 -m venv .venv

Activate the virtual environment. On Unix, Mac OS::

    source .venv/bin/activate

On Windows::

    .venv\Scripts\activate.bat


Install the dependencies, listed in the `requirements.txt <https://github.com/asvetlov/us-pycon-2019-tutorial/blob/master/requirements.txt>`_ file. You can download
the file, or `clone this repository <https://github.com/asvetlov/us-pycon-2019-tutorial>`_::

   (.venv) python -m pip install -U pip -r requirements.txt


3. Verify that you correctly have Python 3.7 installed. If you're able the following
   code, then you're good to go.


.. literalinclude:: ../code/00-preparation/hello.py


Resources and documentation links
---------------------------------

Tools and documentations that we'll use throughout this tutorial.


venv
''''

`Python venv tutorial`_ documentation.


aiohttp
'''''''

- Installation: ``python3.7 -m pip install aiohttp``.

- `aiohttp documentation`_

- `aiohttp`_ source code

- Owner: `Andrew Svetlov <http://asvetlov.blogspot.ca/>`_


f-strings
'''''''''

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
'''''''

`aiohttp`_ is async Python library. Read up the `quick intro <https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/>`_
to asyncio.

type annotations
''''''''''''''''

Our code examples use type annotations and checked with ``mypy``. It is optional.

- typing documentation: https://docs.python.org/3/library/typing.html

- mypy documentation: https://mypy.readthedocs.io/en/stable/

dataclass
'''''''''


The :mod:`dataclass <python:dataclasses>` module provides a decorator and functions
for automatically adding generated special methods such as ``__init__()`` and ``__repr__()``
to user-defined classes. It was originally described in `PEP 557 <https://www.python.org/dev/peps/pep-0557/>`_.

Example::

    @dataclass
    class InventoryItem:
        '''Class for keeping track of an item in inventory.'''
        name: str
        unit_price: float
        quantity_on_hand: int = 0

        def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand

`dataclass documentation`_.

aiohttp-jinja2
''''''''''''''

`jinja2 <http://jinja.pocoo.org/>`_ template renderer for `aiohttp.web
<https://aiohttp.readthedocs.io/en/stable/web.html#aiohttp-web>`_.

`aiohttp-jinja2 documentation`_.

aiohttp-session
'''''''''''''''

https://aiohttp-session.readthedocs.io/en/stable/


click
'''''

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.
It’s the “Command Line Interface Creation Kit”.

`click documentation`_.


.. _`aiohttp-jinja2 documentation`: https://aiohttp-jinja2.readthedocs.io/en/stable/

.. _`click documentation`: https://click.palletsprojects.com/en/7.x/

.. _`aiohttp documentation`: https://aiohttp.readthedocs.io

.. _`Python venv tutorial`: https://docs.python.org/3/tutorial/venv.html

.. _`dataclass documentation`: https://docs.python.org/3/library/dataclasses.html


