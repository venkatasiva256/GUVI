m=int(input())
n=list(map(int,input().split()))
c=max(n)
d,e=0,0
for i in range(0,len(n)-1):
  for j in range(i+1,len(n)):
    if abs(n[i]+n[j])<c:
      d,e=n[i],n[j]
      c=abs(d+e)
print(d,e)
