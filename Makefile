#Make file for building cython binaries 

SRC_PATH := $(PWD)

all: local test

local:
	@echo "Compiling Cython module"
	make -f Makefile.lib
	cd pyc && python3 setup.py build_ext --inplace && cd -

test:
	#cd pyc && python -c "import pcipy" && cd -
	#cp lib/libpci.so.3.1.4 lib/libpci.so
	cd pyc && python3 pcie_gui.py


clean:
	@echo "Cleaning files"
	make -f Makefile.lib clean 
	rm -f pyc/*.so  pyc/*.a pyc/*.o pyc/*.pyc
	rm -f pyc/pcipy.c
	rm -rf build/
