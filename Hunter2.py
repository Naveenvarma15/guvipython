#naveen
n=int(input())
n=list(map(int,input().split()))
n.sort()
n.reverse()
if n[0]==0:
    print("0")
else:
    for i in n:
        print(i,end='')
