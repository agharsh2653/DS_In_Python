name = input("Enter your name ")
print("Good Evening ",name)
print(f"Good Evening {name}")

# problem 2nd
letter  = '''Dear <|Name|>
you are selected!
 <|Date|>'''

print(letter.replace("<|Name|>","Harsh").replace("<|Date|>","12 July 2025"))

#program to detect double space in string
word = "Harsh  is a  hardworking person"

#name is does not change because string is immutable 

# it will detect first occur space
print(word.find("  "))
print(word.replace("  "," "))
