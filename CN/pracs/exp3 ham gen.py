# EVEN PARITY
d1=input("Enter D1: ")
d2=input("Enter D2: ")
d3=input("Enter D3: ")
d5=input("Enter D5: ")
p7=''
p6=''
p4=''

a=int(d1)+int(d3)+int(d5)
if(a%2==0):
    p7='0'
else:
    p7='1'

b=int(d2)+int(d3)+int(p7)
if(b%2==0):
    p6='0'
else:
    p6='1'

c=int(d5)+int(p6)+int(p7)
if(c%2==0):
    p4='0'
else:
    p4='1'

ans=''
ans=p7+p6+d5+p4+d3+d2+d1
print(ans)


