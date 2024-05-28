from BBH_SIM.simulation import BBHSimulation
from BBH_SIM.visualization import plot_orbits_3d
import numpy as np

# Set simulation parameters
m1 = 1000.0
m2 = 1.5
r1_init = np.array([0.0, 0.0, 0.0])
r2_init = np.array([2.0, 0.0, 0.0])
v1_init = np.array([0.0, 0.2, 0.0])
v2_init = np.array([0.0, -0.1, 0.0])
t_start = 0.0
t_end = 20.0
dt = 0.01

# Create a BBHSimulation instance)
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

# Save the simulation data to a file
simulation.save_data("simulation_data.txt")

# Create a new BBHSimulation instance
loaded_simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt
)

# Load the simulation data from the file
loaded_simulation.load_data("simulation_data.txt")

# Access the loaded simulation data
t_array = loaded_simulation.t_array
r1_array = loaded_simulation.r1_array
r2_array = loaded_simulation.r2_array

# plot the orbits
plot_orbits_3d(r1_array, r2_array)
