import matplotlib.pyplot as plt
import numpy as np

a=np.array([[1,1],[1,-1]])
b=np.array([5,1])
solve=np.linalg.solve(a,b)
print(solve)
print(f"x={solve[0]}   y={solve[1]}")


# Define x range
x = np.linspace(0, 5)

# Define the two equations
y1 = 5 - x       # from x + y = 5
y2 = x - 1       # from x - y = 1 => y = x - 1

# Plot the lines
plt.plot(x, y1, label='x + y = 5', color='blue')
plt.plot(x, y2, label='x - y = 1', color='red')

# Plot the point of intersection
# plt.plot(3, 2)  # black circle at (3, 2)
# plt.text(3, 2, 'p(3,2)')

# Graph details
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of x + y = 5 and x - y = 1')
plt.grid(True)
plt.legend()
plt.show()
