#naveen
n=input()
m=[]
for i in n:
    if i.isnumeric():
        m.append(i)
print(''.join(m))
