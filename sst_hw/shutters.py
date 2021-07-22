from . import REAL, SIM

if REAL:
    from sst_hw_real.shutters import *
elif SIM:
    from sst_hw_sim.shutters import *
