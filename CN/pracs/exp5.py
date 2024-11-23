i=input('ip address: ')
ip=i.split('.')

a=int(ip[0])
print(a)

if(a>0 and a<127):
    print("class a")
    print(ip[0]+'0.0.0')

elif(a>=127 and a<192):
    print("class b")
    print(ip[0]+'.'+ip[1]+'.0.0')

elif(a>=192 and a<224):
    print("class c")
    print(ip[0]+'.'+ip[1]+'.'+ip[2]+'.0')

elif(a>=224 and a<239):
    print("class d")

elif(a>=239 and a<256):
    print("class e")
