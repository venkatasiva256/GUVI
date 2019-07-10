N,Q=map(int,input().split())
g=0
for i in range(1,Q+1):
  if(N%i==0)and(Q%i==0):
    g=i
print(g)
