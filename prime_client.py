import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ('127.0.0.1', 8080)

num = int(input("Enter a number: "))

s.sendto(str(num).encode(), server)

result, addr = s.recvfrom(1024)

print("Server Response:", result.decode())

s.close()
