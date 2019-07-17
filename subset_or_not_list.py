m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
	if i in a:
		print("yes")
		break
	else:
		print("no")
		break
