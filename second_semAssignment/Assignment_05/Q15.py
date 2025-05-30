import random
import numpy as np
np.random.seed(1)

a=np.random.randint(0,9,size=(10,10))
print(a)
b=np.random.randint(0,9,size=(10,1))
print(b)

solve=np.linalg.solve(a,b)
print(solve)