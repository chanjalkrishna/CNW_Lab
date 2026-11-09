import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ('127.0.0.1', 12345)

num = input("Enter a Number: ")

s.sendto(num.encode(), server)

data, addr = s.recvfrom(1024)

print("Factorial:", data.decode())

s.close()
