import socket
import datetime

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server address
s.bind(('127.0.0.1', 8080))

print("Time Server Started...")

# Handle multiple client requests
while True:

    data, addr = s.recvfrom(1024)

    # Get current date and time
    current_time = datetime.datetime.now()

    result = current_time.strftime("%d-%m-%Y %H:%M:%S")

    print("Request received from:", addr)
    print("Sending time:", result)

    # Send time to client
    s.sendto(result.encode(), addr)
