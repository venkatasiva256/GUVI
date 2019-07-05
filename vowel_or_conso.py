vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
letter=str(input())
if (letter in vowels):
    print("Vowel")
elif(letter in consonants):
  print("Consonant")
else:
 	print("invalid")
