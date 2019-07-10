#naveen
n=int(input())
o=list(map(int,input().split()))
m=[]
for i in o:
    if o.count(i)==1:
        if i not in m:
            m.append(i)
print(*m)
     
