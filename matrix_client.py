import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))

n = int(input("Enter order of matrix: "))

matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

# Convert matrix into a string
data = str(n) + " "

for row in matrix:
    for value in row:
        data += str(value) + " "

# Send matrix
s.send(data.encode())

# Receive result
result = s.recv(1024).decode()

print("Result:", result)

s.close()
