#Write a Python program to reverse words in a string.

str = "welcome on abroad"
list_str = str.split()
new_str=""
for i in range(len(list_str)-1,-1,-1):
     new_str += list_str[i]+" "

print(new_str)