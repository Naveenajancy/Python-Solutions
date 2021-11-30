import asyncio
import time

start = time.perf_counter()
async def main():
    print("Hello")
    await asyncio.sleep(4)
    print(".... World !!")

asyncio.run(main())
#print(main())

finish = time.perf_counter()
result = print(f"Total time {round(finish-start, 2)} Second(s)")

