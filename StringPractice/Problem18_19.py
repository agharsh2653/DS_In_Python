def first_three(word):
     return word[0:3]

word = input("Enter the word: ") #ipy output ipy
if(len(word)>3):                 #python output pyt
     print(first_three(word))
else:
     print(word)

print(f"https://www.w3resource.com/{word}")