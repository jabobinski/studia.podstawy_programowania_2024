import asyncio

async def print_delayed_message():
    print("Starting async function...")
    await asyncio.sleep(2)
    print("Python Exercises!")

asyncio.run(print_delayed_message())
