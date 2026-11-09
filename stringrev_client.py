import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))

string = input("Enter a String: ")

s.send(string.encode())

data = s.recv(1024).decode()

print("Reversed String:", data)

s.close()
