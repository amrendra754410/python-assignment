# Plot the line y= 2x+ 1 using matplotlib.

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10 )
y=2*x+1
plt.plot(x,y)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y= 2x+ 1")
plt.show()

