n=input()
n1=n.lstrip('-').replace('.','',1).isdigit()
if(n1==True):
  print("Yes")
else:
  print("No")
