import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 8080))

print("Prime Number Server Started...")

data, addr = s.recvfrom(1024)

num = int(data.decode())

if num <= 1:
    result = "Not Prime"

else:
    result = "Prime"

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result = "Not Prime"
            break

s.sendto(result.encode(), addr)

print("Result:", result)

s.close()
