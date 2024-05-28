from BBH_SIM.visualization import plot_orbits_2d, animate_trajectories_2d
from BBH_SIM.simulation import BBHSimulation
import numpy as np

# Set simulation parameters
m1 = 1.0  # Mass of the first black hole
m2 = 1.5  # Mass of the second black hole
r1_init = np.array([0.0, 1.0, 0.0])  # Initial position of the first black hole
r2_init = np.array([1.0, 0.0, 0.0])  # Initial position of the second black hole

# Initial velocity of the first black hole (for circular orbit)
v1_init = np.array([0.0, -0.5, 0.0])
# Initial velocity of the second black hole (for circular orbit)t_start = 0.0
v2_init = np.array([0.0, 0.5, 0.0])
t_start = 0.0
t_end = 20.0
dt = 0.01

# Create and run the simulation
simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt
)
simulation.run()

# Save and reload the data
filename = "simulation_data.txt"
simulation.save_data(filename)
simulation.load_data(filename)

# Plot and animate the results
plot_orbits_2d(simulation.r1_array_2d, simulation.r2_array_2d)
animate_trajectories_2d(
    simulation.r1_array_2d, simulation.r2_array_2d, save_path="trajectories.gif"
)
