import socket

HOST = "127.0.0.1"
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