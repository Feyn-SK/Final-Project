'''States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black
from state_class import state

class Light_Blue(state):
    state = 1

    def action(self):
        if 4 in self.neighborhood:
            return True, self.neighbhorhood.index(4)
    '''


import numpy as np
import time
from Neighborhood import get_neighbors

# Create a dictionary to track how many times each cell has turned dark blue
dark_blue_counter = {}


def update_light_blue(grid):
    rows, cols = grid.shape
    updated_grid = grid.copy()

    # Handle light blue activation
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Light blue state
                neighbors = get_neighbors(grid, i, j)

                # Check if there's at least one black neighbor
                if 4 in neighbors:
                    print(f"Activating light blue cell at ({i},{j})")

                    # Simulate action potential delay
                    time.sleep(1)

                    # Cell becomes dark blue
                    updated_grid[i][j] = 2

                    # Increment activation count in the counter
                    if (i, j) not in dark_blue_counter:
                        dark_blue_counter[(i, j)] = 1
                    else:
                        dark_blue_counter[(i, j)] += 1

                    # Find and remove ONE nearby black cell (convert it to white)
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            ni, nj = i + dx, j + dy
                            if (dx == 0 and dy == 0) or not (0 <= ni < rows and 0 <= nj < cols):
                                continue
                            if updated_grid[ni][nj] == 4:
                                updated_grid[ni][nj] = 0
                                print(f"Removed black cell at ({ni},{nj})")
                                break
                        else:
                            continue
                        break

    # Check for degradation due to repeated firing
    for i in range(rows):
        for j in range(cols):
            if dark_blue_counter.get((i, j), 0) >= 5:
                print(f"Cell at ({i},{j}) degraded after 5 activations")
                updated_grid[i][j] = 0  # Neuron dies (becomes empty)
                dark_blue_counter[(i, j)] = 0  # Reset counter

    return updated_grid
