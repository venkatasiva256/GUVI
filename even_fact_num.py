number=int(input())
box=[]
for i in range(2,number+1,2):
  if(number%i==0):
    box=i
    print(box,end=" ")
