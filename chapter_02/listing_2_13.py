# Защита задачи от снятия 
import asyncio
from delay_functions import delay

async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5с, скоро она закончится!")
        result = await task
        print(result)

asyncio.run(main())
