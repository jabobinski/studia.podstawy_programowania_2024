import asyncio

async def print_name(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    # Define tasks with different delays
    tasks = [
        print_name("Async Function 1 (1 sec delay)", 1),
        print_name("Async Function 2 (2 sec delay)", 2),
        print_name("Async Function 3 (3 sec delay)", 3)
    ]
    
    # Execute tasks concurrently
    await asyncio.gather(*tasks)

# Run the main function within an asyncio event loop
asyncio.run(main())
