n=int(input())
a=list(map(int,input().split()))
num=[]
for i in a:
    if a.count(i)>1:
        if str(i) not in num:
            num.append(str(i))
if len(num)==0:
    print("unique")
else:
    print(" ".join(num))
