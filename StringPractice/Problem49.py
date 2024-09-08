#49. Write a Python program to count and display vowels in text.

vowels = "aeiouAEIOU"
text = "w3resource"
count=0
list = []
for letter in text:
     if letter in vowels:
          count+=1
          list.append(letter)
print(count)
print(list)
