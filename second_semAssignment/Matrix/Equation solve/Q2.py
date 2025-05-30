# example of inconsistent and dependent systemwith numpy

import numpy as np

# inconsistent system
a=np.array([[2,1],[6,3]])
b=np.array([3,3])
solve=np.linalg.solve(a,b)
print(solve)

a=np.array([[2,1],[6,3]])
b=np.array([1,3])
print(np.linalg.solve(a,b))