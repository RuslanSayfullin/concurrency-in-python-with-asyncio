# Задание тайм-аута для as_completed
import asyncio
import aiohttp

from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.google.com', 1),
            fetch_status(session, 'https://www.google.com', 10),
            fetch_status(session, 'https://www.google.com', 10)]
        
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')
        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main())