import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 12345))

print("Duplicate Removal Server Started")

data, addr = s.recvfrom(1024)

string = data.decode()

result = ""

for ch in string:

    if ch not in result:
        result = result + ch

s.sendto(result.encode(), addr)

s.close()
