# Define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
union_set = A.union(B)  # or A | B
print("Union:", union_set)

# Intersection
intersection_set = A.intersection(B)  # or A & B
print("Intersection:", intersection_set)

# Difference (A - B)
difference_set = A.difference(B)  # or A - B
print("Difference (A - B):", difference_set)

# Difference (B - A)
difference_set2 = B.difference(A)
print("Difference (B - A):", difference_set2)



#Membership Checking
# Check if 3 is in set A
print("Is 3 in A?", 3 in A)

# Check if 10 is in set B
print("Is 10 in B?", 10 in B)


# Subset Checking

C = {1, 2}
D = {1, 2, 3, 4}

# Check if C is a subset of D
print("Is C a subset of D?", C.issubset(D))

# Check if D is a subset of C
print("Is D a subset of C?", D.issubset(C))


