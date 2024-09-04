#Write a  Python program to print the following numbers up to 2 decimal places with a sign.

x=4.78345
print(f"Original value of X is {x}")

print("Formated value of X is "+"{:+.2f}".format(x))

y=-7.454342
print(f"Original value of Y is {y}")

print("Formated value of Y is "+"{:+.2f}".format(y))

def print_signed_numbers(numbers):
    for num in numbers:
        formatted_num = f"{num:+.2f}"
        print(f"Formated Number :{formatted_num}")

# Example usage:
numbers_to_print = [3.14159, -2.71828, 0.12345]
print_signed_numbers(numbers_to_print)

