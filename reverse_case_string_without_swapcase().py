# Ask user for input
string = input("Enter a word: ")

# Swap case manually
swapped_string = ""
for char in string:
    if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
        swapped_string += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
        swapped_string += chr(ord(char) + 32)
    else:
        swapped_string += char  # Keep non-alphabet characters as is

# Print the result
print("Swapped case:", swapped_string)
