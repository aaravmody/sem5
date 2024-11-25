a=input("Enter 9 bit string: ")

def iseven(a):
    if(a%2==0):
        return "0"
    return "1"

sum1=iseven(int(a[0])+int(a[2])+int(a[4])+int(a[6])+int(a[8]))
sum2=iseven(int(a[2])+int(a[3])+int(a[6])+int(a[7]))
sum3=iseven(int(a[2])+int(a[3])+int(a[4])+int(a[5]))
sum4=iseven(int(a[0])+int(a[1]))

fin=sum4+sum3+sum2+sum1
print(fin)
ans=int(fin,2)

if ans==0:
    print("No errors")

print("Error at ",ans)

b=[0]*9

for i in range(len(a)):
    b[i]=a[i]

if a[9-ans]=='1':
    b[9-ans]='0'
else:
    b[9-ans]='1'

print(b)

s=''

for i in b:
    s+=i

print(s)