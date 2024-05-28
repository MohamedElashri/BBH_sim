# example.py

import numpy as np
from BBH_SIM.simulation import BBHSimulation
from BBH_SIM.visualization import plot_orbits_3d, plot_waveform, animate_trajectories_3d
from BBH_SIM.waveform import generate_waveform

# Set simulation parameters
m1 = 1.0  # Mass of the first black hole
m2 = 1.0  # Mass of the second black hole
r1_init = np.array([0.0, 0.0, 0.0])  # Initial position of the first black hole
r2_init = np.array([1.0, 0.0, 0.0])  # Initial position of the second black hole
v1_init = np.array([0.0, 0.1, 0.0])  # Initial velocity of the first black hole
v2_init = np.array([0.0, -0.1, 0.0])  # Initial velocity of the second black hole
t_start = 0.0  # Start time of the simulation
t_end = 10.0  # End time of the simulation
dt = 0.01  # Time step

# Create a BBHSimulation instance
simulation = BBHSimulation(
    m1,
    m2,
    r1_init,
    r2_init,
    v1_init,
    v2_init,
    t_start,
    t_end,
    dt,
    pn_order=2,
    radiation=True,
    spin=True,
    spin1=np.array([0.1, 0.2, 0.3]),
    spin2=np.array([0.4, 0.5, 0.6]),
)
# Run the simulation
simulation.run()

# Plot the orbits
plot_orbits_3d(simulation.r1_array, simulation.r2_array)

# Generate and plot the gravitational waveform
h_plus, h_cross = generate_waveform(
    simulation.t_array, simulation.r1_array, simulation.r2_array, m1, m2
)

plot_waveform(simulation.t_array, h_plus, h_cross)

animate_trajectories_3d(
    simulation.r1_array, simulation.r2_array, save_path="trajectories.gif"
)
