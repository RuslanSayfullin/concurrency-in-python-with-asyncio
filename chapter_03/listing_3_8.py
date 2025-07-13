# построение асинхронного эхо-сервера
import asyncio
import socket


async def echo(
        connection: socket, 
        loop: asyncio.AbstractEventLoop
) -> None:
    while data := await loop.sock_recv(connection, 1024):
        # В бесконечном цикле ожидаем данных от клиента
        await loop.sock_sendall(connection, data)   # получив данный, отправляем их обратно клиенту

async def listen_for_connection(
        server_socket: socket, 
        loop: asyncio.AbstractEventLoop
):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}")
        asyncio.create_task(echo(connection, loop))  # после получения запроса

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    await listen_for_connection(server_socket, asyncio.get_event_loop())
    asyncio.run(main())
