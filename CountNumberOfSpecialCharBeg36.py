string=input()
num=0
for i in range(len(string)):
    if(string[i].isdigit()!=True and string[i].isalpha()!=True):
        num=num+1
print(num)
