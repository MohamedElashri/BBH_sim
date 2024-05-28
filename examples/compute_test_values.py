import numpy as np
from BBH_SIM.dynamics import (
    compute_acceleration,
    compute_1pn_correction,
    compute_2pn_correction,
    compute_radiation_reaction,
    compute_spin_effects,
)


def compute_test_values():
    # Test case for compute_acceleration
    r = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 0.1, 0.0])
    m1 = 1.0
    m2 = 1.0
    a = compute_acceleration(r, v, m1, m2)
    print("compute_acceleration:")
    print(f"Expected: {a}")

    # Test case for compute_1pn_correction
    r_mag = 1.0
    v_mag = 0.1
    a_1pn = compute_1pn_correction(r, v, r_mag, v_mag, m1, m2)
    print("\ncompute_1pn_correction:")
    print(f"Expected: {a_1pn}")

    # Test case for compute_2pn_correction
    a_2pn = compute_2pn_correction(r, v, r_mag, v_mag, m1, m2)
    print("\ncompute_2pn_correction:")
    print(f"Expected: {a_2pn}")

    # Test case for compute_radiation_reaction
    a_rad = compute_radiation_reaction(r, v, r_mag, m1, m2)
    print("\ncompute_radiation_reaction:")
    print(f"Expected: {a_rad}")

    # Test case for compute_spin_effects
    s1 = np.array([0.1, 0.1, 0.1])
    s2 = np.array([0.0, 0.0, -0.1])
    spins = (s1, s2)
    a_spin = compute_spin_effects(r, v, r_mag, spins)
    print("\ncompute_spin_effects:")
    print(f"Expected: {a_spin}")


if __name__ == "__main__":
    compute_test_values()
