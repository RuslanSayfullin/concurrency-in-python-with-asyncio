# Первое применение sleep
import asyncio

async def hello_word_message() -> str:
    await asyncio.sleep(5)   # Приостановить hello_world_message на 1 c.
    return 'Hello World!'

async def main() -> None:
    message = await hello_word_message() # Приостановить main до завершения hello_world_message
    print(message)

asyncio.run(main())
