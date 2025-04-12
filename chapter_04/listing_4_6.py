#Конкурентное выполнение запросов с по­мощью gather
import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_4 import fetch_status
from util import async_timed

# Сгенерировать список сопрограмм
@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://google.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

asyncio.run(main())