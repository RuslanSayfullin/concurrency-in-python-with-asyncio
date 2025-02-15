# Использование await для ожидания результата сопрограммы
import asyncio

async def add_one(number: int) -> int:
    return number + 1

async def main() -> None:
    one_plus_one = await add_one(1) # Приостановиться и ждать результата add_one(1)
    one_plus_two = await add_one(2) # Приостановиться и ждать результата add_one(1)
    
    print(one_plus_one)
    print(one_plus_two)

asyncio.run(main())

