def center_string(string):
    width = 20  # Set the fixed width to 20
    total_spaces = width - len(string)
    if total_spaces <= 0:
        return string
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return ' ' * left_spaces + string + ' ' * right_spaces

# Get user input
input_string = input("Enter a string: ")

# Print the centered string
print(f"'{center_string(input_string)}'")
