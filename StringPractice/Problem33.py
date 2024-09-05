#Write a  Python program to print the following integers with zeros to the left of the specified width.

number = 77

desired_width = 5

print(f"Formated number :{str(number).zfill(desired_width)}")
print(f"Formated number :{str(number).rjust(desired_width,'0')}")
