import time
import socket

HOST='127.0.0.1'
PORT=5000

cl=socket.socket()
cl.connect((HOST,PORT))

while True:
    msg=input("Enter data ")
    cl.sendall(msg.encode())
    data=cl.recv(1024)
    time.sleep(1)
    print(data.decode())
    if msg=='end':
        break

cl.close()