#naveen
string=input()
num=0
for i in range(len(string)):
    if(string[i].isdigit()):
        num=num+1
if num==len(string):
    print("yes")
else:
    print("no")
