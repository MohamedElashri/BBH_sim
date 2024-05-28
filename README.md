 # Binary Black Hole Simulation (BBH_SIM)

[![BBH_SIM CI](https://github.com/MohamedElashri/BBH_sim/actions/workflows/ci.yml/badge.svg)](https://github.com/MohamedElashri/BBH_sim/actions/workflows/ci.yml)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/MohamedElashri/BBH_sim/blob/main/LICENSE)

BBH_SIM is a Python package for simulating the dynamics and gravitational waveforms of binary black hole systems. It provides a set of tools and functions to set up and run simulations, visualize the results, and generate gravitational waveforms.

## Introduction

Binary black hole systems are one of the most fascinating and extreme phenomena in the universe. When two black holes orbit each other and eventually merge, they emit gravitational waves that ripple through spacetime. The study of binary black hole dynamics and gravitational waves has been at the forefront of research in gravitational physics, especially since the first direct detection of gravitational waves by LIGO in 2015.

`BBH_SIM` aims to provide a user-friendly and efficient framework for simulating binary black hole systems and generating gravitational waveforms. It incorporates various physical effects, including post-Newtonian corrections, radiation reaction, and spin effects, allowing users to explore different aspects of binary black hole dynamics.

## Installation

To install `BBH_SIM`, clone the repository and run the following command:

```bash
pip install .
```

## Usage

To use `BBH_SIM` in your Python scripts, simply import the necessary modules:

```python
from BBH_SIM.simulation import BBHSimulation
from BBH_SIM.visualization import plot_orbits_3d, plot_waveform
from BBH_SIM.waveform import generate_waveform
```

For detailed information on how to set up and run simulations, visualize the results, and generate gravitational waveforms, please refer to the [documentation](docs/index.md).

## Examples

The `examples` directory contains sample scripts that demonstrate how to use BBH_SIM for various tasks, such as simulating a binary black hole system, visualizing the orbits, and generating gravitational waveforms.

To run an example script, navigate to the `examples` directory and run the desired script:

```bash
cd examples
python example1.py
```

## Documentation

The `docs` directory contains detailed documentation for BBH_SIM. It includes guides on installation, quick start, simulation setup, visualization, and gravitational waveform generation. The documentation is written in Markdown format and can be easily browsed on GitHub.

To access the documentation, navigate to the `docs` directory and open the desired Markdown file.

## Contributing

Contributions to `BBH_SIM` are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

`BBH_SIM` is released under the [MIT License](LICENSE).
