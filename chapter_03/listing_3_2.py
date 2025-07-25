# Чтение данных из сокета
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)  # прослушиваем запросы на подключение
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f"Получен пароль на подключение {client_address}!")

    buffer = b''

    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"Получены данные: {data}!")
            buffer += data
    print(f'Все данные: {buffer}')
    connection.sendall(buffer)
finally:
    server_socket.close()
