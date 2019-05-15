z=input()
try:
    x=int(z)
    if(x%2==0):
        print("even")
    else:
        print("odd")
except ValueError:
    print("invalid")
