f= open("file1.txt")
print(f.read())
f.close()

#The same can be written using with statement like this:
with open("file.txt") as f:
     print(f.read())

#you does not need to close the file or you dont have to explicitly close the file