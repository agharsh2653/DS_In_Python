word = input("Enter the word: ")
li = word.split(" ")
s= ""
print(type(li))
for i in range(len(li)-1,-1,-1):
     s = s+li[i]+" "

print(s)

word1= word[::-1]
print(word1)
l2 = word1.split(" ")
s2=""

for i in range(len(l2)-1,-1,-1):
     s2 = s2+l2[i]+" "

print(s2)