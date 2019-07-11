m,n=map(int,input().split())
p=[]
for i in range (m,n+1):
    j = 1;
    while j*j <= i:
        if j*j == i:
                p.append(i)  
        j = j+1
    i = i+1
print(len(p))
