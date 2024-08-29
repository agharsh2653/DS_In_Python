import random
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

flag=False
count=0
Total_count=10
num = random.randint(lower,upper)
while(count<Total_count):
     count += 1
     
     guess = int(input("Enter the number: ")) 
     print(guess)
     if(guess==num):
          print("Congratulations you did it in ",
              count, " try")
          flag=True
          break
     elif(guess < num):
        print("You guessed too small!")
     elif(guess > num):
        print("You Guessed too high!")

if(flag==False):
     print(f"The number is {num}")
     print("\tBetter Luck Next time!")
     
