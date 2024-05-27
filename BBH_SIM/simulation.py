# simulation.py

import numpy as np
from BBH_SIM.dynamics import compute_acceleration


class BBHSimulation:
    def __init__(
        self,
        m1,
        m2,
        r1_init,
        r2_init,
        v1_init,
        v2_init,
        t_start,
        t_end,
        dt,
        pn_order=1,
        include_radiation_reaction=False,
        spins=None,
    ):
        self.m1 = m1
        self.m2 = m2
        self.r1 = r1_init
        self.r2 = r2_init
        self.v1 = v1_init
        self.v2 = v2_init
        self.t_start = t_start
        self.t_end = t_end
        self.dt = dt
        self.pn_order = pn_order
        self.include_radiation_reaction = include_radiation_reaction
        self.spins = spins

        self.t_array = np.arange(t_start, t_end + dt, dt)
        self.r1_array = np.zeros((len(self.t_array), 3))
        self.r2_array = np.zeros((len(self.t_array), 3))
        self.v1_array = np.zeros((len(self.t_array), 3))
        self.v2_array = np.zeros((len(self.t_array), 3))

    def run(self):
        self.r1_array[0] = self.r1
        self.r2_array[0] = self.r2
        self.v1_array[0] = self.v1
        self.v2_array[0] = self.v2

        for i in range(1, len(self.t_array)):
            r = self.r2 - self.r1
            v = self.v2 - self.v1

            a1 = compute_acceleration(
                r,
                v,
                self.m1,
                self.m2,
                self.pn_order,
                self.include_radiation_reaction,
                self.spins,
            )
            a2 = -a1

            self.v1 += a1 * self.dt
            self.v2 += a2 * self.dt

            self.r1 += self.v1 * self.dt
            self.r2 += self.v2 * self.dt

            self.r1_array[i] = self.r1
            self.r2_array[i] = self.r2
            self.v1_array[i] = self.v1
            self.v2_array[i] = self.v2

    def save_data(self, filename):
        data = np.column_stack(
            (self.t_array, self.r1_array, self.r2_array, self.v1_array, self.v2_array)
        )
        np.savetxt(filename, data, header="t x1 y1 z1 x2 y2 z2 vx1 vy1 vz1 vx2 vy2 vz2")

    def load_data(self, filename):
        data = np.loadtxt(filename)
        self.t_array = data[:, 0]
        self.r1_array = data[:, 1:4]
        self.r2_array = data[:, 4:7]
        self.v1_array = data[:, 7:10]
        self.v2_array = data[:, 10:13]
