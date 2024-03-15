# Изучение поведения wait по умолчанию
import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.google.com')), 
                    asyncio.create_task(fetch_status(session, 'https://www.google.com'))]
        done, pending = await asyncio.wait(fetchers)
        
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        
        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())