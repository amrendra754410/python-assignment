# Take input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary, octal, and hexadecimal
binary = bin(decimal_number)       # [2:] removes the '0b' prefix
octal = oct(decimal_number)        # [2:] removes the '0o' prefix
hexadecimal = hex(decimal_number)  # [2:] removes the '0x' prefix

# Display the results
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal.upper())  # Use upper() for capital letters
