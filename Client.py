import socket

ip = "10.33.22.23"
port = 4000
bufferSize = 1024
message = "Hello World"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send(bytes(message, "utf-8"))
data = s.recv(bufferSize)
s.close()

print("received data:", data)