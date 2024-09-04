str = input("Enter the string: ")
if(str[0]>='A' and str[0]<='Z'):
     print("Starting character is in upercase")
elif(str[0]>='a' and str[0]<='z'):
     print("Starting character is in lowercase")
elif(str[0]>='0' and str[0]<='9'):
     print("starting character is a number")
else:
     print("Starting character is specific character")

string = "w3resource.com"
print(string.startswith("w3r"))