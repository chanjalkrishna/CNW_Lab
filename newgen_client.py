import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server = ('127.0.0.1', 8080)

# Get sentence from user
sentence = input("Enter New Generation English: ")

# Send sentence to server
s.sendto(sentence.encode(), server)

# Receive translated sentence
data, addr = s.recvfrom(1024)

print("Formal English:", data.decode())

s.close()
