import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server = ('127.0.0.1', 8080)

# Enter filename
filename = input("Enter filename: ")

# Send filename to server
s.sendto(filename.encode(), server)

# Receive file contents
data, addr = s.recvfrom(60000)

# Check response
if data.startswith(b"OK"):

    content = data[2:].decode()

    print("\nFile Contents:")
    print(content)

else:
    print(data.decode())

s.close()
