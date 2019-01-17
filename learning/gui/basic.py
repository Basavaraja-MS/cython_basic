# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PCIeStressTest0.1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_PCIeStressTestApplication(object):

    def read_device_name(self):
        print("Read the data for vendorid")
        device_id = self.lineEdit.text()
        print (device_id)
        self.label_2.setText("Selected Device ID for test:" +device_id)
        return device_id

    def setupUi(self, PCIeStressTestApplication):
        PCIeStressTestApplication.setObjectName("PCIeStressTestApplication")
        PCIeStressTestApplication.resize(480, 640)
        PCIeStressTestApplication.setAcceptDrops(False)
        self.lineEdit = QtWidgets.QLineEdit(PCIeStressTestApplication)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(PCIeStressTestApplication)
        self.label.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(PCIeStressTestApplication)
        self.pushButton.setGeometry(QtCore.QRect(300, 100, 51, 21))
        self.pushButton.clicked.connect(self.read_device_name)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PCIeStressTestApplication)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 380, 91, 31))
        font = QtGui.QFont() 
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(PCIeStressTestApplication)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 371, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PCIeStressTestApplication)
        self.label_3.setGeometry(QtCore.QRect(40, 450, 371, 51))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(PCIeStressTestApplication)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(PCIeStressTestApplication)
        self.progressBar.setGeometry(QtCore.QRect(360, 610, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(PCIeStressTestApplication)
        self.label_4.setGeometry(QtCore.QRect(280, 610, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(PCIeStressTestApplication)
        QtCore.QMetaObject.connectSlotsByName(PCIeStressTestApplication)

    def retranslateUi(self, PCIeStressTestApplication):
        _translate = QtCore.QCoreApplication.translate
        PCIeStressTestApplication.setWindowTitle(_translate("PCIeStressTestApplication", "PCIeStressTestApplication"))
        self.label.setText(_translate("PCIeStressTestApplication", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter Device ID </span></p></body></html>"))
        self.pushButton.setText(_translate("PCIeStressTestApplication", "Enter"))
        self.pushButton_2.setText(_translate("PCIeStressTestApplication", "Start Test"))
        self.pushButton_3.setText(_translate("PCIeStressTestApplication", "Stop Test"))
        self.label_4.setText(_translate("PCIeStressTestApplication", "Progress"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_PCIeStressTestApplication()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

