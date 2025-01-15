# MultiThreadExample
Showing some multithread examples.

### Installation
install flask with async: pip install flask[async]

### Execution
then run: python app.py

and in another terminal start the consumer first:
    curl 127.0.0.1:5000/start_consumer

then start the producer:
    curl 127.0.0.1:5000/start_producer
