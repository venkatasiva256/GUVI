a=int(input())
b=map(int,input().split())
b = list(b)
for i in range(a):
  for j in range(i+1,a):
    k = b[i]+b[j]
    if k in b:
      print(b[i],b[j],k)
