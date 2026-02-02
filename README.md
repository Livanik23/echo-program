#Echo сервер и клиент на Python
=
*Cервер принимает соединение от клиента, получает строку и отправляет её обратно (echo). Клиент подключается к серверу, отправляет сообщение и выводит ответ.*

Требования
* Python 3.x
* Операционная система Windows / Linux / macOS

Файлы
* echo-server.py — серверная часть.
* echo-client.py — клиентская часть.

Код
echo-server.py
```python
import socket

HOST = "0.0.0.0"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)
                conn.sendall(data)
```

echo-client.py
```python
import socket

HOST = "10.90.14.20"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello")
    data = s.recv(1024) 
```
print(f"Received {data!r}")

#Настройка адреса и порта
*Если хотите, чтобы сервер был доступен с другой машины в сети, установите в echo-server.py:
* HOST = "0.0.0.0" (слушать на всех интерфейсах),
* а в echo-client.py укажите реальный IP‑адрес сервера.
*Порт PORT можно изменить на любой свободный (например, 5000, 8000 и т.п.), но значения в сервере и клиенте должны совпадать.
