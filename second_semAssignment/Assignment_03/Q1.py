# Write a Python program that takes a decimal number as input and converts it to its binary, octal, and
# hexadecimal representations.
# Instructions:
# • The program should ask the user to input a decimal number.
# • Convert the number to binary, octal, and hexadecimal.
# • Output all three representations.

# Program to convert decimal to binary, octal, and hexadecimal




# Get user input
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary, octal, and hexadecimal
binary = bin(decimal_number)
octal = oct(decimal_number)
hexadecimal = hex(decimal_number)

# Display the results
print(f"Binary representation: {binary}")
print(f"Octal representation: {octal}")
print(f"Hexadecimal representation: {hexadecimal}")
