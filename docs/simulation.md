# Simulation

The `BBHSimulation` class is the core component of the BBH_SIM package. It provides functionality to set up and run simulations of binary black hole systems.

## Initialization

To create an instance of the `BBHSimulation` class, you need to provide the following parameters:

- `m1`, `m2`: Masses of the two black holes.
- `r1_init`, `r2_init`: Initial position vectors of the black holes.
- `v1_init`, `v2_init`: Initial velocity vectors of the black holes.
- `t_start`, `t_end`: Start and end times of the simulation.
- `dt`: Time step size.
- `pn_order`: Post-Newtonian order (default: 1).
- `radiation`: Flag to include radiation reaction (default: False).
- `spin`: Flag to include spin effects (default: False).
- `spins`: Spin vectors of the black holes (default: None).

Example:
```python
from BBH_SIM.simulation import BBHSimulation

m1 = 1.0
m2 = 1.0
r1_init = np.array([0.0, 0.0, 0.0])
r2_init = np.array([1.0, 0.0, 0.0])
v1_init = np.array([0.0, 0.1, 0.0])
v2_init = np.array([0.0, -0.1, 0.0])
t_start = 0.0
t_end = 10.0
dt = 0.01

simulation = BBHSimulation(
    m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt, pn_order=1, radiation=False, spin=False, spins=None
)
```

## Running the Simulation

To run the simulation, call the `run()` method on the simulation instance:

```python
simulation.run()
```

This will perform the numerical integration and update the position and velocity arrays of the black holes.

## Accessing Simulation Data

After running the simulation, you can access the position and velocity arrays of the black holes using the following attributes:

- `simulation.t_array`: Array of time values.
- `simulation.r1_array`: Array of position vectors of the first black hole.
- `simulation.r2_array`: Array of position vectors of the second black hole.
- `simulation.v1_array`: Array of velocity vectors of the first black hole.
- `simulation.v2_array`: Array of velocity vectors of the second black hole.

These arrays can be used for further analysis or visualization of the simulation results.

## Saving and Loading Simulation Data

To save the simulation data to a file, use the `save_data()` method:

```python
simulation.save_data("simulation_data.txt")
```

To load simulation data from a file, use the `load_data()` method:

```python
simulation.load_data("simulation_data.txt")
```

This allows you to save and retrieve simulation results for later use or analysis.

For more information on visualizing the simulation results and generating waveforms, please refer to the [Visualization](visualization.md) and [Waveform](waveform.md) sections of the documentation.
