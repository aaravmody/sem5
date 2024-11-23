# character count
frame=int(input("Enter no. of frames:"))
final=''

for i in range(0,frame):
    data=input(f"Enter string {i+1}:")
    char_count=str(len(data)+1)+data
    final+=char_count


print(final)

