# Example

This example demonstrates how to use the BBH_SIM package to set up and run a simulation, visualize the results, and generate gravitational waveforms.

## Code

```python
from BBH_SIM.simulation import BBHSimulation
from BBH_SIM.visualization import plot_orbits_3d, plot_waveform
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

For more detailed information on each aspect of the package, please refer to the corresponding sections of the documentation.
