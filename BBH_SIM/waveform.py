# waveform.py

import numpy as np


def generate_waveform(t_array, r1_array, r2_array, m1, m2):
    """
    Generate the gravitational waveform from the binary black hole trajectory.

    Parameters:
    - t_array (numpy.ndarray): Array of time values.
    - r1_array (numpy.ndarray): Array of position vectors of the first black hole.
    - r2_array (numpy.ndarray): Array of position vectors of the second black hole.
    - m1 (float): Mass of the first black hole.
    - m2 (float): Mass of the second black hole.

    Returns:
    - h_plus (numpy.ndarray): Plus polarization of the gravitational waveform.
    - h_cross (numpy.ndarray): Cross polarization of the gravitational waveform.
    """
    r_array = r2_array - r1_array
    h_plus = np.array([compute_h_plus(r, m1, m2) for r in r_array])
    h_cross = np.array([compute_h_cross(r, m1, m2) for r in r_array])
    return h_plus, h_cross


def compute_h_plus(r, m1, m2):
    """
    Compute the plus polarization of the gravitational waveform at a given separation.

    Parameters:
    - r (numpy.ndarray): Separation vector between the black holes.
    - m1 (float): Mass of the first black hole.
    - m2 (float): Mass of the second black hole.

    Returns:
    - h_plus (float): Plus polarization of the gravitational waveform.
    """
    r_mag = np.linalg.norm(r)
    mu = m1 * m2 / (m1 + m2)  # Reduced mass
    return 2 * mu / r_mag


def compute_h_cross(r, m1, m2):
    """
    Compute the cross polarization of the gravitational waveform at a given separation.

    Parameters:
    - r (numpy.ndarray): Separation vector between the black holes.
    - m1 (float): Mass of the first black hole.
    - m2 (float): Mass of the second black hole.

    Returns:
    - h_cross (float): Cross polarization of the gravitational waveform.
    """
    r_mag = np.linalg.norm(r)
    mu = m1 * m2 / (m1 + m2)  # Reduced mass
    return mu / r_mag
