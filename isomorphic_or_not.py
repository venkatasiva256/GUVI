m,n=map(str,input().split())
if(len(m)!=len(n)):
    print("no")
else :
    p1=[m.count(i) for i in m]
    p2=[n.count(i) for i in n]
if(p1==p2):
    print("yes")
else:
    print("no")
