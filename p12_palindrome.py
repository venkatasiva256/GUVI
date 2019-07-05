num=input()
if len(num)==4:
  if (num[0]==num[3])and(num[1]==num[2]):
    print("yes")
  else:
    print("no")
elif len(num)==3:
  if (num[0]==num[2]):
   print("yes")
  else:
   print("no")
