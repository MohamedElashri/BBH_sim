import numpy as np
from BBH_SIM.waveform import generate_waveform, compute_h_plus, compute_h_cross


def test_generate_waveform():
    t_array = np.linspace(0, 10, 100)
    r1_array = np.zeros((100, 3))
    r2_array = np.ones((100, 3))
    m1 = 1.0
    m2 = 1.0
    h_plus, h_cross = generate_waveform(t_array, r1_array, r2_array, m1, m2)
    assert h_plus.shape == (100,)
    assert h_cross.shape == (100,)


def test_compute_h_plus():
    r = np.array([1.0, 0.0, 0.0])
    m1 = 1.0
    m2 = 1.0
    h_plus = compute_h_plus(r, m1, m2)
    assert np.isclose(h_plus, 1.0)


def test_compute_h_cross():
    r = np.array([1.0, 0.0, 0.0])
    m1 = 1.0
    m2 = 1.0
    h_cross = compute_h_cross(r, m1, m2)
    assert np.isclose(h_cross, 0.5)
