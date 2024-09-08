#51. Write a  Python program to find the first non-repeating character in a given string.

str = "ababa"
dt = {}
for char in str:
     dt.update({char:0})
count=0
for key,value in dt.items():
     for i in str:
          if(i==key):
               value+=1
               dt.update({key:value})

flag=False
for ch in dt:
     if dt[ch]==1:
          print(ch)
          falg =True
          break

if flag == False:
     print("None") 
     