def reverse_str(str):
     if(len(str)%4==0):
          return str[len(str)::-1]
     
print(reverse_str("sister"))
print(reverse_str("Mathematics!"))