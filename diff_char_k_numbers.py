m,n,k=map(str,input().split())
k=int(k)
r=len(m)
p=0
for i in range(r):
    if(m[i]!=n[i]):
        p=p+1
if(p==k):
    print("yes")
else:
    print("no")
