from __future__ import absolute_import, print_function

import os
import sys

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import os

# For demo purposes, we build our own tiny library.
"""
try:
    print("building libmymath.a")
    assert os.system("gcc -shared -fPIC -c mymath.c -o mymath.o") == 0
    assert os.system("ar rcs libmymath.a mymath.o") == 0
except:
    if not os.path.exists("libmymath.a"):
        print("Error building external library, please create libmymath.a manually.")
        sys.exit(1)
"""
# Here is how to use the library built above.
ext_modules = cythonize([
    Extension("pcipy",
              sources=["pcipy.pyx"],
              #include_dirs=[os.getcwd(), "$(SRC_PATH)/lib"],  # path to .h file(s)
              #library_dirs=[os.getcwd(), "$(SRC_PATH)/lib"],  # path to .a or .so file(s)
              include_dirs=[os.getcwd(), os.path.join(os.getcwd(), "../lib")],  # path to .h file(s)
              library_dirs=[os.getcwd(), os.path.join(os.getcwd(), "../lib")],  # path to .a or .so file(s)
              libraries=['pci'])
], gdb_debug=True)

setup(
    name='cdns_pcipy',
    ext_modules=ext_modules,
)
