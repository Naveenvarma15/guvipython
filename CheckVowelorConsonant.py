n = input()
if n.isalpha() == True:
    if(n=='A' or n=='a' or n=='E' or  n=='e' or n=='I'or n=='i' or n=='O' or n=='o' or n=='U' or n=='u'):
         print("Vowel")
    else:
         print("Consonant")
else:
    print("invalid")
