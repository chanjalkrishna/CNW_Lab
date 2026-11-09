import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ('127.0.0.1', 12345)

string = input("Enter a String: ")

s.sendto(string.encode(), server)

data, addr = s.recvfrom(1024)

print("String Without Duplicates:", data.decode())

s.close()
