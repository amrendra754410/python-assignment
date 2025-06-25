# Define the list and the integer
list1 = [1, 2, 3]
int1 = 10

# Print memory addresses before modification
print("Before modification:")
print("Memory address of list1:", id(list1))
print("Memory address of int1:", id(int1))

# Modify the list and the integer
list1.append(4)
int1 += 1

# Print memory addresses after modification
print("\nAfter modification:")
print("Memory address of list1:", id(list1))   # Should remain the same
print("Memory address of int1:", id(int1))     # Will likely change
