a=int(input())
b=map(int,input().split())
b = list(b)
for i in range(a):
  for j in range(i+1,a):
    if(b[i]+b[j]==0):
      print(b[i],b[j])
      break
