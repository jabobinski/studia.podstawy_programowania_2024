import asyncio

async def async_operation():
    # Simulate a long-running asynchronous operation
    await asyncio.sleep(3)
    return "Operation completed successfully"

async def main():
    try:
        result = await asyncio.wait_for(async_operation(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out")

# Run the main coroutine in the event loop
asyncio.run(main())
