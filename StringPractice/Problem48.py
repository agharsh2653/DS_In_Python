#Write a Python program to swap commas and dots in a string.

def Replace(str1):
    str1 = str1.replace(', ', 'third')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('third', '.')
    return str1
     
string = "32.054,23"
print(Replace(string))
