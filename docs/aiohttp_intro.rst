Intro to aiohttp
================

In the previous section, we've got a taste of what **asynchronous** task execution
looks like using :mod:`asyncio <python:asyncio>` library.

The example before was quite simple, and perhaps not very exciting. Let's now try
building something bigger, like our own web scraper. A web scraper is a way to extract
data from websites. It is a way to copy/download data programmatically.

For demonstration purpose, we'll try downloading some PEPs and save them to
our local machine for further analysis.

The PEPs we want to download are the governance PEPs:

- PEP 8010: https://www.python.org/dev/peps/pep-8010/

- PEP 8011: https://www.python.org/dev/peps/pep-8011/

- PEP 8012: https://www.python.org/dev/peps/pep-8012/

- PEP 8013: https://www.python.org/dev/peps/pep-8013/

- PEP 8014: https://www.python.org/dev/peps/pep-8014/

- PEP 8015: https://www.python.org/dev/peps/pep-8015/

- PEP 8016: https://www.python.org/dev/peps/pep-8016/

Downloading contents synchronously
----------------------------------

First, let us try doing this **synchronously** using the `requests`_ library.
It can be installed using pip.

::

    python3.7 -m pip install requests


Downloading an online resource using `requests`_ is straightforward.

::

    import requests

    response = requests.get("https://www.python.org/dev/peps/pep-8010/")
    print(response.content)

It will print out the HTML content of `PEP 8010`_. To save it locally to a file::

    filename = "sync_pep_8010.html"

    with open(filename, "wb") as pep_file:
        pep_file.write(content.encode('utf-8'))

The file ``sync_pep_8010.html`` will be created.

💡 Exercise
-----------

Let's take the next 10-15 minutes to write a script that will programmatically
download PEPs 8010 to 8015 using `requests`_ library.

Solution
--------

Here is an example solution. It is ok if yours do not look exactly the same.

.. literalinclude:: ../code/02-intro-aiohttp/requests_demo.py

In the above solution, we're downloading the PEP one at a time. From previous
section, we know that using :mod:`asyncio <python:asyncio>`, we can run the
same task **asynchronously**. `requests`_ itself is not an asyncio library.
Enter `aiohttp`_.

Downloading contents asynchronously
-----------------------------------

Install `aiohttp`_ if you have not already::

    python3.7 -m pip install aiohttp


Here's an example of downloading an online resource using `aiohttp`_.

::

    import asyncio
    import aiohttp

    async def download_pep(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                content = await resp.read()
                print(content)
                return content

    asyncio.run(download_pep("https://www.python.org/dev/peps/pep-8010/"))


Writing the downloaded content to a new file can be done as its own coroutine.

::

    async def write_to_file(pep_number, content):
        filename = f"async_{pep_number}.html"
        with open(filename, "wb") as pep_file:
            pep_file.write(content)

Since we now have two coroutines, we can execute them like so::


    async def web_scrape_task(pep_number):
        url = f"https://www.python.org/dev/peps/pep-{pep_number}/"

        downloaded_content = await download_pep(url)
        await write_to_file(pep_number, downloaded_content)


    asyncio.run(web_scrape_task(8010))



💡 Exercise
-----------

The code is looking more complex than when we're doing it synchronously, using
`requests`_. But you got this. Now that you know how to download an online
resource using aiohttp, now you can download multiple pages asynchronously.

Let's take the next 10-15 minutes to write the script for downloading PEPs
8010 - 8015 using aiohttp.


Solution
--------

Here is an example solution. It is ok if yours do not look exactly the same.

.. literalinclude:: ../code/02-intro-aiohttp/aiohttp_demo.py

While the code looks longer and more complex than our solution using `requests`_,
by executing the code asynchronously, the task is taking less time to complete.

Why aiohttp
-----------

- Web frameworks like `Django`_ and Flask don't support :mod:`asyncio <python:asyncio>`.

- aiohttp provides the framework for both web Server and Client. For example,
  `Django`_ is mainly the framework you'd use if you need a server, and you'll
  use it in conjuction with `requests`_.

We're not advocating for you to replace your existing web application with `aiohttp`_.
Each framework comes with their own benefits. Our goal in this tutorial is to learn
something new together, and be comfortable working with asyncio.


.. _`Django`: https://docs.djangoproject.com/

.. _`aiohttp`: https://aiohttp.readthedocs.io

.. _`requests`: https://2.python-requests.org//en/master/

.. _`PEP 8010`: https://www.python.org/dev/peps/pep-8010/
