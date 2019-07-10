w,k=map(int,input().split())
for i in range(w):
  if(k**i==w):
    print("yes")
    break
else:
    print("no")
