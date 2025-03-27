#Get user input
text = input("Enter text: ")

#Assume the text is uppercase initially
is_upper = True

#Check each character
for letter in text:
    if 'a' <= letter <= 'z':  # If lowercase
        is_upper = False
        #Stop Loop
        break

# Print result
if is_upper:
    print("The text is fully uppercase.")
else:
    print("The text is NOT fully uppercase.")