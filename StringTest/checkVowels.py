#WAPP to check vowels and consonant in any string input by user
import re

def findVowels(string):
    vowels = re.findall(r'[aeiouAEIOU]', string)
    return len(vowels), vowels

user_input = input("Enter a string: ")
count, vowels_list = findVowels(user_input)
print(f"Number of vowels: {count}")
print(f"Vowels: {', '.join(vowels_list)}")
