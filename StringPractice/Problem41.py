#Write a  Python program to strip a set of characters from a string.
import re
def remove_chars(input_string, chars_to_remove):
    print(f"[{re.escape(chars_to_remove)}]")
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string

original_string = "Hello!@# World$"
chars_to_remove = "!@#$"
result = remove_chars(original_string, chars_to_remove)
print("Result:", result)

