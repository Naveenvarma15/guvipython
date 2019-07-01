#naveen
n=str(input())
m=len(n)
a=0
b=0
for i in range(0,m):
    if n[i].isalpha():
        a=a+1
    if n[i].isnumeric():
        b=b+1
if a==0 or b==0:
    print("N0")
else:
    print("Yes")
