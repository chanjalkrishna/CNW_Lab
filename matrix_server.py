import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(1)

print("Server waiting...")

conn, addr = s.accept()

data = conn.recv(4096).decode()

values = list(map(int, data.split()))

n = values[0]
matrix = []

k = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(values[k])
        k += 1
    matrix.append(row)

upper = True
lower = True
diagonal = True

for i in range(n):
    for j in range(n):

        if i > j and matrix[i][j] != 0:
            upper = False

        if i < j and matrix[i][j] != 0:
            lower = False

        if i != j and matrix[i][j] != 0:
            diagonal = False

if diagonal:
    result = "Diagonal Matrix"
elif upper:
    result = "Upper Triangular Matrix"
elif lower:
    result = "Lower Triangular Matrix"
else:
    result = "Neither"

print("Result:", result)

conn.send(result.encode())

conn.close()
s.close()
