#выполнение двух сопрограмм
import asyncio
from delay_functions import delay

async def add_one(number: int) -> int:
    return number +1

async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message()   #приостоновить main до возврата из hello_world_message
    one_plus_one = await add_one(1)         #приостоновить main до возврата из add_one
    print(one_plus_one)
    print(message)

asyncio.run(main())
