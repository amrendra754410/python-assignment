import numpy as np

# Coefficient matrix
A = np.array([[2, 3],
              [4, 6]])

# Constant matrix
B = np.array([6, 12])

# Calculate rank of coefficient matrix and augmented matrix
rank_A = np.linalg.matrix_rank(A)
# print(rank_A)
augmented_matrix = np.column_stack((A, B))
# print(augmented_matrix)
rank_augmented = np.linalg.matrix_rank(augmented_matrix)

# print(A.shape[1])



# Check for dependency
if rank_A == rank_augmented and rank_A < A.shape[1]:
    print("The system is dependent (infinitely many solutions).")
elif rank_A == rank_augmented:
    print("The system has a unique solution.")
else:
    print("The system is inconsistent (no solution).")
