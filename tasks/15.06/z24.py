import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_multiple_urls(urls):
    tasks = []
    for url in urls:
        tasks.append(fetch_data(url))
    return await asyncio.gather(*tasks)

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2'
    ]
    results = await fetch_multiple_urls(urls)
    for idx, result in enumerate(results):
        print(f"Data from URL {urls[idx]}:")
        print(result)
        print("=" * 30)

# Run the main coroutine in the event loop
asyncio.run(main())
