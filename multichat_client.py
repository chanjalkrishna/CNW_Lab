import socket
import threading

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect(('127.0.0.1', 8080))

print("Connected to Chat Server")
print("Type 'exit' to leave")

# Function to receive messages
def receive():
    while True:
        try:
            msg = s.recv(1024).decode()

            if not msg:
                break

            print("\nOther:", msg)

        except:
            break

# Create receiving thread
thread = threading.Thread(target=receive)
thread.start()

# Send messages
while True:
    msg = input("You: ")

    if msg.lower() == "exit":
        break

    s.sendall(msg.encode())

# Close socket
s.close()
