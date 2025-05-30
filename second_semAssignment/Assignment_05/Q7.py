import numpy as np
import random
np.random.seed(1)
matrix=np.random.randint(0,9,size=(3,3))
print(matrix)
# matrix=np.array([[1,2,1],[2,4,0],[3,6,3]])
det=np.linalg.det(matrix)
print(det)
if(det!=0):
    print("Matrix is invertible")
else:
    print("Matrix is not invertible")
