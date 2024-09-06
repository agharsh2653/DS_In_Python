#43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder

area = 1256.66
volume = 1254.725

# Define the number of decimals for formatting.
decimals = 2

# Print the area of the rectangle with formatting and the specified number of decimals.
print(f"The area of the rectangle is {area:.{decimals}f}cm²")

# Update the number of decimals for formatting.
decimals = 3

# Print the volume of the cylinder with formatting and the specified number of decimals.
print(f"The volume of the cylinder is {volume:.{decimals}f}cm³")