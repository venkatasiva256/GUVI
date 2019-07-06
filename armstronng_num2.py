number=int(input())
c=0
s=number
while s>0:
    d=s%10
    cube=d*d*d
    c=c+cube
    s//=10
if(number==c):
    print("yes")
else:
    print("no")
