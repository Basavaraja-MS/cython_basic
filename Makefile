#Make file for building cython binaries 

all: local

local:
	@echo "Compiling Cython module"
	python setup.py build_ext --inplace


clean:
	@echo "Cleaning files"
	rm -f *.so  *.a *.o 
	rm -f call_mymath.c
	rm -rf build/
