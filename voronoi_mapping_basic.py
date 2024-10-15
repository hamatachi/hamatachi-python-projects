import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

def generate_random_points(num_points, min_val=0, max_val=10):
    return np.random.uniform(min_val, max_val, size=(num_points, 2))

def plot_voronoi(points):
    vor = Voronoi(points)
    
    fig, ax = plt.subplots()
    
    # Plot the Voronoi diagram
    for simplex in vor.ridge_vertices:
        if -1 not in simplex:
            plt.plot(vor.vertices[simplex, 0], vor.vertices[simplex, 1], 'k-')
    
    # Plot the points
    plt.plot(points[:, 0], points[:, 1], 'ro')
    
    # Set axis limits
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    
    plt.title("Voronoi Diagram")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    plt.show()

# Generate random points
num_points = 20
points = generate_random_points(num_points)

# Plot the Voronoi diagram
plot_voronoi(p
