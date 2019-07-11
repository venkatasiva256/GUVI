m,n=map(str,input().split())
r=len(m)
p=0
for i in range(r):
    if(m[i]!=n[i]):
        p=p+1
if(p==1):
    print("yes")
else:
    print("no")
