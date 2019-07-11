N,Q=map(int,input().split())
p=[]
for i in range(N,Q+1):
  for j in range(2,i): 
    if(i%j==0):
      break
  else:
    p.append(i)
print(len(p))
