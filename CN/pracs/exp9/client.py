import time
import socket

HOST='127.0.0.1'
PORT=5000

cl=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cl.connect((HOST,PORT))

while True:
    msg=input("Enter data ")
    cl.sendall(msg.encode())
    if msg=='end':
        break
    data=cl.recv(1024)
    time.sleep(1)
    print(data.decode())

print("End connetion")
cl.close()