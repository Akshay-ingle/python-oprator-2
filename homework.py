# Program to check if a character is an alphabet

# Input from the user
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    # Check if it is an alphabet
    if char.isalpha():
        print(f"The character '{char}' is an alphabet.")
    else:
        print(f"The character '{char}' is not an alphabet.")
else:
    print("Please enter only one character.")
