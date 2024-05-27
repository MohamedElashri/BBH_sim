import numpy as np
import matplotlib.pyplot as plt
from BBH_SIM.visualization import plot_orbits_3d, plot_waveform, plot_from_file


def test_plot_orbits_3d():
    r1_array = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
    r2_array = np.array([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
    plot_orbits_3d(r1_array, r2_array, show=False)
    plt.close()


def test_plot_waveform():
    t_array = np.linspace(0, 10, 100)
    h_plus = np.sin(t_array)
    h_cross = np.cos(t_array)
    plot_waveform(t_array, h_plus, h_cross, show=False)
    plt.close()


def test_plot_from_file(tmpdir):
    data = np.array(
        [
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.1, 0.0],
            [1.0, 1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.2, 0.0],
        ]
    )
    file_path = tmpdir.join("simulation_data.txt")
    np.savetxt(file_path, data)
    plot_from_file(file_path, plot_type="orbits", show=False)
    plt.close()
    plot_from_file(file_path, plot_type="waveform", show=False)
    plt.close()
