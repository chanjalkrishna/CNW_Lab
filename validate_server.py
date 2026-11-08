import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 8080))

print("Student ID Server Started...")

data, addr = s.recvfrom(1024)

student_id = data.decode()

if student_id.startswith("MDL"):

    count = 0

    for ch in student_id:
        if ch.isalpha():
            count = count + 1

    result = "Valid ID"
    result = result + "\nNumber of Alphabets: " + str(count)

else:
    result = "Invalid Student ID"

s.sendto(result.encode(), addr)

print(result)

s.close()
