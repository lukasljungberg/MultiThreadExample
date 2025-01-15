import asyncio
import random

# The idea is to create a class for the protocol
async def produce_send_raw_data(data, queue: asyncio.Queue=None):
    await queue.put("__producer__")
    await queue.put(data)
    print("In producer: ", data)


