# Plot the line y= 3x using matplotlib. (Note: Correct from “vertical line”.
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10)
y=3*x
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.title("y= 3x")
plt.show()