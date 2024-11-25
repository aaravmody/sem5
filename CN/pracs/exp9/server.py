import time
import socket

HOST='127.0.0.1'
PORT=5000

cl=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cl.bind((HOST,PORT))
cl.listen()

print("Server is listening on port",PORT)
conn,add=cl.accept()

def ack(conn):
    while True:
        data=conn.recv(1024)
        if not data:
            break

        msg=data.decode()
        time.sleep(1)
        print("data recd is ", msg)
        if msg=='end':
            break
        ack='sending ack of recd data'
        conn.sendall(ack.encode())

    conn.close()

ack(conn)
cl.close()