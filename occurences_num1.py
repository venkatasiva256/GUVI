N1,K1=map(str,input().split())
N=list(N1)
count=0
for i in range(0,len(N)):
    if(K1==N[i]):
        count=count+1
print(count)
