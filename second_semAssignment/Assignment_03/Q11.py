# Write a Python program that assigns the numbers 10 and 10 to two different variables num1 and num2.
# Check if both variables reference the same memory location using the id() function.
# Assign two larger integers (e.g., 1000 and 1000) to num3 and num4 and check their memory locations.
# Explain why small integers might reference the same memory location, but larger integers might not.



# Assign values
num1 = 10
num2 = 10

# Check memory addresses
print("Memory address of num1:", id(num1))
print("Memory address of num2:", id(num2))
print("num1 and num2 reference same object:", id(num1) == id(num2))

# Assign larger integers
num3 = 1000
num4 = 1000

print("Memory address of num3:", id(num3))
print("Memory address of num4:", id(num4))
print("num3 and num4 reference same object:", id(num3) == id(num4))
