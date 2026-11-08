import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ('127.0.0.1', 9000)

filename = input("Enter file name: ")

s.sendto(filename.encode(), server)

data, addr = s.recvfrom(60000)

print("\nResponse Received From Server:")
print(data.decode())

s.close()
