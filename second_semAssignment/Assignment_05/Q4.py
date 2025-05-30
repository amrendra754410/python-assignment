# Visualize the system given in Question 3 using matplotlib
# 2x+ 3y= 6
# 4x+ 6y= 12


import numpy as np;
import matplotlib.pyplot as plt

a=np.array([[2,3],[4,6]])
b=np.array([4,6])
# solve=np.linalg.solve(a,b)
# print(f"x={solve[0]}   y={solve[1]}")

x=np.linspace(0,6)
y1=(6-2*x)/3
y2=(12-4*x)/6   

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

