#naveen
n=list(map(int,input().split()))
m=list(map(int,input().split()))
o=list(map(int,input().split()))
if n[0]==m[0] and n[0]==o[0]:
    print("yes")
elif n[1]==m[1] and n[1]==o[1]:
    print("yes")
elif n[0]==n[1] and m[0]==m[1] and o[0]==o[1]:
    print("yes")
else:
    print("no")
