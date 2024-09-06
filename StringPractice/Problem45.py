#45. Write a  Python program to check whether a string contains all letters of the alphabet.
import string

alphabat = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >=alphabat)

input_string = 'The quick brown fox jumps over the lazy cat'

print(set(input_string.lower()) >=alphabat)
