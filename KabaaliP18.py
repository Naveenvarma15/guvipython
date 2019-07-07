#naveen
n=int(input())
m=[]
s=0
for i in range(n):
    m.append(input())
for i in range(n):
    if sorted(m[i])==sorted('kabali'):
        s=s+1
print(s)
