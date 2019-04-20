import asyncio
import time

import aiohttp


async def download_pep(pep_number: int) -> bytes:

    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"
    print(f"Begin downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(f"Finished downloading {url}")
            return content


async def write_to_file(pep_number: int, content: bytes) -> None:
    filename = f"async_{pep_number}.html"
    with open(filename, "wb") as pep_file:
        print(f"Begin writing to {filename}")
        pep_file.write(content)
        print(f"Finished writing {filename}")


async def web_scrape_task(pep_number: int) -> None:
    content = await download_pep(pep_number)
    await write_to_file(pep_number, content)


async def main() -> None:
    tasks = []
    for i in range(8010, 8016):
        tasks.append(web_scrape_task(i))
    await (asyncio.wait(tasks))


if __name__ == "__main__":
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")


# Begin downloading https://www.python.org/dev/peps/pep-8010/
# Begin downloading https://www.python.org/dev/peps/pep-8015/
# Begin downloading https://www.python.org/dev/peps/pep-8012/
# Begin downloading https://www.python.org/dev/peps/pep-8013/
# Begin downloading https://www.python.org/dev/peps/pep-8014/
# Begin downloading https://www.python.org/dev/peps/pep-8011/
# Finished downloading https://www.python.org/dev/peps/pep-8014/
# Begin writing to async_8014.html
# Finished writing async_8014.html
# Finished downloading https://www.python.org/dev/peps/pep-8012/
# Begin writing to async_8012.html
# Finished writing async_8012.html
# Finished downloading https://www.python.org/dev/peps/pep-8013/
# Begin writing to async_8013.html
# Finished writing async_8013.html
# Finished downloading https://www.python.org/dev/peps/pep-8010/
# Begin writing to async_8010.html
# Finished writing async_8010.html
# Finished downloading https://www.python.org/dev/peps/pep-8011/
# Begin writing to async_8011.html
# Finished writing async_8011.html
# Finished downloading https://www.python.org/dev/peps/pep-8015/
# Begin writing to async_8015.html
# Finished writing async_8015.html
# Execution time: 0.87 seconds.
