import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server address
s.bind(('127.0.0.1', 8080))

print("Translation Server Started...")

# Receive message from client
data, addr = s.recvfrom(1024)

sentence = data.decode()

print("Received:", sentence)

# Translation dictionary
dictionary = {
    "gonna": "going to",
    "wanna": "want to",
    "gotta": "have to",
    "lol": "laughing out loud",
    "btw": "by the way",
    "thx": "thank you",
    "pls": "please",
    "u": "you",
    "r": "are"
}

# Translate sentence
words = sentence.split()

translated = []

for word in words:
    translated.append(dictionary.get(word.lower(), word))

result = " ".join(translated)

print("Translated:", result)

# Send result to client
s.sendto(result.encode(), addr)

s.close()
