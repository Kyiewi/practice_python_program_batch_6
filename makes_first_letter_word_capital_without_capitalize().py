# Ask user for input
string = input("Enter a word: ")

# Check if the string is not empty
if len(string) > 0:
    # Manually capitalize the first letter
    first_letter = string[0]
    if 'a' <= first_letter <= 'z':  # Check if it's lowercase
        first_letter = chr(ord(first_letter) - 32)  # Convert to uppercase

    # Initialize an empty string for the rest of the characters
    rest_of_string = ""

    # Convert the rest of the string to lowercase manually
    for char in string[1:]:
        if 'A' <= char <= 'Z':  # Check if it's uppercase
            # Convert to lowercase
            new_char = chr(ord(char) + 32)
        else:
            # Keep the character as is (already lowercase or non-alphabetical)
            new_char = char
        rest_of_string = rest_of_string + new_char  # Add to the result string

    # Combine the capitalized first letter with the rest of the string
    capitalized_string = first_letter + rest_of_string
else:
    # If the string is empty, just return it as is
    capitalized_string = string

# Print the result
print("Capitalized string:", capitalized_string)
