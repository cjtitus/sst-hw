from . import REAL, SIM

if REAL:
    from sst_hw_real.motors import *
elif SIM:
    from sst_hw_sim.motors import *
