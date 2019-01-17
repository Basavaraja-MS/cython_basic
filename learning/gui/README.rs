Install PyQt5 on linux system 

* Make sure you running pyhton 3.x you can check it by running python -v
* if not intalll python 3 by brew install python3
* If already installed make it default python by writing alias python=python3   in .bashrc file

* Run below commands to install PyQt5
 
sudo apt-get install python3-pyqt5  
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools

Run this command to open GUI viewer

qtchooser -run-tool=designer -qt=5

