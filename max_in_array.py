n,k=map(int,input().split())
e=input()
n1=list(map(int,input().split()))
k1=list(map(int,input().split()))
for i in k1:
  n1.append(i)
  print(max(n1),end=" ")
