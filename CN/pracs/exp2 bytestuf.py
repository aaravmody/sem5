a=input("Enter message: ")
s=input("Start: ")
e=input("End: ")
esc=input("Escape: ")
b=''

ans=''
for i in a:
    if(i==s or i==e):
        b+=esc
    b+=i

ans=s+b+e
print(ans)