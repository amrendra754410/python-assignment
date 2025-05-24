# Write a Python program to convert a binary number to its decimal equivalent. The program should
# take a binary number as input and return the corresponding decimal value.
# Example:
# • Input: 1101
# • Output: 13



def binary_to_decimal(a):
    decimal = int(a, 2)
    return decimal
binary_number = input("Enter a binary number: ")


decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of binary {binary_number} is {decimal_number}.")
