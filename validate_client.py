import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ('127.0.0.1', 8080)

student_id = input("Enter Student ID: ")

s.sendto(student_id.encode(), server)

result, addr = s.recvfrom(1024)

print("Server Response:")
print(result.decode())

s.close()
