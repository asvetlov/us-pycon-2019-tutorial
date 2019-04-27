.. Hands-on Intro to aiohttp (PyCon tutorial) documentation master file, created by
   sphinx-quickstart on Thu Apr 18 10:54:59 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Hands-on Intro to aiohttp (PyCon US 2019 tutorial)
==================================================

Asyncio is a relatively new feature in Python, with the ``async`` and ``await`` syntax
only recently became proper keywords in Python 3.7. Asyncio allows you to write
asynchronous programs in Python. In this tutorial, we’ll introduce you to an
asyncio web library called `aiohttp`_.

`aiohttp`_ is a library for building web client and server using Python and asyncio.
We’ll introduce you to several key features of aiohttp; including routing, session handling,
templating, using middlewares, connecting to database, and making HTTP GET/POST requests.

We’ll use all new Python 3.7 features to build web services with asyncio and aiohttp.

This tutorial is for `PyCon US 2019 <https://us.pycon.org/2019/schedule/presentation/68/>`_
in Cleveland, Ohio. Video recording will be posted once available.

If you have any feedback or questions about this tutorial, please `file an
issue <https://github.com/asvetlov/us-pycon-2019-tutorial>`_.


Code of Conduct
===============

Be open, considerate, and respectful.

License
=======

`CC-BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_.

Agenda
======


.. toctree::
   :titlesonly:

   preparation
   resources
   asyncio_intro
   aiohttp_intro
   aiohttp_server
   aiohttp_client
   aiohttp_templates
   aiohttp_middlewares
   aiohttp_session
   aiohttp_tests
   git-basics

.. _`aiohttp`: https://aiohttp.readthedocs.io
