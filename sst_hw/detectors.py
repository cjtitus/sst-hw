from . import REAL, SIM

if REAL:
    from sst_hw_real.detectors import *
elif SIM:
    from sst_hw_sim.detectors import *
