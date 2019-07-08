number=int(input())
che=0
for i in range(0,number):
  if(2**i==number):
    che=1
if(che==1):
   print("yes")
else:
  print("no")
