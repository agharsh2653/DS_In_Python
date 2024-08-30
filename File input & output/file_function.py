
f = open("file1.txt")
# lines = f.readlines()
# print(lines,type(lines))

# line = f.readline()
# print(line,type(line))

# line = f.readline()
# print(line,type(line))

# line = f.readline()
# print(line,type(line))

line = f.readline()
while(line!=""):
     print(line)
     line = f.readline()
     
f.close()