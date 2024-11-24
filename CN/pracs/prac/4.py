import time
import random

total=10
window=4
sent=0
ack=0

while(ack<total):
    for i in range(window):
        if(sent<total):
            print("Sent",sent)
            sent+=1
            time.sleep(1)
    for i in range(window):
        ac=random.choice([True,False])
        if ac:
            print("Recd ", ack)
            ack+=1
        else:
            print("Didnt recieve ", ack)
            sent=ack
            break