# Quickstart

This guide will walk you through the basic steps to get started with the BBH_SIM package.

## Importing the Package

To use the BBH_SIM package in your Python program, start by importing the necessary modules:

```python
from BBH_SIM.simulation import BBHSimulation
from BBH_SIM.visualization import plot_orbits_3d, plot_waveform
from BBH_SIM.waveform import generate_waveform
```

## Setting Up the Simulation

Create an instance of the `BBHSimulation` class with the desired simulation parameters:

```python
simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt,
    pn_order=1, include_radiation_reaction=False, spins=None
)
```

- `m1`, `m2`: Masses of the two black holes.
- `r1_init`, `r2_init`: Initial position vectors of the black holes.
- `v1_init`, `v2_init`: Initial velocity vectors of the black holes.
- `t_start`, `t_end`: Start and end times of the simulation.
- `dt`: Time step size.
- `pn_order`: Post-Newtonian order (default: 1).
- `include_radiation_reaction`: Flag to include radiation reaction (default: False).
- `spins`: Spin vectors of the black holes (default: None).

## Running the Simulation

To run the simulation, call the `run()` method on the simulation instance:

```python
simulation.run()
```

This will perform the numerical integration and update the position and velocity arrays of the black holes.

## Visualizing the Results

To visualize the orbits of the black holes in a 3D plot, use the `plot_orbits_3d()` function:

```python
plot_orbits_3d(simulation.r1_array, simulation.r2_array)
```

To generate and plot the gravitational waveform, use the `generate_waveform()` and `plot_waveform()` functions:

```python
h_plus, h_cross = generate_waveform(
    simulation.t_array, simulation.r1_array, simulation.r2_array, m1, m2
)
plot_waveform(simulation.t_array, h_plus, h_cross)
```

That's it! You've now learned the basic steps to set up and run a simulation using the BBH_SIM package. For more detailed information and advanced usage, please refer to the other sections of the documentation.

