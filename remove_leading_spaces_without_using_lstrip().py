# Ask user for input with leading spaces
custom_lstrip = input("Enter Full Name with leading spaces: ")

# Find first non-space character
for char in range(len(custom_lstrip)):
    if custom_lstrip[char] != " ":
        # Print name without leading spaces
        print(custom_lstrip[char:])
        # Stop loop
        break