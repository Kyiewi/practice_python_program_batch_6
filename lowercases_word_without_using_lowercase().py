# Get user input
text = input("Enter text: ")

# Convert to lowercase manually
result = ""
for letter in text:
    if 'A' <= letter <= 'Z':  # If uppercase
        result += chr(ord(letter) + 32)  # Convert to lowercase
    else:
        result += letter  # Keep as is

# Print result
print("Lowercase text:", result)