import asyncio
import time

start = time.perf_counter()
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
async def main():
    # await say_after(1, 'Hello!')
    # await say_after(2, 'World!')
    task1 = asyncio.create_task(say_after(1, 'Hello'))
    task2 = asyncio.create_task(say_after(2, 'World'))

    await task1
    await task2

asyncio.run(main())

finish = time.perf_counter()
result = print(f"Total time {round(finish-start, 2)} Second(s)")

