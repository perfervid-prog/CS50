# Star Distribution Simulation

This program simulates the placement of 500 stars in a 2D space, ensuring that the minimum distance between any two stars is at least 5000 units. The coordinates are generated using a fixed seed for reproducibility.  The simulation utilizes NumPy for random number generation and Matplotlib for visualization.


## Problem Statement

The goal is to generate the coordinates of 500 stars within a world with coordinates ranging from -110,000 to 110,000 on both the x and y axes.  A crucial constraint is that the minimum distance between any two stars must be at least 5000 units. This is visualized by a red circle centered at (0,0) with a radius of 5000 units.

## Code Description

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_distance(x1, y1, x2, y2):
    """Calculates the Euclidean distance between two points."""
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def generate_stars_coord(num_stars, min_distance=5000):
    """Generates star coordinates with a minimum distance constraint."""
    np.random.seed(0)  # Fixed seed for reproducibility
    world_size = 110000

    stars = []

    while len(stars) < num_stars:
        x = np.random.randint(-world_size, world_size)
        y = np.random.randint(-world_size, world_size)

        # Check for distance to existing stars. Crucial optimization.
        valid_placement = True
        for star in stars:
            if calculate_distance(star[0], star[1], x, y) < min_distance:
                valid_placement = False
                break
        if valid_placement:
            stars.append((x, y))

    return stars


stars = generate_stars_coord(500)

# Plotting the stars
plt.figure(figsize=(15, 15))
plt.scatter(*zip(*stars), s=5)  # Use smaller marker size

# Plotting the constraint radius (5000 units)
circle = plt.Circle((0, 0), 5000, fill=False, color='red', label='5000 units radius')
plt.gca().add_patch(circle)

plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.title("Star Distribution (Minimum Distance = 5000)")
plt.legend()
plt.axis('equal')  # Ensures correct aspect ratio for visualization
plt.show()
```

## Implementation Details

### Key Functions

1. `calculate_distance(x1, y1, x2, y2)`
   - Calculates Euclidean distance between two points
   - Returns distance as a float value

2. `generate_stars_coord(num_stars, min_distance=5000)`
   - Generates star coordinates using random sampling
   - Validates minimum distance requirement
   - Returns list of (x,y) coordinate tuples

### Visualization Components

- Uses matplotlib for plotting
- Scatter plot for star positions
- Reference circle with 5000-unit radius
- Equal aspect ratio for accurate distance representation


## Installation

### Prerequisites
- Python 3.9 or higher
- Packages (numpy, matplotlib)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/perfervid-prog/CS50.git
   cd CS50
   ```
2. **Create a virtual enviroment (use cmd)**

    ```bash
    python -m venv env
    source env/bin/activate    # For Linux/macOS
    env\Scripts\activate       # For Windows
    ```

3. **Install Dependencies**<br>
    Use the provided `requirements.txt` file to install the necessary python packages.

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the code**<br>

    Now, there you go. Launch the Streamlit app:

    ```bash
    python Assignments/star_allocating_problem_in_2D.py
    ```
---

## Project Structure

```bash
CS50/
│
├── Assignments/
│   ├── star_allocating_problem_in_2D.py
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
```