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
            conn.sendall("До свидания!")
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