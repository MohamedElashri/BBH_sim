# Waveform

The BBH_SIM package provides functions to generate gravitational waveforms from the binary black hole simulation results.

## Generating Waveforms

To generate the gravitational waveforms, use the `generate_waveform()` function:

```python
from BBH_SIM.waveform import generate_waveform

h_plus, h_cross = generate_waveform(
    simulation.t_array, simulation.r1_array, simulation.r2_array, m1, m2
)
```

This function takes the time array (`t_array`), position arrays of the black holes (`r1_array` and `r2_array`), and their masses (`m1` and `m2`) as input and returns the plus and cross polarizations of the gravitational waveform (`h_plus` and `h_cross`).

## Computing Polarizations

The `generate_waveform()` function internally calls the `compute_h_plus()` and `compute_h_cross()` functions to compute the individual polarizations of the gravitational waveform.

```python
from BBH_SIM.waveform import compute_h_plus, compute_h_cross

h_plus = compute_h_plus(r, m1, m2)
h_cross = compute_h_cross(r, m1, m2)
```

These functions take the separation vector between the black holes (`r`) and their masses (`m1` and `m2`) as input and return the corresponding polarization of the gravitational waveform.

You can use these functions directly if you need to compute the polarizations at specific time steps or separation vectors.

For more information on visualizing the generated waveforms, please refer to the [Visualization](visualization.md) section of the documentation.
