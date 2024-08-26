d = {} #empty dictionary
marks = {
     "harry":"code",
     "harsh":84,
     "keshav":56,
     "list":[1,3,5],
     0:"zero"
}
#print((marks),type(marks))
print(marks["harry"])

#Dictionary methods
#print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"harry":99,"Anushka":78})
print(marks.items())

# print(marks.get("harry2")) # Print None
# print(marks["harry2"]) #Print an error

#new_dict = marks.copy() #Return a shallow copy of a dict
keys = ['a','b','c']
new_dict = dict.fromkeys(keys,0)
print(new_dict)

value = new_dict.pop('c','default_value') #if key is exits it return value and pop it otherwise it return provided default value
print(value)
item = marks.popitem()
print(item)

marks.clear() #clear the data 
new_dict.clear()
