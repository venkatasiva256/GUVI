word=str(input())
a=len(word)
b=[]
for i in range(0,a,3):
  b=word[i]
if(a==1):
  print(word[0])
else:
  print(word[0]+b)
