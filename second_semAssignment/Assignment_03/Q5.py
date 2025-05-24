# Write a Python program to find the Two’s complement representation of a given integer (positive or
# negative) using an 8-bit representation.
# Instructions:
# The program should ask the user to input an integer.
# If the number is positive, find its binary form.
# If the number is negative, compute the Two’s complement in 8 bits.
# Output the Two’s complement.



def to_twos_complement_8bit(num):
    if -128 <= num <= 127:
        if num >= 0:
            # Positive number: just format to 8-bit binary
            return format(num, '08b')
        else:
            # Negative number: compute Two's complement
            return format((1 << 8) + num, '08b')
    else:
        return "Error: Number out of range for 8-bit representation."

# Main program
try:
    user_input = int(input("Enter an integer between -128 and 127: "))
    result = to_twos_complement_8bit(user_input)
    print("8-bit Two's complement representation:", result)
except ValueError:
    print("Invalid input! Please enter an integer.")
