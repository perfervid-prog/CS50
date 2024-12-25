"""
Problem Statement:
You are tasked with simulating the placement of stars in the sky. Given a world with coordinates ranging from -110000 to 110000 on both the x and y axes, you need to generate 500 stars (represented as dots) in a random manner such that the minimum distance between any two stars is at least 5000 units. The positions of the stars should be generated using a fixed seed value to ensure that the star positions are reproducible across multiple executions. Finally, you must plot these stars on a 2D plane using  matplotlib.
"""


import numpy as np
import matplotlib.pyplot as plt



def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def generate_stars_coord(num_stars, min_distance=5000):
    np.random.seed(0)
    world_size = 110000

    stars = []

    while len(stars) < num_stars:
        x = np.random.randint(-world_size, world_size)
        y = np.random.randint(-world_size, world_size)

        # get the last star
        for star in stars:
            if (calculate_distance(star[0], star[1], x, y)) < min_distance:
                break
        else:
            stars.append((x, y))

    return stars


stars = generate_stars_coord(500)

# Create the plot
plt.figure(figsize=(15, 15))
plt.scatter(*zip(*stars))

circle = plt.Circle((0, 0), 2500, fill=False, color='red', label='5000 units radius')
plt.gca().add_patch(circle)

plt.axis('equal')

plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.title("Star Distribution")
plt.legend()
plt.show()
