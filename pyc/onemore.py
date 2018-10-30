#!/usr/bin/env python3

import common as ptest

test_param_dict = {
    "pcipm_test": True,
    "aspm_test": True,
    "test_count": 10,
    "aer_chk": False,
    "dll_active_chk": False,
    "print_only": False,
    "d1": False,
    "d2": False,
    "id": True,
    "max_aspm": 1
    }


ptest.main_test_fun(test_param_dict)
