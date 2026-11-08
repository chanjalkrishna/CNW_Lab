import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))

word = input("Enter a word: ")

s.send(word.encode())

result = s.recv(1024).decode()

print("Server Response:", result)

s.close()
