def max_num(n1,n2,n3):
	if(n1>=n2)and (n1>=n3):
		max=n1
	elif(n2>=n1)and(n2>=n3):
		max=n2
	elif(n3>=n1)and(n3>=n2): 
		max=n3
	return max
n1=int(input())
n2=int(input())
n3=int(input())
print(max_num(n1,n2,n3))

