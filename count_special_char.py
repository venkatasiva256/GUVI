n=input()
p=0
for i in range (len(n)):
  if (n[i].isdigit()or n[i].isalpha()or n[i]==' '):
    continue
  else:
    p=p+1
print(p)
