total=10
ack=[False]*total
win=4
sent=0
wait=[]
import time
import random
while False in ack:
    while sent<total and len(wait)<win:
        print("Sending frame ",sent)
        wait.append(sent)
        sent+=1
        time.sleep(1)
        
    for i in wait:
        ackn=random.choice([True,False])
        if ackn:
            print("Recd ackn for frame ",i)
            ack[i]=True
            wait.remove(i)
        else:
            print("Ackn lost , resending", i)
            time.sleep(1)