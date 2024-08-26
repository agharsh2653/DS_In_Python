#p1
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
# d = int(input("Enter number 4: "))

# if(a>b and a>c and a>d):
#      print(f"{a} is greater number") 
# elif(b>a and b>c and b>d):
#      print(f"{b} is greater number")
# elif(c>a and c>b and c>d):
#      print(f"{c} is greater number")
# else:
#      print(f"{d} is greater number")

#p3
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "Subscribe this"
# p4 = "click this"

# message = input("Enter your comment: ")
# if((message in p1)  or (message in p2) or (message in p3) or (message in p4)):
#      print("This comment is spam")
# else:
#      print("This comment is not a spam")     
 
#p4
# username = input("Enter username: ")
# if(len(username)<10):
#      print("your username contains less then 10 characters")
# else:
#      print("All is well!")

#p6
# marks = int(input("Enter your marks : "))
# if(marks<=100 and marks >=90):
#      grade = "Ex"
# elif(marks<90 and marks>=80):
#      grade = "A"
# elif(marks<80 and marks>=70):
#      grade = "B"
# elif(marks<70 and marks>=60):
#      grade = "C"
# elif(marks<60 and marks>=50):
#      grade = "D"
# else:
#      grade = "F"

# print("Your Grade is : ",grade)

#p7
post = input("Enter the post: ")
if("Harsh".lower() in post.lower()):
     print("This post is talking about you")
else:
     print("Ille not you")