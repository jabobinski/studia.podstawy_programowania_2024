import asyncio

async def print_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)

async def main():
    await print_numbers()

# Create an asyncio event loop
loop = asyncio.get_event_loop()

# Run the main coroutine in the event loop
loop.run_until_complete(main())

# Close the event loop
loop.close()
