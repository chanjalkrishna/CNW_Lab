import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))

n = input("Enter number of terms: ")

s.send(n.encode())

data = s.recv(1024).decode()

print("Fibonacci Series:", data)

s.close()
