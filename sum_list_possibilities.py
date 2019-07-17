a=int(input())
b=map(int,input().split())
b = list(b)
for i in range(a):
  for j in range(i+1,a):
    for k in range(j+1,a):
      if(b[i]+b[j]==b[k]):
        print(b[i],b[j],b[k])
