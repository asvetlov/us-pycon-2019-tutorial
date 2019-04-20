import asyncio
import time


async def long_running_task(time_to_sleep):
    print(f"Begin sleep for {time_to_sleep}")
    await asyncio.sleep(time_to_sleep)
    print(f"Awake from {time_to_sleep}")


async def main():
    task1 = asyncio.create_task(long_running_task(2))
    task2 = asyncio.create_task(long_running_task(10))
    task3 = asyncio.create_task(long_running_task(5))
    await (asyncio.wait([task1, task2, task3]))


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")
