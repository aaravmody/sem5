a=input("Enter data to be sent")
count=0
r=''
for i in a:
    if(i=='1'):
        count+=1
    else:
        count=0
    r+=i
    if(count==5):
        r+='0'
        count=0
    
    

print(r)
