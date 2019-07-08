number=int(input())
check=0
for i in range(0,number):
  if(2**i==number):
    check=1
if(check==1):
   print("yes")
else:
  print("no")
