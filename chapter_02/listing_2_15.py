from asyncio import Future
import asyncio


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))   # Создать задачу, которая асинхронно установит значение future
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)  # Ждать 1 с, прежде чем установить значение
    future.set_result(42)


async def main() -> None:
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())
