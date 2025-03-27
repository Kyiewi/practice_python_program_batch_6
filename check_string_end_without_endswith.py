# Ask user for input
string = input("Enter a word: ")
suffix = input("Suffix to check: ")

# Get lengths of string and suffix
suffix_length = len(suffix)
string_length = len(string)

# Check if the suffix is not longer than the string
if suffix_length <= string_length:
    # Extract the ending part of the string
    end_part = string[string_length - suffix_length:]

    # Compare with the given suffix
    if end_part == suffix:
        print("The string ends with the suffix.")
    else:
        print("The string does NOT end with the suffix.")
else:
    print("The suffix is longer than the word, so it cannot match.")