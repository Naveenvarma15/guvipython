x,y,z=input().split()
max(x,y,z)
if(int((x>=y) and (x>=z))):
    print(x)
elif(int((y>=x) and (y>=z))):
    print(y)
else:
    print(z)
