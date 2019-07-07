word1=input()
for i in word1:
    if i.islower():
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")
