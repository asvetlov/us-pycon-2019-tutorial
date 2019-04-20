import time


def long_running_task(time_to_sleep: int) -> None:
    print(f"Begin sleep for {time_to_sleep}")
    time.sleep(time_to_sleep)
    print(f"Awake from {time_to_sleep}")


def main() -> None:
    long_running_task(2)
    long_running_task(10)
    long_running_task(5)


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")
