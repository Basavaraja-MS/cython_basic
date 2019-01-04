Installation and Running guidelines of Cadence PCIe Application Level Stress test tool 

Pre-Requisites
--------------
Cython
* sudo apt-get install build-essential
* sudo apt install python-pip3
* pip3 install Cython
PyQt5
* sudo apt-get install python3-pyqt5  pyqt5-dev-tools qttools5-dev-tool

Running the test cases
----------------------
GUI
* make gui
* Opens a GUI window and Log display window
CLI
* make cli
* Runns all the test cases implimented and with all the monitoring logics implimented 
* Log file found under output/testresults.txt
* TIP: To watch realtime logs use tail -f output/testresults.txt
clean
* make clean 

Project structure
-----------------
* gui/
    - pcie_gui.py: 
          Main GUI window source file
    - pcie_log.py: 
          Log GUI window source file and also contains log framework      
* lib/
    - Core files intract with OS specific driver files, whihc generates libpci.so library 
* pyc/
    - pcipy.pyx: 
          Cython source file which will invoke pci class, read* and write* functions from lib libarray files 
    - pcipy_h.pxd:
          Cython header file, This file is used to instantiate C structures and functions from lib files
    - pciheader.py:
          Acts same as c header files in python 
     - common.py:
          Implimented all the test cases and make cli will call these functions 
* Makefile
    - Main make file for invocation of GUI or CLI mode of running and compilation of test cases
* Makefile.lib
    - This submake file is implimented for compilation of C files which are in "lib" and generates libpci.so librrary file
* README.md
    - This file

