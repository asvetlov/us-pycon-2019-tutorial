Hands-on Intro to aiohttp
=========================

Description
------------

Asyncio is a relatively new feature in Python, with the async and await syntaxes only recently became proper keywords in Python 3.7. Asyncio allows you to write asynchronous programs in Python. In this tutorial, we’ll introduce you to an asyncio web library called aiohttp.

aiohttp is a library for building web client and server using Python and asyncio. We’ll introduce you to several key features of aiohttp; including routing, session handling, templating, using middlewares, connecting to database, and making HTTP GET/POST requests. We’ll provide best practises in building your aiohttp application, as well as how to write tests for your application.

We’ll use all new Python 3.7 features to build web services with asyncio and aiohttp. 

Audience
---------

Intermediate/Advanced skill level.

Participants should know how to program in Python, have a GitHub account, know how to commit their work using git and to create pull requests, and understand how REST API works. They should also be familiar with the concept of Python virtual environments and installing Python libraries using pip.
Prior to attending the tutorial, participant should have Python 3.7 installed on their laptop.

This tutorial is not suitable for novices or someone new to Programming.

For this tutorial, we will deploy the code to Heroku and GitHub. Participant may want to reconsider taking this tutorial if there is anything preventing them from uploading their source code to the cloud services like Heroku or GitHub.

Outline
-------

1. Introduction (5 minutes)
- Go over the agenda
- Who we are: Python core developers, maintainer and long time user of aiohttp

2. Intro to asyncio (10 minutes)
- Explanation and demo of concurrency in Python

3. Intro to aiohttp (10 minutes)
- Why use aiohttp
- Provide documentation links: https://aiohttp.readthedocs.io/
- Examples of web apps with aiohttp

4. Hands-on intro to aiohttp server (30 minutes)
- Write our first aiohttp web server
- Introduce how to add routes/url
- Introduce how to handle GET and POST requests (useful for serving REST API)
- Provide example of how to handle file upload to the web server

5. Hands-on intro to aiohttp client (20 minutes)
- Write our first aiohttp client
- Introduce how to make GET and POST requests (useful for making REST API calls)
- Provide example of how to submit form and file upload
- Provide example of how to add request headers

6. Hands-on intro to HTML template with aiohttp (30 minutes)
- Introduce aiohttp-jinja2 renderer, and use it in the web server
- Provide example on how to structure the project (separating Python codebase and HTML templates directory)
- Documentation: http://aiohttp_jinja2.readthedocs.org/

7. Hands-on intro to middlewares (20 minutes)
- Introduce the concept of middleware, and when to use them
- Introduce how to add middleware to aiohttp server
- Provide example of error handling using middleware
- Documentation: https://aiohttp.readthedocs.io/en/stable/web_advanced.html#aiohttp-web-middlewares

8. Hands-on intro to session handling (20 minutes)
- Introduce how to handle user sessions/logging in and out on the web server

9. Hands-on intro to writing unit tests for aiohttp app (30 minutes)
- Writing tests for aiohttp client 
- Writing tests for aiohttp server
- Tests using pytest and pytest-asyncio.

10. Extra time to finish exercises and QA


Additional Notes
----------------

This is a brand new tutorial that we’ve crafted especially for PyCon US. This tutorial will be presented by two experienced presenters: Mariatta Wijaya and Andrew Svetlov.

Mariatta Wijaya is a Python core developer, and has experience giving talks, keynotes and tutorial all over the world. She has given the Build-a-GitHub-Bot Workshop at PyCon US 2018 [1]. For the past two years, Mariatta has been building web services using aiohttp, notably CPython’s GitHub bots [2] and PyCascades Code of Conduct Hotline [3].

Andrew Svetlov is a Python core developer, and the author of aiohttp library. Andrew has also authored and maintained various other asyncio-based libraries [4], and have spoken at various Python conferences.

If accepted, we can only give the tutorial on Thursday. This is because both presenters will be attending Python Language Summit on Wednesday. Mariatta is the chair of Python Language Summit 2019 and 2020.

[1] https://www.youtube.com/watch?v=ZwvjtCjimiw
[2] https://github.com/python/miss-islington and https://github.com/python/bedevere
[3] https://github.com/Mariatta/enhanced-coc-hotline
[4] https://github.com/aio-libs 


