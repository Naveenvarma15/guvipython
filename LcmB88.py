#naveen
import math
n=list(map(int,input().split()))
for i in n:
    print(int((n[0]*n[1])/math.gcd(n[0],n[1])))
    break
