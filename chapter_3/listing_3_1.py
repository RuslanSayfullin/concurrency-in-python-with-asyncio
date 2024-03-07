# запуск сервера и прослушивание порта для подключения
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockport(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)  # прослушиваем запросы на подключение
server_socket.listen()

connection, client_address = server_socket.accept()
print(f'Полчен запрос на подключение от {client_address}!')
