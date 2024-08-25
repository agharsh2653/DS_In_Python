num = int(input("Enter the number: "))
sum=int(input("Enter the number of series: "))
n=sum
print(sum,end="+")
for i in range(1,num):

     sum+=(10**i)*n
     print(sum,end="+")