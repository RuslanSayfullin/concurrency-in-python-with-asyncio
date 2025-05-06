# Взаимоблокировка
from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()

def a():    
    # Захватить блокировку A
    with lock_a:
        print('Захвачена блокировка a из метода a!')
        # Ждать одну секунду; это создает подходящие условия для взаимоблокировки
        time.sleep(1)
        # Захватить блокировку B
        with lock_b:
            print('Захвачены обе блокировки из метода a!')

def b():
    # Захватить блокировку B
    with lock_b:
        print('Захвачена блокировка b из метода b!')
        # Захватить блокировку A
        with lock_a:
            print('Захвачены обе блокировки из метода b!')

thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()