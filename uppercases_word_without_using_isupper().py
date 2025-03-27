# Get user input
text = input("Enter text: ")

# Convert to lowercase manually
result = ""
for letter in text:
    if 'a' <= letter <= 'z':  # If lowercase
        result += chr(ord(letter) - 32)  # Convert to uppercase
    else:
        result += letter  # Keep as is

# Print result
print("Uppercase text:", result)