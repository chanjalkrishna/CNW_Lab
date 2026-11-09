import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(1)

print("Server Started")

conn, addr = s.accept()

num = int(conn.recv(1024).decode())

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    result = "Armstrong Number"
else:
    result = "Not an Armstrong Number"

conn.send(result.encode())

conn.close()
s.close()
