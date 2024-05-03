# -*- coding: utf-8 -*-
"""
cyipopt: Python wrapper for the Ipopt optimization package, written in Cython.

Copyright (C) 2012-2015 Amit Aides
Copyright (C) 2015-2017 Matthias Kümmerer
Copyright (C) 2017-2024 cyipopt developers

License: EPL 2.0
"""

import sys
if sys.platform == 'win32':
    import os
    extra_dll_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')  
    if os.path.isdir(extra_dll_dir):  
        os.add_dll_directory(extra_dll_dir)

from ipopt_wrapper import *
from .ipopt_wrapper import *
from .scipy_interface import *
from .version import __version__
from .exceptions import *
