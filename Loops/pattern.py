num = int(input("Enter the number: "))

for i in range(0,num):
    print(" "*(num-i),end="")
    print("*"*(2*i+1),end="")
    print()

for i in range(0,num):
     print("*"*(i+1))

for i in range(1,num+1):
     if(i==1 or i==num):
          print("*"*num,end="")
     else:
          print("*",end="")
          print(" "*(num-2),end="")
          print("*",end="")
     print()


for i in range(1,num+1):
     for j in range(1,i+1):
          print(j,end="")
     print()

for i in range(0,num):
     for j in range(num-i,0,-1):
          print(j,end="")
     print()