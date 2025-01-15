from flask import Flask
from decorators import producer, consumer
import asyncio
app = Flask(__name__)
shared_queue = asyncio.Queue()
@app.route('/start_producer', methods=['GET'])
@producer(shared_queue)
async def start_producer():
    return "from_producer"

@app.route('/start_consumer', methods=['GET'])
@consumer(shared_queue)
async def start_consumer():
    return "from_consumer"

if __name__ == '__main__':
    app.run()
