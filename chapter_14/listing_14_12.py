# Реализация цикла событий
import functools
import selectors
from typing import List
from chapter_14.listing_14_11 import CustomTask
from chapter_14.listing_14_8 import CustomFuture

class EventLoop:
    _tasks_to_run: List[CustomTask] = []

    def __init__(self):
        self.selector = selectors.DefaultSelector()
        self.current_result = None
    
    def _register_socket_to_read(self, sock, callback):
        future = CustomFuture()
        try:
            self.selector.get_key(sock)
        except KeyError:
            sock.setblocking(False)
            self.selector.register(sock, selectors.EVENT_READ,
                    functools.partial(callback, future))
        else:
            self.selector.modify(sock, selectors.EVENT_READ, functools.partial(callback, future))
            return future

    def _set_current_result(self, result):
        self.current_result = result

    async def sock_recv(self, sock):
        print('Регистрируется сокет для прослушивания данных...')
        return await self._register_socket_to_read(sock, self.recieved_data)
    
    async def sock_accept(self, sock):
        print('Регистрируется сокет для приема подключений...')
        return await self._register_socket_to_read(sock, self.accept_connection)
    
    def sock_close(self, sock):
        self.selector.unregister(sock)
        sock.close()
    
    def register_task(self, task):
        # Зарегистрировать задачу в цикле событий
        self._tasks_to_run.append(task)
    
    def recieved_data(self, future, sock):
        data = sock.recv(1024)
        future.set_result(data)
    
    def accept_connection(self, future, sock):
        result = sock.accept()
        future.set_result(result)

def run(self, coro):
    """Выполнять главную сопрограмму, пока она не завершится,
    и на каждой итерации выполнять готовые к работе задачи"""
    self.current_result = coro.send(None)
    while True:
        try:
            if isinstance(self.current_result, CustomFuture):
                self.current_result.add_done_callback(self._set_current_result)
                if self.current_result.result() is not None:
                    self.current_result = coro.send(self.current_result.result())
                else:
                    self.current_result = coro.send(self.current_result)
        except StopIteration as si:
            return si.value
        
        for task in self._tasks_to_run:
            task.step()
        
        self._tasks_to_run = [task for task in self._tasks_to_run if not task.is_finished()]
        events = self.selector.select()
        print('В селекторе есть событие, обрабатывается...')
        for key, mask in events:
            callback = key.data
            callback(key.fileobj)