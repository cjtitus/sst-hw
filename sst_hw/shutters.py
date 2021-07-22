from . import REAL_API, SIM_API

if REAL_API:
    from sst_hw_real.shutters import *
elif SIM_API:
    from sst_hw_sim.shutters import *
