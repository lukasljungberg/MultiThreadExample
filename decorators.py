import asyncio
import functools
from threading import Thread
from producers import produce_send_raw_data
from consumers import consumer_retrieve_raw_data



def producer(shared_queue: asyncio.Queue):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Set producer, consumer
            data = func(*args, **kwargs)
            produce = produce_send_raw_data
            # Print the args
            print("From decorator: ", args, kwargs)
            # Run the function
            def run():
                async def main():
                    await asyncio.create_task(produce(data, shared_queue))
                asyncio.run(main())
            t = Thread(target=run)
            t.start()
            return data
        return wrapper
    return decorator

def consumer(shared_queue: asyncio.Queue):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Set producer, consumer
            data = func(*args, **kwargs)
            consume = consumer_retrieve_raw_data
            # Print the args
            print("From decorator: ", args, kwargs)
            # Run the function
            def run():
                async def main():
                    await asyncio.create_task(consume(shared_queue))
                asyncio.run(main())
            t = Thread(target=run)
            t.start()
            return data
        return wrapper
    return decorator

