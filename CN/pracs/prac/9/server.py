import time
import socket

HOST='127.0.0.1'
PORT=5000

cl=socket.socket()
cl.bind((HOST,PORT))
cl.listen()

conn,addr=cl.accept()

while True:
    data=conn.recv(1024)
    time.sleep(1)
    print("Recv ",data.decode())
    ack="Sending ack"
    print(ack)
    conn.sendall(ack.encode())
    if data=='end':
        break

cl.close()