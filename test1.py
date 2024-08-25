

def prime(num):
     temp=0
     
     for i in range(2,num//2):
          if(num%i==0):
               temp+=1
               break

     if(temp==0 and num!=-1):
          return True
     else:
          return False
         
          
for i in range(50,150):
     if(prime(i)):
          print(i)     


