start,end=input().split()
start=int(start)
end=int(end)
for i in range(start,end):
    s=0
    c=i
    while (i!=0):
        d=i%10
        s=s+d*d*d
        i=i//10
    if(c==s):
        print(c, end=" ")
