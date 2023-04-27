import asyncio
import aiohttp
from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    """Конкурентное выполнение запросов с помощью gather"""
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]     # Сгенерировать список сопрограмм
        status_codes = await asyncio.gather(*requests)              # Ждать завершения всех запросов
        print(status_codes)


asyncio.run(main())
