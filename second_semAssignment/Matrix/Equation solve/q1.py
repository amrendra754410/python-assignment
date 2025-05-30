import numpy as np

a=np.array([[2,-6,6],
            [2,3,-1],
            [4,-3,-1]])
b=np.array([-8,15,19])

solve=np.linalg.solve(a,b)
print(solve)
print(np.linalg.det(b))