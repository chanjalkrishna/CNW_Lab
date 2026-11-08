import socket
import os
import signal

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9000))

# Automatically handle completed child processes
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("UDP File Server Started...")
print("Listening on port 9000")

try:
    while True:

        data, addr = s.recvfrom(1024)

        filename = data.decode()

        pid = os.fork()

        if pid == 0:

            child_pid = os.getpid()

            if os.path.isfile(filename):

                with open(filename, 'r') as f:
                    content = f.read()

                result = "Handled by Server PID: " + str(child_pid)
                result = result + "\n\n" + content

            else:
                result = "Handled by Server PID: " + str(child_pid)
                result = result + "\nFile Not Found"

            s.sendto(result.encode(), addr)

            s.close()
            os._exit(0)

        else:
            print("Request:", filename, "served by child PID:", pid)

except KeyboardInterrupt:
    print("\nServer Stopped")

finally:
    s.close()
