import requests

response = requests.get('http://www.google.com')   # веб-запрос ограничен производительностью ввода-вывода
items = response.headers.items()
headers = [f'{key}: {headers}' for key, headers in items]   # обработка ограничена быстродействием процессора
formatted_headers = '\n'.join(headers)  # конкатетация строк ограничена быстродействием процессора
with open('headers.txt', 'w') as file:
    file.write(formatted_headers)   # Запись на диск ограничена производительностью ввода-вывода
