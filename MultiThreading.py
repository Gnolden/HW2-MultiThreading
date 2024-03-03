import asyncio
import aiohttp
import platform


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]

        responses = await asyncio.gather(*tasks)
        return responses


async def main():
    urls = [f"https://dummyjson.com/products/{x}" for x in range(1, 101)]

    responses = await fetch_all_urls(urls)
    # for url, response in zip(urls, responses):
    #     print(f"Response from {url}: {response[:50]}...")

    with open('response.json', 'w', encoding="utf-8") as f:
        jhon = ',\n'.join(responses)
        f.write(f"[\n{jhon}\n]")


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
