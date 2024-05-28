import numpy as np
from BBH_SIM.simulation import BBHSimulation


def test_bbh_simulation():
    m1 = 1.0
    m2 = 1.0
    r1_init = np.array([0.0, 0.0, 0.0])
    r2_init = np.array([1.0, 0.0, 0.0])
    v1_init = np.array([0.0, 0.1, 0.0])
    v2_init = np.array([0.0, -0.1, 0.0])
    t_start = 0.0
    t_end = 1.0
    dt = 0.1

    simulation = BBHSimulation(
        m1, m2, r1_init, r2_init, v1_init, v2_init, t_start, t_end, dt
    )
    simulation.run()

    assert simulation.r1_array.shape == (11, 3)
    assert simulation.r2_array.shape == (11, 3)
    assert simulation.r1_array_2d.shape == (11, 2)
    assert simulation.r2_array_2d.shape == (11, 2)
    assert np.allclose(simulation.t_array, np.arange(0.0, 1.1, 0.1))
