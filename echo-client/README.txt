# echo-server.py - Многопоточный эхо-сервер
import socket
import threading

HOST = "0.0.0.0"
PORT = 65432

def handle_client(conn, addr):
    print(f"Подключен клиент {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"Клиент {addr} отключился")
            break
        message = data.decode('utf-8').strip()
        print(f"От {addr}: {message}")
        if message.lower() == 'exit':
            conn.sendall(b"До свидания!")
            break
        conn.sendall(data)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Сервер слушает {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()
python
# echo-client.py - Интерактивный клиент
import socket

HOST = "127.0.0.1"  # Или твой серверный IP, например "10.90.14.20"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Подключен к {HOST}:{PORT}")
    print("Введите сообщения (exit для выхода):")
    while True:
        message = input("> ")
        if message.lower() == 'exit':
            s.sendall(b"exit")
            data = s.recv(1024)
            print(f"Сервер: {data.decode('utf-8')}")
            break
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f"Эхо: {data.decode('utf-8')}")
Основные изменения
Сервер теперь использует потоки для одновременной обработки нескольких клиентов. Каждый клиент получает отдельный поток handle_client, который эхит сообщения и закрывает соединение при 'exit'.

Клиент стал интерактивным: вводит сообщения в цикле до 'exit'. Используй 127.0.0.1 для локального тестирования или реальный IP сервера.
​

Запуск
Запусти python echo-server.py

В отдельных терминалах: python echo-client.py

Тестируй несколько клиентов одновременно — сервер обработает всех.
​

Возможности
Несколько клиентов параллельно без блокировок.

Команда exit (без учета регистра) завершает сессию клиента.

Автоматическое закрытие при отключении клиента.

Логи подключений в консоли сервера.
​