import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8080))
s.listen(1)

print("Palindrome Server Started...")

conn, addr = s.accept()

data = conn.recv(1024).decode()

rev = data[::-1]

if data == rev:
    result = "Palindrome"
else:
    result = "Not Palindrome"

conn.send(result.encode())

print("Result:", result)

conn.close()
s.close()
