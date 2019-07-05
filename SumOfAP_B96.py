#naveen
n,m,o=list(map(int,input().split()))
s=0
for i in range(0,o):
    s=s+n
    n=n+m
print(s)
