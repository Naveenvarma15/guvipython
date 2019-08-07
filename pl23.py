
m,n=input().split()
m=list(map(int,input().split()))
n=list(map(int,input().split()))
for i in n:
    m.append(i)
    print(max(m),end=' ')
    continue
