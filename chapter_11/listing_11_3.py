# Состояние гонки с участием словарей
import asyncio


class MockSocket:
    def __init__(self):
        self.socket_closed = False

    async def send(self, msg: str):
        if self.socket_closed:
            raise Exception('Сокет закрыт!')
        print(f'Отправляется: {msg}')
        await asyncio.sleep(1)
        print(f'Отправлено: {msg}')
    
    def close(self):
        self.socket_closed = True


user_names_to_sockets = {'John': MockSocket(),
                        'Terry': MockSocket(),
                        'Graham': MockSocket(),
                        'Eric': MockSocket()}

async def user_disconnect(username: str):
    # Отключить пользователя и удалить его из памяти приложения
    print(f'{username} отключен!')
    socket = user_names_to_sockets.pop(username)
    socket.close()

async def message_all_users():
    # Отправить сообщения всем пользователям конкурентно
    print('Создаются задачи отправки сообщений')
    messages = [socket.send(f'Привет, {user}') for user, socket in user_names_to_sockets.items()]
    await asyncio.gather(*messages)

async def main():
    await asyncio.gather(message_all_users(), user_disconnect('Eric'))

asyncio.run(main())