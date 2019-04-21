import time

import requests


def download_pep(pep_number: int) -> bytes:

    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"
    print(f"Begin downloading {url}")
    response = requests.get(url)
    print(f"Finished downloading {url}")
    return response.content


def write_to_file(pep_number: int, content: bytes) -> None:

    filename = f"sync_{pep_number}.html"

    with open(filename, "wb") as pep_file:
        print(f"Begin writing to {filename}")
        pep_file.write(content)
        print(f"Finished writing {filename}")


if __name__ == "__main__":
    s = time.perf_counter()

    for i in range(8010, 8016):
        content = download_pep(i)
        write_to_file(i, content)

    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")

# Begin downloading https://www.python.org/dev/peps/pep-8010/
# Finished downloading https://www.python.org/dev/peps/pep-8010/
# Begin writing to 8010.html
# Finished writing 8010.html
# Begin downloading https://www.python.org/dev/peps/pep-8011/
# Finished downloading https://www.python.org/dev/peps/pep-8011/
# Begin writing to 8011.html
# Finished writing 8011.html
# Begin downloading https://www.python.org/dev/peps/pep-8012/
# Finished downloading https://www.python.org/dev/peps/pep-8012/
# Begin writing to 8012.html
# Finished writing 8012.html
# Begin downloading https://www.python.org/dev/peps/pep-8013/
# Finished downloading https://www.python.org/dev/peps/pep-8013/
# Begin writing to 8013.html
# Finished writing 8013.html
# Begin downloading https://www.python.org/dev/peps/pep-8014/
# Finished downloading https://www.python.org/dev/peps/pep-8014/
# Begin writing to 8014.html
# Finished writing 8014.html
# Begin downloading https://www.python.org/dev/peps/pep-8015/
# Finished downloading https://www.python.org/dev/peps/pep-8015/
# Begin writing to 8015.html
# Finished writing 8015.html
# Execution time: 3.60 seconds.
