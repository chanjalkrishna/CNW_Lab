import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8080))

s.listen()

print("Chat Server Started...")

clients = []

def handle_client(conn, addr):
    print("Connected:", addr)

    while True:
        try:
            msg = conn.recv(1024).decode()

            if not msg:
                break

            print("Message:", msg)

            for client in clients:
                if client != conn:
                    client.sendall(msg.encode())

        except:
            break

    if conn in clients:
        clients.remove(conn)

    conn.close()
    print("Client disconnected")

while True:
    conn, addr = s.accept()

    clients.append(conn)

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    thread.start()
