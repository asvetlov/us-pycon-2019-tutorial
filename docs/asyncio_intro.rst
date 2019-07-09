Intro to asyncio
================


What does it mean for something to be **asynchronous**?

It means that being able to do multiple things at once. The :mod:`asyncio <python:asyncio>` library
in Python provides the framework to do this.

Consider a scenario where you have a long running task, which you'd like to
perform multiple times. In a traditional synchronous programming, you'd execute
one task after another. If one task is taking 10 seconds to complete, running
the task 6 times will take 1 full minute.

Here's a simple code to demonstrate that:

.. literalinclude:: ../code/01-intro-asyncio/sync_demo.py


In the above example, we wanted to run ``long_running_task`` 3 times, each with
varying time to complete.

When the code run, we can see the following output::

    Begin sleep for 2
    Awake from 2
    Begin sleep for 10
    Awake from 10
    Begin sleep for 5
    Awake from 5
    Execution time: 17.01 seconds.

The above was an example of **synchronous** execution, the ``long_running_task``
was executed one at a time, and each time we're waiting for it to complete
before starting another one.

Now let's take a look on how it would look like if we're running it **asynchronously**
using asyncio.

First we convert the ``long_running_task`` into a coroutine, by adding the keyword
``async``::

    import asyncio


    async def long_running_task(time_to_sleep):
        print(f"Begin sleep for {time_to_sleep}")
        await asyncio.sleep(time_to_sleep)
        print(f"Awake from {time_to_sleep}")


Note that coroutine cannot simply be called like regular functions. For example,
you can type the following::

    >>> long_running_task()
    <coroutine object task at 0x1016dff40>

But the code was not executed. It does not print out ``Begin sleep ..`` or ``Awake from``.

To actually execute the coroutine, you have three options:

- using :func:`asyncio.run() <python:asyncio.run>`

::

    asyncio.run(long_running_task(3))

- **await**-ing the coroutine

::

    async def main():
        await long_running_task(3)

    asyncio.run(main())

- using :func:`asyncio.create_task() <python:asyncio.create_task>`

::

    async def main():
        task = asyncio.create_task(long_running_task(3))

        await task

    asyncio.run(main())


Suppose now we want to execute ``long_running_task`` three times **asynchronously**:

.. literalinclude:: ../code/01-intro-asyncio/async_demo.py

The output::

    Begin sleep for 2
    Begin sleep for 10
    Begin sleep for 5
    Awake from 2
    Awake from 5
    Awake from 10
    Execution time: 10.01 seconds.

Notice how the tasks are all starting at about the same time, and that the third
(5) task was completed before the second one (10) was finished. The total time
taken was faster compared to when it was run synchronously.
