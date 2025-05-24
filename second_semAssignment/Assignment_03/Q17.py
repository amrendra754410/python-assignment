# Write a python program using scipy for a traveling salesman who drives around to visit N cities,
# including his home city, to try to sell his balloons and then return home. He wants to minimize the
# distance he travels so that his fuel costs are as small as possible.


import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import differential_evolution

# Define coordinates of cities (including home city)
# Format: [(x1, y1), (x2, y2), ..., (xN, yN)]
city_coordinates = np.array([
    [0, 0],   # Home city
    [2, 3],
    [5, 4],
    [1, 6],
    [7, 3],
    [4, 1]
])

# Calculate distance matrix
dist_matrix = squareform(pdist(city_coordinates, metric='euclidean'))

# Objective function: total distance of TSP route
def total_distance(order):
    order = np.argsort(order)
    dist = 0
    for i in range(len(order)):
        dist += dist_matrix[order[i], order[(i + 1) % len(order)]]
    return dist

# Bounds for each city position in the solution
bounds = [(0, 1)] * len(city_coordinates)

# Solve using differential evolution
result = differential_evolution(total_distance, bounds, strategy='best1bin', maxiter=1000, popsize=15)

# Get final route
best_order = np.argsort(result.x)
best_route = city_coordinates[best_order]
best_distance = total_distance(result.x)

# Output
print("Optimal Visit Order of Cities (Indices):", best_order)
print("Coordinates of Optimal Route:", best_route)
print("Minimum Total Distance:", round(best_distance, 2))
