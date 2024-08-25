

def armstrongNum(num):
     n = num
     sum=0
     while(n!=0):
          rem=n%10
          sum += rem**3
          n //= 10
     
     if(num==sum):
          return True
     else:
          return False


for i in range(1,1000):
     if(armstrongNum(i)):
          print(i)
         

