a,d=map(int,input().split())
b,e=map(int,input().split())
c,f=map(int,input().split())
if(a==b==c):
    print("yes")
elif(d==e==f):
    print("yes")
elif(a==d and b==e and c==f):
    print("yes")
else:
    print("no")
