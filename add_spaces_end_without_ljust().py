# Ask user for input
string = input("Enter a word: ")
width = int(input("Enter total width: "))

# Add spaces only if needed
if len(string) < width:
    string += " " * (width - len(string))

# Print the result
print("Padded string:", f'"{string}"')
