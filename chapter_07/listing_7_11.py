from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:        # Захватить блокировку A
        print('Acquired lock a from method a!')
        time.sleep(1)   # Ждать одну секунду;
        with lock_b:    # Захватить блокировку B
            print('Acquired both locks from method a!')


def b():
    with lock_b:        # Захватить блокировку B
        print('Acquired lock b from method b!')
        with lock_a:    # Захватить блокировку A
            print('Acquired both locks from method b!')


thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
