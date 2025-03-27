#Ask user to input string and prefix to remove
string = input("Enter a word: ")
prefix = input("Prefix to remove in the word: ")

# Check if the string starts with the given prefix
if string.startswith(prefix):
    # Remove the prefix by slicing the string
    string = string[len(prefix):]

# Print the resulting string
print("Result:", string)

