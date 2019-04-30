aiohttp Client
==============

Now we have a REST server, let's write REST client to it.


The idea is: create a ``Client`` class with ``.list()``, ``.get()``, ``.create()``
etc. methods to operate on blog posts collection.

Data structures
---------------

We need a ``Post`` *dataclass* to provide post related fields (and avoid dictionaries in
our API)::

    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Post:
        id: int
        owner: str
        editor: str
        title: str
        text: Optional[str]

        def pprint(self) -> None:
            print(f"Post {self.id}")
            ...


Client class
------------

``Client`` is a class with embedded ``aiohttp.ClientSession``.  Also, we need the REST
server URL to connect and user name to provide creator / last-editor information::

    class Client:
        def __init__(self, base_url: URL, user: str) -> None:
            self._base_url = base_url
            self._user = user
            self._client = aiohttp.ClientSession(raise_for_status=True)

To properly close ``Client`` instance add ``.close()`` method::

    async def close(self) -> None:
        return await self._client.close()

Now is a time for implementing a method to access the REST server, e.g. ``.list()``::

    async def list(self) -> List[Post]:
        async with self._client.get(self._make_url("api")) as resp:
            ret = await resp.json()
            return [Post(text=None, **item) for item in ret["data"]]


It makes ``GET {base_url}/api`` request, read JSON response and returns a list of
``Post`` objects.


``_make_url`` is a helper for prepending *base url* to API endpoints. For the tutorial
it is simple but in real life you often need to do more work, e.g. provide Authorization
HTTP header, sign your request etc.::

    def _make_url(self, path: str) -> URL:
        return self._base_url / path


Client Usage
-------------

The usage is simple::

   async def fetch():
       client = Client("http://localhost:8080", "John")
       try:
          posts = await client.list()
          for post in posts:
              post.pprint()
       finally:
          await client.close()

``try``/``finally`` is not very convinient, many people prefer ``async with``
statement. It saves 3 lines and (more important) avoids silly errors like instantiating
a client variable *inside* ``try``/``finally`` block.

::

   async def fetch():
       async with Client("http://localhost:8080", "John") as client:
          posts = await client.list()
          for post in posts:
              post.pprint()

To support this form we need to implement ``__aenter__`` / ``__aexit__`` async
``Client`` methods::

    async def __enter__(self) -> "Client":
        return self

    async def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Optional[bool]:
        await self.close()

Full Client Example
--------------------

In *full example* we provide a *Command Line Tool* to work with REST API server by using
famous Click_ library.

The *Click* usage is out of scope of the tutorial itself, but you can learn the full
example on your own: :ref:`full-client` .


.. toctree::
   :hidden:

   aiohttp_client_full


.. _Click: https://click.palletsprojects.com/
