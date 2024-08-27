#Make a python program to prime number from 100 to 200
def primeNum(num):
     flag=False
     for i in range(2,num):
          if(num%i==0):
               flag = True
     
     if(flag==False):
          return True
     else:
          return False
     
for i in range(100,200):
     if(primeNum(i)):
          print(i)