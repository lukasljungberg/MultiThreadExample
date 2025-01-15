import asyncio
import random

# The idea is to create a class for the protocol
async def consumer_retrieve_raw_data(queue: asyncio.Queue=None):
    await queue.put("__consumer__")
    while True:
        temp = await queue.get()
        if temp == "__producer__":
            item = await queue.get()
            break
        await queue.put("__consumer__")
    print("In consumer: ", item)