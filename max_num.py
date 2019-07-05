n_1,n_2,n_3=map(int,input().split())
if(n_1>=n_2)and (n_1>=n_3):
	max=n_1
elif(n_2>=n_1)and(n_2>=n_3):
	max=n_2
else: 
	max=n_3
print(max)
