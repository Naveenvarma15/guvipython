#naveen
n=int(input())
z=[]
s=0
for i in range(n):
    z.append(input())
for i in range(n):
    if sorted(z[i])==sorted('kabali'):
        s+=1
print(s)
