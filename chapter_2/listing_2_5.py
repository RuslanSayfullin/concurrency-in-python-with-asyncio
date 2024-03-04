#первое применение sleep
import asyncio

async def hello_word_message() -> str:
    await asyncio.sleep(10)   #приостановить hello_world_message на 1 c.
    return 'Hello World!'

async def main() -> None:
    message = await hello_word_message() #приостоновить main до завершения hello_world_message
    print(message)

asyncio.run(main())
