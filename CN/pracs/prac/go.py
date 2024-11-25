total=10
ack=0
win=4
sent=0
import time
import random
while(ack<total):
    for i in range(win):
        if sent<total:
            print("Sending frame ",sent)
            sent+=1
            time.sleep(1)
        
    for i in range(win):
        ackn=random.choice([True,False])
        if ackn:
            print("Recd ackn for frame ",ack)
            ack+=1
        else:
            print("Ackn lost , resending from here", ack)
            sent=ack
            break