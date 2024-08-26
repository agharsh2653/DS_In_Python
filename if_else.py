age = int(input("Enter your age"))

if(age<=18):
    print("you are above the age of consent")
    print("Good for you")
elif(age<0):
    print("you are entering the invalid negative age")
else:
    print("you are below the age of consent")