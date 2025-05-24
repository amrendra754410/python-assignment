# Define a sample set
A = {1, 2, 3}

# Define a relation as a set of tuples
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}  # You can modify this set to test different properties

# Check Reflexive
def is_reflexive(A, R):
    for a in A:
        if (a, a) not in R:
            return False
    return True

# Check Symmetric
def is_symmetric(R):
    for (a, b) in R:
        if (b, a) not in R:
            return False
    return True

# Check Transitive
def is_transitive(R):
    for (a, b) in R:
        for (x, c) in R:
            if b == x:
                if (a, c) not in R:
                    return False
    return True

# Check Anti-symmetric
def is_anti_symmetric(R):
    for (a, b) in R:
        if a != b and (b, a) in R:
            return False
    return True

# Check Equivalence
def is_equivalence(A, R):
    if not is_reflexive(A, R):
        return False
    if not is_symmetric(R):
        return False
    if not is_transitive(R):
        return False
    return True

# Display results
print("Relation R:", R)
print("Reflexive:", is_reflexive(A, R))
print("Symmetric:", is_symmetric(R))
print("Transitive:", is_transitive(R))
print("Anti-symmetric:", is_anti_symmetric(R))
print("Equivalence Relation:", is_equivalence(A, R))
