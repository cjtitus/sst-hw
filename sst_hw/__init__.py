import os
from pkg_resources import get_distribution, DistributionNotFound

"""
Style imitated shamelessly from qtpy: https://github.com/spyder-ide/qtpy/blob/master/qtpy/__init__.py
"""

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
   # package is not installed
   pass

SST_API = "SST_HW"

REAL_API = ["real"]
SIM_API = ["sim"]

binding_specified = SST_API in os.environ

os.environ.setdefault(SST_API, 'real')
API = os.environ[SST_API].lower()

initial_api = API
assert API in (REAL_API + SIM_API)

REAL = True
SIM = False

if API in REAL_API:
    try:
        from sst_hw_real import __version__ as REAL_HW_VERSION
    except ImportError:
        API = os.environ[SST_API] = 'sim'

if API in SIM_API:
    try:
        from sst_hw_sim import __version__ as SIM_HW_VERSION
        REAL = False
        SIM = True
    except ImportError:
        raise RuntimeError("No SST HW packages found")
