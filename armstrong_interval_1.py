n1,n2=map(int,input().split())
for n in range(n1,n2):
    s=0
    temp=n
    while temp>0:
        d=temp%10
        c=d*d*d
        s=s+c
        temp//=10
    if(n==s):
        print(n,end=" ")
