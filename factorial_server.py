import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 12345))

print("Factorial Server Started")

data, addr = s.recvfrom(1024)

num = int(data.decode())

if num < 0:

    result = "Factorial Not Possible"

else:

    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    result = str(fact)

s.sendto(result.encode(), addr)

s.close()
