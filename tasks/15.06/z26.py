import asyncio

async def time_consuming_task():
    try:
        print("Starting time-consuming task...")
        await asyncio.sleep(5)  # Simulate a time-consuming operation (5 seconds)
        print("Time-consuming task completed.")
    except asyncio.CancelledError:
        print("Time-consuming task was cancelled.")

async def main():
    task = asyncio.create_task(time_consuming_task())

    # Wait for a bit before cancelling the task
    await asyncio.sleep(2.5)

    # Cancel the task
    task.cancel()

    try:
        await task  # Wait for the task to be cancelled
    except asyncio.CancelledError:
        print("Task cancellation handled in main.")

# Run the main coroutine in the event loop
asyncio.run(main())
