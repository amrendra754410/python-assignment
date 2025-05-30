# Use NumPy to solve a 5×5 linear system generated with random integers using np.random.randint.
# Create a random 5 ×1 constant vector and solve using np.linalg.solve()

import numpy as np
np.random.seed(1)
matrix=np.random.randint(0,9, size=(5,5))
print(matrix)

cont=np.random.randint(0,5,size=(5,1))
print(cont)

print(np.linalg.solve(matrix,cont))