m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
	if i in a:
		print("YES")
		break
	else:
		print("NO")
		break
