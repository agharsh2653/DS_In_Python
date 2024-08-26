word = input("Enter the name: ")

for i in range( len(word)-1,-1,-1):
     print(word[i])
     #Tkinter

for i in word:
     print(i,end="")

print(word[::-1]) 

print(word[len(word):2:-1])

a="pedestal Training"
print(a.replace("e","r"))
print(a.count("e"))
print(a.upper())
print(a.lower())
print(a.islower())
print(a.isupper())
# isupper() to check the string in uper case
# islower() to check the string in lower case 

print(a.split(" "),type(a.split(" ")))
s1 = " ".join(a)
print(s1,len(s1))
print(a.find("e")) #if doest not trace the value it will return -1
print(a.index("e"))

olleh dlrow
dlorlw olleh