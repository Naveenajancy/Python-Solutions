import time
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(10, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    task3 = asyncio.create_task(say_after(0, 'zero-sec'))
    task4 = asyncio.create_task(say_after(5, '5-sec'))
    await task1
    await task2
    await task3
    await task4
    print(f"finished at {time.strftime('%X')}")

#type(main)
asyncio.run(main())
