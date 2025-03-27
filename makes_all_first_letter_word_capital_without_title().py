# Ask user for input
string = input("Enter a sentence: ")

# Initialize an empty string to hold the result
title_case_string = ""

# Initialize a flag to indicate whether the current character is the first in a word
is_first_letter = True

# Loop through each character in the string
for char in string:
    # If the character is alphabetic and it's the first letter of a word
    if char.isalpha() and is_first_letter:
        # Capitalize the first letter
        title_case_string += char.upper()
        is_first_letter = False
    elif char.isalpha():
        # For subsequent letters, convert them to lowercase
        title_case_string += char.lower()
    else:
        # Non-alphabetic characters are added as is, and reset the flag for the next word
        title_case_string += char
        is_first_letter = True

# Print the result
print("Title case string:", title_case_string)
