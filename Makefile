#Make file for building cython binaries 

SRC_PATH := $(PWD)

all: local cli

gui: local gui
	cd pyc && python3 pcie_gui.py && cd -

local:
	@echo "Compiling Cython module"
	make -f Makefilelib
	cd pyc && python3 setup.py build_ext --inplace && cd -

cli:
	cd pyc && python3 cli.py && cd -
	#cd pyc && python3 common.py && cd -

clean:
	@echo "Cleaning files"
	make -f Makefilelib clean 
	rm -f pyc/*.so  pyc/*.a pyc/*.o pyc/*.pyc
	rm -f pyc/pcipy.c
	rm -rf build/

