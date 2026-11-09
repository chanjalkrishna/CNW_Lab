import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8080))

s.listen(1)

print("Fibonacci Server Started")

conn, addr = s.accept()

data = conn.recv(1024).decode()

n = int(data)

a = 0
b = 1

result = ""

for i in range(n):

    result = result + str(a) + " "

    c = a + b

    a = b
    b = c

conn.send(result.encode())

conn.close()
s.close()
