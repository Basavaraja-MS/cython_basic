# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PCIeApplicationStressTest(object):
    def setupUi(self, PCIeApplicationStressTest):
        PCIeApplicationStressTest.setObjectName("PCIeApplicationStressTest")
        PCIeApplicationStressTest.resize(509, 361)
        PCIeApplicationStressTest.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(218, 218, 218);\n"
"background-color: rgb(227, 227, 227);")
        self.lineEdit = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(PCIeApplicationStressTest)
        self.progressBar.setGeometry(QtCore.QRect(390, 340, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 30, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 61, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton.setGeometry(QtCore.QRect(400, 30, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(PCIeApplicationStressTest)
        self.listView.setGeometry(QtCore.QRect(30, 121, 391, 191))
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        self.checkBox = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox.setGeometry(QtCore.QRect(40, 160, 91, 25))
        self.checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 190, 81, 20))
        self.checkBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 220, 91, 20))
        self.checkBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_4.setGeometry(QtCore.QRect(40, 250, 101, 20))
        self.checkBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_5.setGeometry(QtCore.QRect(40, 280, 101, 20))
        self.checkBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_5.setObjectName("checkBox_5")
        self.spinBox = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox.setGeometry(QtCore.QRect(160, 160, 31, 16))
        self.spinBox.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 190, 31, 16))
        self.spinBox_2.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_3.setGeometry(QtCore.QRect(160, 220, 31, 16))
        self.spinBox_3.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_4.setGeometry(QtCore.QRect(160, 250, 31, 16))
        self.spinBox_4.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_5.setGeometry(QtCore.QRect(160, 280, 31, 16))
        self.spinBox_5.setStyleSheet("alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_5.setObjectName("spinBox_5")
        self.verticalScrollBar = QtWidgets.QScrollBar(PCIeApplicationStressTest)
        self.verticalScrollBar.setGeometry(QtCore.QRect(400, 140, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 71, 16))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_4.setGeometry(QtCore.QRect(160, 130, 35, 10))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 160, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 190, 56, 17))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 220, 56, 17))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 250, 56, 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 280, 56, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 280, 56, 17))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 220, 56, 17))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 190, 56, 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 160, 56, 17))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_11.setGeometry(QtCore.QRect(280, 250, 56, 17))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 100, 56, 17))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 100, 56, 17))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_5 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_5.setGeometry(QtCore.QRect(350, 130, 35, 10))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_6.setGeometry(QtCore.QRect(360, 160, 35, 16))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_7.setGeometry(QtCore.QRect(360, 190, 35, 10))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_8.setGeometry(QtCore.QRect(360, 220, 35, 10))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_9.setGeometry(QtCore.QRect(360, 250, 35, 10))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_10.setGeometry(QtCore.QRect(360, 280, 35, 10))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(PCIeApplicationStressTest)
        QtCore.QMetaObject.connectSlotsByName(PCIeApplicationStressTest)

    def retranslateUi(self, PCIeApplicationStressTest):
        _translate = QtCore.QCoreApplication.translate
        PCIeApplicationStressTest.setWindowTitle(_translate("PCIeApplicationStressTest", "Cadence PCIe Application Stress Test"))
        self.label.setText(_translate("PCIeApplicationStressTest", "Enter Device ID "))
        self.label_2.setText(_translate("PCIeApplicationStressTest", "Enter Vendor ID "))
        self.pushButton.setText(_translate("PCIeApplicationStressTest", "OK"))
        self.checkBox.setText(_translate("PCIeApplicationStressTest", "Link Down Test"))
        self.checkBox_2.setText(_translate("PCIeApplicationStressTest", "Link Retrain Test"))
        self.checkBox_3.setText(_translate("PCIeApplicationStressTest", "Link Equalization Test"))
        self.checkBox_4.setText(_translate("PCIeApplicationStressTest", "PCI Power Down Test"))
        self.checkBox_5.setText(_translate("PCIeApplicationStressTest", "ASPM Power Down Test"))
        self.label_3.setText(_translate("PCIeApplicationStressTest", "Test Name"))
        self.label_4.setText(_translate("PCIeApplicationStressTest", "Count"))
        self.pushButton_2.setText(_translate("PCIeApplicationStressTest", "Run Test"))
        self.pushButton_3.setText(_translate("PCIeApplicationStressTest", "Run Test"))
        self.pushButton_4.setText(_translate("PCIeApplicationStressTest", "Run Test"))
        self.pushButton_5.setText(_translate("PCIeApplicationStressTest", "Run Test"))
        self.pushButton_6.setText(_translate("PCIeApplicationStressTest", "Run Test"))
        self.pushButton_7.setText(_translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_8.setText(_translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_9.setText(_translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_10.setText(_translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_11.setText(_translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_12.setText(_translate("PCIeApplicationStressTest", "Run All "))
        self.pushButton_13.setText(_translate("PCIeApplicationStressTest", "Stop"))
        self.label_5.setText(_translate("PCIeApplicationStressTest", "Status"))
        self.label_6.setText(_translate("PCIeApplicationStressTest", "Idle"))
        self.label_7.setText(_translate("PCIeApplicationStressTest", "Idle"))
        self.label_8.setText(_translate("PCIeApplicationStressTest", "Idle"))
        self.label_9.setText(_translate("PCIeApplicationStressTest", "Idle"))
        self.label_10.setText(_translate("PCIeApplicationStressTest", "Idle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PCIeApplicationStressTest = QtWidgets.QDialog()
    ui = Ui_PCIeApplicationStressTest()
    ui.setupUi(PCIeApplicationStressTest)
    PCIeApplicationStressTest.show()
    sys.exit(app.exec_())
