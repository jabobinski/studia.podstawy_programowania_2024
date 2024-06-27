import asyncio
import time

async def task(name, seconds):
    print(f"Task {name} started")
    await asyncio.sleep(seconds)
    print(f"Task {name} completed after {seconds} seconds")

async def main():
    # List of tasks to run concurrently
    tasks = [
        task("A", 2),
        task("B", 1),
        task("C", 3)
    ]
    
    # Measure the starting time
    start_time = time.time()
    
    # Run tasks concurrently using asyncio.gather()
    await asyncio.gather(*tasks)
    
    # Measure the ending time
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"All tasks completed in {elapsed_time:.2f} seconds")

# Run the main coroutine in the event loop
asyncio.run(main())
