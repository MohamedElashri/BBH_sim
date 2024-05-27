# Example 1: Simulating a Binary Black Hole System

This example demonstrates how to use the BBH_SIM package to set up and run a simulation, visualize the results, and generate gravitational waveforms.

## Code

```python
from BBH_SIM.simulation import BBHSimulation
from BBH_SIM.visualization import plot_orbits_3d, plot_waveform
from BBH_SIM.waveform import generate_waveform
import numpy as np


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
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt
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
```

## Explanation

1. First, we import the necessary modules from the BBH_SIM package.

2. We set the simulation parameters, including the masses of the black holes, their initial positions and velocities, and the simulation time parameters.

3. We create an instance of the `BBHSimulation` class with the specified parameters.

4. We run the simulation using the `run()` method, which performs the numerical integration and updates the position and velocity arrays of the black holes.

5. We plot the orbits of the black holes using the `plot_orbits_3d()` function, passing the position arrays as arguments.

6. We generate the gravitational waveform using the `generate_waveform()` function, passing the time array, position arrays, and masses as arguments.

7. Finally, we plot the generated waveform using the `plot_waveform()` function, passing the time array and the plus and cross polarizations of the waveform.

This example provides a basic overview of how to use the BBH_SIM package to simulate and analyze binary black hole systems. You can modify the simulation parameters and explore different scenarios based on your requirements.

# Example 2: Saving and Loading Simulation Data

This example demonstrates how to save and load simulation data using the BBH_SIM package.

## Code

```python
from BBH_SIM.simulation import BBHSimulation
import numpy as np
import matplotlib.pyplot as plt

# Set simulation parameters
m1 = 1.0
m2 = 1.5
r1_init = np.array([0.0, 0.0, 0.0])
r2_init = np.array([2.0, 0.0, 0.0])
v1_init = np.array([0.0, 0.2, 0.0])
v2_init = np.array([0.0, -0.1, 0.0])
t_start = 0.0
t_end = 20.0
dt = 0.01

# Create a BBHSimulation instance
simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt
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
from BBH_SIM.visualization import plot_orbits_3d

plot_orbits_3d(r1_array, r2_array)
```

## Explanation

1. We set the simulation parameters and create an instance of the `BBHSimulation` class.

2. We run the simulation using the `run()` method.

3. We save the simulation data to a file named "simulation_data.txt" using the `save_data()` method.

4. We create a new instance of the `BBHSimulation` class with the same parameters.

5. We load the simulation data from the file using the `load_data()` method.

6. We can now access the loaded simulation data using the attributes of the `loaded_simulation` instance.

This example shows how you can save the simulation data to a file for later use and load it back into a new simulation instance for analysis or further processing.


# Example 3: Simulating with Post-Newtonian Corrections

This example demonstrates how to run a simulation with post-Newtonian corrections using the BBH_SIM package.

## Code

```python
from BBH_SIM.simulation import BBHSimulation
import numpy as np


# Set simulation parameters
m1 = 10.0
m2 = 8.0
r1_init = np.array([0.0, 0.0, 0.0])
r2_init = np.array([5.0, 0.0, 0.0])
v1_init = np.array([0.0, 0.1, 0.0])
v2_init = np.array([0.0, -0.1, 0.0])
t_start = 0.0
t_end = 50.0
dt = 0.01

# Create a BBHSimulation instance with post-Newtonian corrections
simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt,
    pn_order=3
)

# Run the simulation
simulation.run()

# Plot the orbits
plot_orbits_3d(simulation.r1_array, simulation.r2_array)
```

## Explanation

1. We set the simulation parameters, including the masses of the black holes and their initial positions and velocities.

2. We create an instance of the `BBHSimulation` class with `pn_order=3`, specifying that we want to include post-Newtonian corrections up to the 3rd order.

3. We run the simulation using the `run()` method.

4. We plot the orbits of the black holes using the `plot_orbits_3d()` function.

This example demonstrates how to incorporate post-Newtonian corrections in the simulation to account for relativistic effects. The `pn_order` parameter allows you to specify the desired order of corrections.


# Example 4: Simulating with Radiation Reaction

This example demonstrates how to run a simulation with radiation reaction using the BBH_SIM package.

## Code

```python
import numpy as np
from BBH_SIM.simulation import BBHSimulation

# Set simulation parameters
m1 = 5.0
m2 = 3.0
r1_init = np.array([0.0, 0.0, 0.0])
r2_init = np.array([3.0, 0.0, 0.0])
v1_init = np.array([0.0, 0.2, 0.0])
v2_init = np.array([0.0, -0.3, 0.0])
t_start = 0.0
t_end = 30.0
dt = 0.01

# Create a BBHSimulation instance with radiation reaction
simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt,
    include_radiation_reaction=True
)

# Run the simulation
simulation.run()

# Generate and plot the gravitational waveform
h_plus, h_cross = generate_waveform(
    simulation.t_array, simulation.r1_array, simulation.r2_array, m1, m2
)
plot_waveform(simulation.t_array, h_plus, h_cross)
```

## Explanation

1. We set the simulation parameters, including the masses of the black holes and their initial positions and velocities.

2. We create an instance of the `BBHSimulation` class with `include_radiation_reaction=True`, indicating that we want to include radiation reaction in the simulation.

3. We run the simulation using the `run()` method.

4. We generate the gravitational waveform using the `generate_waveform()` function.

5. We plot the generated waveform using the `plot_waveform()` function.

This example shows how to include radiation reaction in the simulation, which accounts for the energy and angular momentum loss due to gravitational wave emission. The `include_radiation_reaction` parameter allows you to enable or disable this effect.


# Example 5: Simulating with Spin Effects

This example demonstrates how to run a simulation with spin effects using the BBH_SIM package.

## Code

```python
from BBH_SIM.simulation import BBHSimulation
import numpy as np


# Set simulation parameters
m1 = 8.0
m2 = 6.0
r1_init = np.array([0.0, 0.0, 0.0])
r2_init = np.array([4.0, 0.0, 0.0])
v1_init = np.array([0.0, 0.1, 0.0])
v2_init = np.array([0.0, -0.2, 0.0])
t_start = 0.0
t_end = 40.0
dt = 0.01

# Set spin vectors
s1 = np.array([0.2, 0.0, 0.0])
s2 = np.array([0.0, 0.3, 0.0])

# Create a BBHSimulation instance with spin effects
simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt,
    spins=(s1, s2)
)

# Run the simulation
simulation.run()

# Plot the orbits
plot_orbits_3d(simulation.r1_array, simulation.r2_array)
```

## Explanation

1. We set the simulation parameters, including the masses of the black holes and their initial positions and velocities.

2. We define the spin vectors `s1` and `s2` for the two black holes.

3. We create an instance of the `BBHSimulation` class with `spins=(s1, s2)`, specifying the spin vectors for the black holes.

4. We run the simulation using the `run()` method.

5. We plot the orbits of the black holes using the `plot_orbits_3d()` function.

This example demonstrates how to include spin effects in the simulation. The `spins` parameter allows you to specify the spin vectors for each black hole, which influence their orbital dynamics.
