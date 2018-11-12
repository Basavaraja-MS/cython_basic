# cython_basic

This is the basic examples of using cython for c libraries 

There are basically 3 files exists,
* math.h and math.c files are source files of c program
still dont know any limitation hence i will use all the c
files in these modules

* call_mymath.pyx is cython specific file, all the functions
are redefined according to the cython need 

* there is one more .pxd file is needed which act as header
file for .pyx files. We will discuss it on bigger projects

* setup.py is the configuration file, whihc create the environ
-ment for compilation of .C/.h files and .pyx/.pyd files 


Compilation:

To compile above files is has to be done by
	python setup.py build_ext --inplace

which generates, call_mymath.c, call_mymath.so, mymath.o and libmymath.a
files alog with build directory which contians temp.linux-x86_64-2.7 dir
and contains call_mymath.o  

Installation tips:
Should install devutilites
Machine should have git tool
git clone form the given url
install pip3 by sudo apt install python-pip3
pip install Cython
https://cython.readthedocs.io/en/latest/src/quickstart/install.html
https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3

Installation and desktop entry -
https://stackoverflow.com/questions/36757752/how-to-install-pyqt5-in-python-3-ubuntu-14-04


