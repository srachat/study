import asyncio
import time


def inner(description, start, end):
    for i in range(start, end):
        value = yield i
        print(f"{description} got: {value}")
    print(f"{description} finished at {end - 1}")
    return end


def general():
    start = yield from inner("first", 1, 5)
    end = yield from inner("second", start, 10)
    return end


async def my_coroutine(number):
    print(f"Starting coroutine number {number} at {time.time()}")
    await asyncio.sleep(2)
    print(f"Finishing coroutine number {number} at {time.time()}")


async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))


asyncio.run(main())
