# Выполнение счетного кода в отладочном режиме
import asyncio
from async_timed import async_timed

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(1000000):
        counter += 1
    return counter

async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one

asyncio.run(main(), debug=True)
