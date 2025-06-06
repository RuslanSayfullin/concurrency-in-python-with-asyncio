# Исполнитель пула процессов в сочетании с asyncio
import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List

def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter += 1
        return counter

async def main():
    with ProcessPoolExecutor() as process_pool:
        # Создать частично применяемую функцию count с фиксированным аргументом
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 100000000]
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))
        
        results = await asyncio.gather(*call_coros)  # ждём получения результатов

        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())

