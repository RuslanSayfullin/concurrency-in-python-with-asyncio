# создание пула процессов
from multiprocessing import Pool

def say_hello(name: str) -> str:
    return f'Привет, {name}'

if __name__ == "__main__":
    # Создать пул процессов
    with Pool() as process_pool:
        # Выполнить say_hello с аргументом в отдельном процессе и получить результат
        hi_jeff = process_pool.apply(say_hello, args=('Jeff',))
        hi_john = process_pool.apply(say_hello, args=('John',))
        print(hi_jeff)
        print(hi_john)
