# Основы будущих обьектов
from asyncio import Future

my_future = Future()

print(f'my_future готов? {my_future.done()}')

my_future.set_result(42)

print(f'my_future готов? {my_future.done()}')
print(f'Какой результат в my_future? Ответ: {my_future.result()}')
