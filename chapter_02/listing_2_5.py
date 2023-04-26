import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)      # Приостановить hello_world_message на 1 с
    return "Привет Мир!"


async def main() -> None:
    message = await hello_world_message()   # Приостановить main до завершения hello_world_message
    print(message)


asyncio.run(main())
