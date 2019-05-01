aiohttp Writing tests
=====================

There are several tools for testing Python code.

We show how to work with the most powerful and popular tool called pytest_ .

We need to install ``pytest`` itself and ``pytest-aiohttp`` plugin first::

   pip install pytest
   pip install pytest-aiohttp

.. note::

   ``pytest-aiohttp`` is not compatible with another pupular plugin ``pytest-asyncio``.


Making test asynchronous
------------------------

Just use ``async def test_*()`` instead of plain ``def test_*()``. ``pytest-aiohttp``
does all dirty work for you::

    async def test_a():
        await asyncio.sleep(0.01)
        assert 1 == 2  # False

Testing server code
-------------------


Testing client with fake server
-------------------------------

Working with HTTPS
------------------

Client mocking
--------------

There is ``aioresponses`` third-party library::

    pip install aioresponses

Usage::

    from aioresponses import aioresponses

    async def test_request():
        with aioresponses() as mocked:
            mocked.get('http://example.com', status=200, body='test')
            session = aiohttp.ClientSession()
            resp = await session.get('http://example.com')

            assert resp.status == 200
            assert "test" == await resp.text()



TBD (by Andrew)

- Writing tests for aiohttp client
- Writing tests for aiohttp server
- Tests using pytest and pytest-asyncio.


.. _pytest: https://docs.pytest.org
