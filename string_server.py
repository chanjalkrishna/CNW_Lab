import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(1)

print("Server Started")

conn, addr = s.accept()

data = conn.recv(1024).decode()

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in data:

    if ch.lower() in "aeiou":
        vowels = vowels + 1

    elif ch.isalpha():
        consonants = consonants + 1

    elif ch.isdigit():
        digits = digits + 1

    elif ch == " ":
        spaces = spaces + 1

result = str(vowels) + "," + str(consonants)
result = result + "," + str(digits) + "," + str(spaces)

conn.send(result.encode())

conn.close()
s.close()
