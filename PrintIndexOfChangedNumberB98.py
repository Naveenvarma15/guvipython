#naveen
n=int(input())
n=list(map(int,input().split()))
for i in range(0,len(n)-1):
    if n[i]>n[i+1]:
        print(i)
        break
