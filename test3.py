
def factorial(num):
     fact=1
     for i in range(2,num+1):
          fact = fact*i
     return fact 

def strongNum(num):
     strong=0
     n=num
     while(n!=0):
          rem=n%10
          strong+= factorial(rem)
          n//=10
     
     if(num==strong):
          return True
     else:
          return False



def perfectNum(num):
     perfact=0
     for i in range(1,num):
          if(num%i==0):
               perfact +=i
     
     if(perfact==num):
          return True
     else:
          return False

num = int(input("Enter the number: "))
if(strongNum(num)==True and perfectNum(num)==False):
     print(f"Strong number is {num}")
elif(strongNum(num)==True and perfectNum(num)==True):
     print(f"{num} is a strong and perfect number both")
elif(strongNum(num)==False and perfectNum(num)==True):
     print(f"Perfect number is {num}")
else:
     print(f"{num} is not a Strong number and perfect number ")
     

          
