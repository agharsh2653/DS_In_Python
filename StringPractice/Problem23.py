str = "Welcome to the harsh app developer website\n          "

#using strip() to delte all the spaces and defines symbol
print ( str.strip() ) 
  
# using lstrip() to delete all trailing ' ' end spaces or defines symbol

print ( str.lstrip() ) 
  
# using rstrip() to delete all leading ' ' start spaces or defined symbol 

print ( str.rstrip() ) 

#problem sort the string in lexi
def lexicographic_sort(s):
     return sorted(sorted(s), key=len)


print(lexicographic_sort("w3resource"))
print(lexicographic_sort("quickburn"))