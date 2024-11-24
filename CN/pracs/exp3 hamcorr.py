a='1110101'

def iseven(a):
    if(int(a)%2==0):
        return '0'
    return '1'

sum1=int(a[6])+int(a[4])+int(a[2])+int(a[0])
sum2=int(a[6])+int(a[5])+int(a[2])+int(a[1])
sum3=int(a[3])+int(a[2])+int(a[1])+int(a[0])

e1=iseven(sum1)
e2=iseven(sum2)
e3=iseven(sum3)

ans=e3+e2+e1
print(ans)

final=int(ans,2)

print("Error at pos", final)

b=[]
if a[7-final]==1:
    b[7-final]=0
else:
    b[7-final]=1

for i in a:
    b.append(i)



print(b)