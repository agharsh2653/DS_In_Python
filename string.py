str1="harsh"
print(len(str1))
str2="agrawal"
print(len(str1))
final_str=str1+str2
print(final_str)
print(final_str[1:5])
print(final_str[-7:])
print(final_str[-4:-1])
print(str1.endswith("sh"))
print(str2.capitalize())
print(str1.replace("har","an"))
print(str2.find("w"))

#slicing with space value
print(final_str[1:5:2])

#escape sequence 
print("Hello, harsh is a good boy\nbut not a bad \"boy\"")