#Write a  Python program to print the following integers with '*' to the right of the specified width

number = 77

desired_width = 5

print(f"Formated number :{str(number).ljust(desired_width,'*')}")