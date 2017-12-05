#Make file for building cython binaries 

SRC_PATH := $(PWD)

all: local

local:
	@echo "Compiling Cython module"
	make -f Makefile.lib
	cd pyc && python setup.py build_ext --inplace && cd -


clean:
	@echo "Cleaning files"
	make -f Makefile.lib clean 
	rm -f pyc/*.so  pyc/*.a pyc/*.o 
	rm -f pyc/pcipy.c
	rm -rf build/
