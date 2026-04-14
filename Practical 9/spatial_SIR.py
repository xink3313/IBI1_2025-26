# spatial_SIR.py
# A 2D spatial SIR model to simulate disease spread on a grid

import numpy as np
import matplotlib.pyplot as plt

# 1. Initialize the population grid (100x100)
# 0 = Susceptible (Purple), 1 = Infected (Green/Teal), 2 = Recovered (Yellow)
grid_size = 100
population = np.zeros((grid_size, grid_size))

# Pick a random starting point for the first outbreak
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = 1

# 2. Model parameters
beta = 0.3      # Infection probability for neighbors
gamma = 0.05    # Recovery probability
time_steps = 100

# Snapshots to plot (at time 0, 10, 50, and 100)
snapshots = [0, 10, 50, 100]
snapshot_data = {}

# 3. Time course simulation
for t in range(time_steps + 1):
    
    # Save the current state if it matches our snapshot times
    if t in snapshots:
        snapshot_data[t] = population.copy()
        
    # We use a copy of the population to update states synchronously
    new_population = population.copy()
    
    # Find the coordinates of all currently infected individuals
    infected_x, infected_y = np.where(population == 1)
    
    # Iterate through each infected person
    for i in range(len(infected_x)):
        x = infected_x[i]
        y = infected_y[i]
        
        # Check all 8 neighboring cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Skip the center cell (the infected person themselves)
                if dx == 0 and dy == 0:
                    continue
                
                nx = x + dx
                ny = y + dy
                
                # Check if the neighbor is within the grid boundaries
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    # If the neighbor is susceptible, try to infect them
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1 # Becomes infected
                            
        # The infected person attempts to recover
        if np.random.random() < gamma:
            new_population[x, y] = 2 # Becomes recovered
            
    # Update the main population grid for the next time step
    population = new_population.copy()

# 4. Plot the results in a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)
fig.suptitle("2D Spatial SIR Model Spread", fontsize=16)

# Plot each snapshot
for ax, t in zip(axes.flatten(), snapshots):
    ax.imshow(snapshot_data[t], cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
    ax.set_title(f"Time: {t}")

# Adjust layout, save and show
plt.tight_layout()
plt.savefig("spatial_SIR.png", format="png")
plt.show()