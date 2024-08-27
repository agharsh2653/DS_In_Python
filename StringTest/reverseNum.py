#WAPP to print reverse of a number
num = int(input("Enter the number: "))

sum=0
while num!=0:
     rem=num%10
     sum=sum*10+rem
     num//=10

print("Reverse of a number: ",sum)
