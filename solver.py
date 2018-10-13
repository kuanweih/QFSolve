import numpy as np


N_1D = 20    # number of grids on a side
ETA = 1.    # mass/hbar: particle mass over Planck const.
BOXSIZE = 1.    # simulation box size
CFL = 1.   # Caurant constrain for a time step


# 1D perturbation wave
rho_0 = 1.
rho_1 = 1e-4
k = 2. * np.pi
phi_0 = 0.
v_0 = 1.
v_1 = np.pi * 1e-4

print(np.linspace(0,BOXSIZE,num=N_1D))

# fluid_ic = [[],
#             []]    # ic arrays
#
#
# dh = BOXSIZE / N_1D    # grid size
# dts = ETA * dh**2     # time step for Schrodinger
# dtf = dh / vmax    # time step for fluid dynamics
# dt = CFL / (1. / dts + 1. / dtf)
#
# fluid
