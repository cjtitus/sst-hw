import os

"""
Style imitated shamelessly from qtpy: https://github.com/spyder-ide/qtpy/blob/master/qtpy/__init__.py
"""
SST_API = "SST_HW"

REAL_API = ["real"]
SIM_API = ["sim"]

binding_specified = SST_API in os.environ

os.environ.setdefault(SST_API, 'real')

initial_api = API
assert API in (REAL_API + SIM_API)

if API in REAL_API:
    try:
        from sst_hw_real import __version__ as REAL_HW_VERSION
    except ImportError:
        API = os.environ[SST_API] = 'sim'

if API in SIM_API:
    try:
        from sst_hw_sim import __version__ as SIM_HW_VERSION
    except ImportError:
        raise RuntimeError("No SST HW packages found")
