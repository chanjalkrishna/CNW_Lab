import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server = ('127.0.0.1', 8080)

# Send request
message = "Give me current date and time"

s.sendto(message.encode(), server)

# Receive time from server
data, addr = s.recvfrom(1024)

print("Current Date and Time:", data.decode())

s.close()
