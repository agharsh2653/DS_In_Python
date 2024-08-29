num = int(input("Enter the number: "))
sum=0
while(num!=0):
     rem = num%10
     sum += rem
     num //= 10

print(sum)