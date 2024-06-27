import asyncio
import random

async def producer(queue, producer_id):
    for i in range(5):  # Produce 5 items
        item = random.randint(1, 10)  # Generate a random item
        await queue.put((producer_id, item))
        print(f"Producer {producer_id} added item {item} to the queue")
        await asyncio.sleep(random.uniform(0.5, 1.5))  # Simulate some delay

async def consumer(queue):
    while True:
        item = await queue.get()
        producer_id, value = item
        print(f"Consumer consumed item {value} from producer {producer_id}")
        queue.task_done()
        await asyncio.sleep(1)  # Simulate processing time

async def main():
    queue = asyncio.Queue()

    # Create multiple producers
    producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]

    # Create a single consumer
    consumer_task = asyncio.create_task(consumer(queue))

    # Wait for all producers to finish producing
    await asyncio.gather(*producers)

    # Wait for the consumer to finish consuming
    await queue.join()

    # Cancel the consumer task
    consumer_task.cancel()

# Run the main coroutine in the event loop
asyncio.run(main())
