import socket

ip = "10.33.22.23"
port = 4000
bufferSize = 20


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(1)

conn, addr = s.accept()
print("connection Adress: ", addr)
while 1:
    data = conn.recv(bufferSize)
    if not data: break
    print("Recieved Data: ", data)
    conn.send(data)
conn.close()
