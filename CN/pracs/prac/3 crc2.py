def crc(data,divisor):
    n=len(divisor)
    temp=data+'0'*(n-1)
    temp=list(temp)
    divisor=list(divisor)
    for i in range(len(data)):
        if temp[i]=='1':
            for j in range(n):
                temp[i+j]=str(int(temp[i+j])^int(divisor[j]))
    rem=''.join(temp[-(n-1):])
    return rem

def crc2(data,divisor):
    n=len(divisor)
    temp=list(data)
    divisor=list(divisor)
    for i in range(len(data)):
        if temp[i]=='1':
            for j in range(n):
                temp[i+j]=str(int(temp[i+j])^int(divisor[j]))
    rem=''.join(temp[-(n-1):])
    return rem

a=input("Enter data: ")
b=input("Enter divsor: ")
c=crc(a,b)

d=a+c
print(d)

e=input("Enter recieved data: ")
f=crc2(e,b)

if(int(f)==0):
    print("Correct")
else:
    print("Wrong")