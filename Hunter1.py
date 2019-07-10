#naveen
n=int(input())
n=list(map(int,input().split()))
m=[]
for i in n:
    if n.count(i)>1:
        if i not in m:
            m.append(i)
print(*m)
if len(m)==0:
    print("unique")
