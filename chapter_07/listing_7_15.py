# Приложение для нагрузочного тестирования
import asyncio
from asyncio import AbstractEventLoop

from threading import Thread
from chapter_07.listing_7_14 import LoadTester

class ThreadedEventLoop(Thread):
    # Создать новый класс потока
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True
    
    def run(self):
        self._loop.run_forever()

loop = asyncio.new_event_loop()
asyncio_thread = ThreadedEventLoop(loop)
# Запустить новый поток, исполняющий цикл событий asyncio в фоновом режиме
asyncio_thread.start()

app = LoadTester(loop)
app.mainloop()