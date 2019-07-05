let_list=['a','e','i','o','u']
let_list1=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
letter=str(input())
if (letter in let_list):
    print("Vowel")
elif(letter in let_list1):
  print("Consonant")
else:
 	print("invalid")
