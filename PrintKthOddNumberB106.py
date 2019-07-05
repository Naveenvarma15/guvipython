#naveen
n,m=map(int,input().split())
o=input().split()
p=[]
for i in o:
    if int(i)%2!=0:
        p.append(i)
print(p[m-1])
