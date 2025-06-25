import numpy as np
# x=5,y=1,z=-2

e1=np.array([[2,-6,6],[2,3,-1],[4,-3,-1]])
s=np.array([-8,15,19])
solve=np.linalg.solve(e1,s)
print(f"x={solve[0]} y={solve[1]} z={solve[2]}")


inv=np.linalg.inv(e1)
# det=np.linalg.det(e1)
prod=np.dot(inv,s)  
print(f"x={prod[0]} y={prod[1]} z={prod[2]}")



