import numpy as np
import matplotlib.pyplot as plt


def plot_orbits_3d(
    r1_array, r2_array, fig=None, ax=None, show=True, save_path=None, **kwargs
):
    """
    Plot the 3D orbits of the binary black holes.

    Parameters:
    - r1_array (numpy.ndarray): Array of position vectors of the first black hole.
    - r2_array (numpy.ndarray): Array of position vectors of the second black hole.
    - fig (matplotlib.figure.Figure): Figure object to use for plotting (default: None).
    - ax (matplotlib.axes.Axes): Axes object to use for plotting (default: None).
    - show (bool): Whether to display the plot (default: True).
    - save_path (str): Path to save the plot (default: None).
    - **kwargs: Additional keyword arguments to pass to the plotting function.
    """
    if fig is None and ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

    ax.plot(
        r1_array[:, 0], r1_array[:, 1], r1_array[:, 2], label="Black Hole 1", **kwargs
    )
    ax.plot(
        r2_array[:, 0], r2_array[:, 1], r2_array[:, 2], label="Black Hole 2", **kwargs
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend()

    if save_path is not None:
        plt.savefig(save_path)
    if show:
        plt.show()


def plot_waveform(
    t_array, h_plus, h_cross, fig=None, ax=None, show=True, save_path=None, **kwargs
):
    """
    Plot the gravitational waveform.

    Parameters:
    - t_array (numpy.ndarray): Array of time values.
    - h_plus (numpy.ndarray): Plus polarization of the gravitational waveform.
    - h_cross (numpy.ndarray): Cross polarization of the gravitational waveform.
    - fig (matplotlib.figure.Figure): Figure object to use for plotting (default: None).
    - ax (matplotlib.axes.Axes): Axes object to use for plotting (default: None).
    - show (bool): Whether to display the plot (default: True).
    - save_path (str): Path to save the plot (default: None).
    - **kwargs: Additional keyword arguments to pass to the plotting function.
    """
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    ax.plot(t_array, h_plus, label="Plus Polarization", **kwargs)
    ax.plot(t_array, h_cross, label="Cross Polarization", **kwargs)
    ax.set_xlabel("Time")
    ax.set_ylabel("Strain")
    ax.legend()

    if save_path is not None:
        plt.savefig(save_path)
    if show:
        plt.show()


def plot_from_file(file_path, plot_type="orbits", **kwargs):
    """
    Plot the simulation data from a file.

    Parameters:
    - file_path (str): Path to the simulation data file.
    - plot_type (str): Type of plot to generate ('orbits' or 'waveform').
    - **kwargs: Additional keyword arguments to pass to the respective plotting function.
    """
    data = np.loadtxt(file_path)
    t_array = data[:, 0]
    r1_array = data[:, 1:4]
    r2_array = data[:, 4:7]

    if plot_type == "orbits":
        plot_orbits_3d(r1_array, r2_array, **kwargs)
    elif plot_type == "waveform":
        h_plus = data[:, 7]
        h_cross = data[:, 8]
        plot_waveform(t_array, h_plus, h_cross, **kwargs)
    else:
        raise ValueError(
            f"Invalid plot type: {plot_type}. Supported types are 'orbits' and 'waveform'."
        )
