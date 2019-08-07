#naveen
n,m=list(map(int,input().split()))
li=[]
li1=[]
for i in range(1,11):
    if n%i==0:
        li.append(i)
        o=max(li)
for i in range(1,11):
    if m%i==0:
      li1.append(i)
      p=max(li1)
print(o,end='')
