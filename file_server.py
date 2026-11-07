import socket
import os

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server address
s.bind(('127.0.0.1', 8080))

print("File Server Started...")

# Handle multiple client requests
while True:

    # Receive filename
    data, addr = s.recvfrom(1024)

    filename = data.decode()

    print("Requested file:", filename)

    # Check whether file exists
    if os.path.exists(filename):

        # Read file contents
        f = open(filename, "rb")
        content = f.read()
        f.close()

        # Send file to client
        s.sendto(b"OK" + content, addr)

        print("File sent successfully")

    else:
        s.sendto(b"ERROR: File not found", addr)

        print("File not found")
