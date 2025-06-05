# Visualize the 3D linear system using matplotlib (as planes):
# x+ y+ z= 6
# x−y+ z= 2
# 2x+ y−z= 3


import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D as ax

a=np.array([[1,1,1],[1,-1,1],[2,1,-1]])
b=np.array([6,2,3])
solve=np.linalg.solve(a,b)
print(solve)


x=np.linspace(0,5)
z=np.linspace(0,5)
y1=6-z-x
y2=z+x-2
y3=3+z-2*x

ax.plot_surface(x,z,y1) 
ax.plot_surface(x,z,y2)
ax.plot_surface(x,z,y3)


ax.set_xlabel="x"
ax.set_ylabel="y"
ax.set_zlabel="z"


plt.show()

