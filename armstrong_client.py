import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

num = input("Enter a Number: ")

s.send(num.encode())

result = s.recv(1024).decode()

print(result)

s.close()
