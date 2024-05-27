import numpy as np
from BBH_SIM.dynamics import (
    compute_acceleration,
    compute_1pn_correction,
    compute_2pn_correction,
    compute_radiation_reaction,
    compute_spin_effects,
)


def test_compute_acceleration():
    r = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0])
    m1 = 1.0
    m2 = 1.0
    a = compute_acceleration(r, v, m1, m2)
    assert np.allclose(a, np.array([-1.33486e-10, 0.00000e00, 0.00000e00]), rtol=1e-6)


def test_compute_1pn_correction():
    r = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0])
    r_mag = 1.0
    v_mag = 0.1
    m1 = 1.0
    m2 = 1.0
    a_1pn = compute_1pn_correction(r, v, r_mag, v_mag, m1, m2)
    assert np.allclose(
        a_1pn, np.array([-1.4831777e-29, 0.0000000e00, 0.0000000e00]), rtol=1e-6
    )


def test_compute_2pn_correction():
    r = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0])
    r_mag = 1.0
    v_mag = 0.1
    m1 = 1.0
    m2 = 1.0
    a_2pn = compute_2pn_correction(r, v, r_mag, v_mag, m1, m2)
    assert np.allclose(
        a_2pn, np.array([-1.75985309e-55, 0.00000000e00, 0.00000000e00]), rtol=1e-6
    )


def test_compute_radiation_reaction():
    r = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0])
    r_mag = 1.0
    m1 = 1.0
    m2 = 1.0
    a_rad = compute_radiation_reaction(r, v, r_mag, m1, m2)
    assert np.allclose(
        a_rad, np.array([-0.00000000e00, -1.56610497e-73, -0.00000000e00]), rtol=1e-6
    )


def test_compute_spin_effects():
    r = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0])
    r_mag = 1.0
    s1 = np.array([0.1, 0.1, 0.1])
    s2 = np.array([0.0, 0.0, -0.1])
    spins = (s1, s2)
    a_spin = compute_spin_effects(r, v, r_mag, spins)
    assert np.allclose(
        a_spin, np.array([0.00000000e00, 0.00000000e00, -1.48317778e-29]), rtol=1e-6
    )
