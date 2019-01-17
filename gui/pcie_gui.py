#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import common as ptest
from pcie_log import *
import threading
import time


class Ui_PCIeApplicationStressTest(object):
    lnkdwntest_run = False
    pmtest_run = False
    aspmtest_run = False
    lnkrettest_run = False
    linkequtest_run = False

    def __init__(self):
        self.test_param = {
            "link_disable_test": False,
            "link_disable_test_count": 10,
            "link_down_stat": False,

            "link_ret_test": False,
            "link_ret_test_count": 10,
            "link_ret_stat": False,

            "link_equ_test": False,
            "link_equ_test_count": 10,
            "link_equ_stat": False,

            "aspm_test": False,
            "aspm_test_count": 10,
            "aspm_test_stat": False,

            "pcipm_test": False,
            "pcipm_test_count": 10,
            "pcipm_test_stat": False,

            "id": True,
            "aer_chk": False,
            "dll_active_chk": True,
            "d1": False,
            "d2": False,
            "print_only": False,
            "max_aspm": 1,

            "segrp": 0,
            "busrp": 0,
            "devrp": 1,
            "funrp":  0,

            "segep": 0,
            "busep": 1,
            "devep": 0,
            "funep": 0,
        }

    def setupUi(self, PCIeApplicationStressTest):
        PCIeApplicationStressTest.setObjectName("PCIeApplicationStressTest")
        PCIeApplicationStressTest.resize(509, 361)
        PCIeApplicationStressTest.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                                "background-color: rgb(218, 218, 218);\n"
                                                "background-color: rgb(227, 227, 227);")
        self.progressBar = QtWidgets.QProgressBar(PCIeApplicationStressTest)
        self.progressBar.setGeometry(QtCore.QRect(390, 340, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_funcEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_funcEP.setGeometry(QtCore.QRect(362, 60, 51, 20))
        self.lineEdit_funcEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_funcEP.setText("0")
        self.lineEdit_funcEP.setObjectName("lineEdit_funcEP")
        self.label_2 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 31, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_EPok = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_EPok.setGeometry(QtCore.QRect(430, 60, 56, 17))
        self.pushButton_EPok.setObjectName("pushButton_EPok")
        def bdf_ep_ok():
            self.test_param["segep"] = self.lineEdit_segEP.text()
            self.test_param["busep"] = self.lineEdit_busEP.text()
            self.test_param["devep"] = self.lineEdit_devEP.text()
            self.test_param["funcep"] = self.lineEdit_funcEP.text()
            #print(self.test_param["segep"], self.test_param["busep"], self.test_param["devep"], self.test_param["funcep"])
        self.pushButton_EPok.clicked.connect(bdf_ep_ok)
        self.listView = QtWidgets.QListView(PCIeApplicationStressTest)
        self.listView.setGeometry(QtCore.QRect(20, 121, 421, 191))
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        self.checkBox_LnkDwn = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_LnkDwn.setGeometry(QtCore.QRect(40, 160, 91, 25))
        self.checkBox_LnkDwn.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_LnkDwn.setObjectName("checkBox_LnkDwn")
        self.checkBox_LnkRetrain = QtWidgets.QCheckBox(
            PCIeApplicationStressTest)
        self.checkBox_LnkRetrain.setGeometry(QtCore.QRect(40, 190, 81, 20))
        self.checkBox_LnkRetrain.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_LnkRetrain.setObjectName("checkBox_LnkRetrain")
        self.checkBox_LinkEqua = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_LinkEqua.setGeometry(QtCore.QRect(40, 220, 91, 20))
        self.checkBox_LinkEqua.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_LinkEqua.setObjectName("checkBox_LinkEqua")
        self.checkBox_PM = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_PM.setGeometry(QtCore.QRect(40, 250, 101, 20))
        self.checkBox_PM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_PM.setObjectName("checkBox_PM")
        self.checkBox_aspm = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_aspm.setGeometry(QtCore.QRect(40, 280, 101, 20))
        self.checkBox_aspm.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_aspm.setObjectName("checkBox_aspm")
        self.spinBox_LinkDwn = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_LinkDwn.setGeometry(QtCore.QRect(160, 160, 41, 16))
        self.spinBox_LinkDwn.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_LinkDwn.setMinimum(10)
        self.spinBox_LinkDwn.setMaximum(10000)
        self.spinBox_LinkDwn.setObjectName("spinBox_LinkDwn")
        self.spinBox_LnkRet = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_LnkRet.setGeometry(QtCore.QRect(160, 190, 41, 16))
        self.spinBox_LnkRet.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_LnkRet.setMinimum(10)
        self.spinBox_LnkRet.setMaximum(1000)
        self.spinBox_LnkRet.setObjectName("spinBox_LnkRet")
        self.spinBox_LnkEqu = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_LnkEqu.setGeometry(QtCore.QRect(160, 220, 41, 16))
        self.spinBox_LnkEqu.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_LnkEqu.setMinimum(10)
        self.spinBox_LnkEqu.setMaximum(1000)
        self.spinBox_LnkEqu.setObjectName("spinBox_LnkEqu")
        self.spinBox_pm = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_pm.setGeometry(QtCore.QRect(160, 250, 41, 16))
        self.spinBox_pm.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_pm.setMinimum(10)
        self.spinBox_pm.setMaximum(1000)
        self.spinBox_pm.setObjectName("spinBox_pm")
        self.spinBox_aspm = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_aspm.setGeometry(QtCore.QRect(160, 280, 41, 16))
        self.spinBox_aspm.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_aspm.setMinimum(10)
        self.spinBox_aspm.setMaximum(1000)
        self.spinBox_aspm.setObjectName("spinBox_aspm")
        self.verticalScrollBar = QtWidgets.QScrollBar(
            PCIeApplicationStressTest)
        self.verticalScrollBar.setGeometry(QtCore.QRect(400, 140, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 81, 16))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_4.setGeometry(QtCore.QRect(150, 130, 51, 16))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_LnkDwn = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkDwn.setGeometry(QtCore.QRect(220, 160, 56, 17))
        self.pushButton_LnkDwn.setObjectName("pushButton_LnkDwn")
        def lnk_dwn_test():
            if self.checkBox_LnkDwn.isChecked() == True and self.lnkdwntest_run == False:
                self.test_param["link_disable_test"] = True
                self.test_param["lnkdwntest_count"] = self.spinBox_LinkDwn.value()
                self.label_LnkDwn.setText("Run")
                self.lnkdwntest_run = True
                logging.info("Run Link down test count %d", self.test_param["lnkdwntest_count"])
                test(self.test_param)
                prbar(self, self.test_param)
            else:
                logging.info("Dont Run Link down test")
        self.pushButton_LnkDwn.clicked.connect(lnk_dwn_test)
        self.pushButton_LnkRet = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkRet.setGeometry(QtCore.QRect(220, 190, 56, 17))
        self.pushButton_LnkRet.setObjectName("pushButton_LnkRet")
        def link_ret_test():
            if self.checkBox_LnkRetrain.isChecked() == True and self.lnkrettest_run == False:
                self.test_param["link_ret_test"] = True
                self.test_param["link_ret_test_count"] = self.spinBox_LnkRet.value()
                self.label_LnkRet.setText("Run")
                self.lnkrettest_run = True
                self.label_LnkRet.repaint() #For displaying Run
                logging.info("Run Link retrain test count %d", self.test_param["link_ret_test_count"])
                #test(self.test_param)
                prbar(self, self.test_param)
                link_ret_test_stp()
            else:
                logging.info("Dont Run Link retrain test")
        self.pushButton_LnkRet.clicked.connect(link_ret_test)
        self.pushButton_LnkEq = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkEq.setGeometry(QtCore.QRect(220, 220, 56, 17))
        self.pushButton_LnkEq.setObjectName("pushButton_LnkEq")
        def link_equ_test():
            if self.checkBox_LinkEqua.isChecked() == True and self.linkequtest_run == False:
                self.test_param["link_equ_test"] = True
                self.test_param["link_equ_test_count"] = self.spinBox_LnkEqu.value()
                self.label_LnkEqu.setText("Run")
                self.linkequtest_run = True
                logging.info("Run Link Equalization count %d", self.test_param["link_equ_test_count"])
                test(self.test_param)
            else:
                logging.info("Dont Run Link Equalization test")
        self.pushButton_LnkEq.clicked.connect(link_equ_test)
        self.pushButton_PM = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_PM.setGeometry(QtCore.QRect(220, 250, 56, 17))
        self.pushButton_PM.setObjectName("pushButton_PM")
        def pcipm_test():
            if self.checkBox_PM.isChecked() == True and self.pmtest_run == False:
                self.test_param["pcipm_test"] = True
                self.test_param["pcipm_test_count"] = self.spinBox_pm.value()
                self.label_pm.setText("Run")
                self.pmtest_run = True
                logging.info("PM test count %d", self.test_param["pcipm_test_count"])
                test(self.test_param)
            else:
                logging.info("Dont Run PM test")
        self.pushButton_PM.clicked.connect(pcipm_test)
        self.pushButton_aspm = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_aspm.setGeometry(QtCore.QRect(220, 280, 56, 17))
        self.pushButton_aspm.setObjectName("pushButton_aspm")
        self.pushButton_aspmstp = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_aspmstp.setGeometry(QtCore.QRect(280, 280, 56, 17))
        self.pushButton_aspmstp.setObjectName("pushButton_aspmstp")
        def aspm_test_stp():
            if self.checkBox_aspm.isChecked() == True and self.aspmtest_run == True:
                self.label_aspm.setText("Idle")
                self.aspmtest_run = False
                self.test_param["aspm_test"] = False
                logging.info("stop aspm test count")
            else:
                logging.info("Dont stop aspm test")
        self.pushButton_aspmstp.clicked.connect(aspm_test_stp)
        self.pushButton_LnkStop = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkStop.setGeometry(QtCore.QRect(280, 220, 56, 17))
        self.pushButton_LnkStop.setObjectName("pushButton_LnkStop")
        def link_equ_test_stp():
            if self.checkBox_LinkEqua.isChecked() == True and self.linkequtest_run == True:
                self.label_LnkEqu.setText("Idle")
                self.linkequtest_run = False
                self.test_param["link_equ_test"] = False
                logging.info("stop Link Equ test")
            else:
                logging.info("Dont stop Link Equ test")
        self.pushButton_LnkStop.clicked.connect(link_equ_test_stp)
        self.pushButton_LnkRetStop = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkRetStop.setGeometry(QtCore.QRect(280, 190, 56, 17))
        self.pushButton_LnkRetStop.setObjectName("pushButton_LnkRetStop")
        def link_ret_test_stp():
            if self.checkBox_LnkRetrain.isChecked() == True and self.lnkrettest_run == True:
                self.label_LnkRet.setText("Idle")
                self.lnkrettest_run = False
                self.test_param["link_ret_test"] = False
                logging.info("stop lnk retrain test count")
            else:
                logging.info("Dont stop lnk retrain test")
        self.pushButton_LnkRetStop.clicked.connect(link_ret_test_stp)
        self.pushButton_LnkDwn_stop2 = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkDwn_stop2.setGeometry(
            QtCore.QRect(280, 160, 56, 17))
        self.pushButton_LnkDwn_stop2.setObjectName("pushButton_LnkDwn_stop2")
        def link_disable_test_stp():
            if self.checkBox_LnkDwn.isChecked() == True and self.lnkdwntest_run == True:
                self.label_LnkDwn.setText("Idle")
                self.lnkdwntest_run = False
                self.test_param["link_down_stat"] = False
                self.test_param["link_disable_test"] = False
                logging.info("Stop Link down")
            else:
                logging.info("Dont stop test")
        self.pushButton_LnkDwn_stop2.clicked.connect(link_disable_test_stp)
        self.pushButton_PMStp = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_PMStp.setGeometry(QtCore.QRect(280, 250, 56, 17))
        self.pushButton_PMStp.setObjectName("pushButton_PMStp")
        def pm_test_stp():
            if self.checkBox_PM.isChecked() == True and self.pmtest_run == True:
                self.label_pm.setText("Idle")
                self.pmtest_run = False
                self.test_param["pcipm_test"] = False
                logging.info("Stop pm test")
            else:
                logging.info("Dont stop test")
        self.pushButton_PMStp.clicked.connect(pm_test_stp)
        #self.pushButton_PMStp = QtWidgets.QPushButton(PCIeApplicationStressTest)
        #self.pushButton_PMStp.setGeometry(QtCore.QRect(280, 250, 56, 17))
        self.pushButton_RunAll = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_RunAll.setGeometry(QtCore.QRect(290, 100, 56, 17))
        self.pushButton_RunAll.setObjectName("pushButton_RunAll")
        def run_all_tests():
            if False in {self.lnkdwntest_run, self.pmtest_run,
                                self.aspmtest_run, self.lnkrettest_run, self.linkequtest_run}:
                self.checkBox_PM.setChecked(True)
                self.checkBox_LinkEqua.setChecked(True)
                self.checkBox_aspm.setChecked(True)
                self.checkBox_LnkRetrain.setChecked(True)
                self.checkBox_LnkDwn.setChecked(True)

                self.lnkdwntest_run = True
                self.pmtest_run = True
                self.aspmtest_run = True
                self.lnkrettest_run = True
                self.linkequtest_run = True

                self.test_param["link_disable_test"] = True
                self.test_param["link_ret_test"] = True
                self.test_param["link_equ_test"] = True
                self.test_param["aspm_test"] = True
                self.test_param["pcipm_test"] = True

                self.test_param["pcipm_test_count"] = self.spinBox_pm.value()
                self.test_param["link_ret_test_count"] = self.spinBox_LnkRet.value()
                self.test_param["link_equ_test_count"] = self.spinBox_LnkEqu.value()
                self.test_param["aspm_test_count"] = self.spinBox_aspm.value()
                self.test_param["link_disable_test_count"] = self.spinBox_LinkDwn.value()
                logging.info("All tests are run ")
                test(self.test_param)
            else:
                logging.info("Dont Run PM test")
        self.pushButton_RunAll.clicked.connect(run_all_tests)
        self.pushButton_StopAll = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_StopAll.setGeometry(QtCore.QRect(360, 100, 56, 17))
        self.pushButton_StopAll.setObjectName("pushButton_StopAll")
        self.label_5 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_5.setGeometry(QtCore.QRect(350, 130, 51, 20))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_LnkDwn = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_LnkDwn.setGeometry(QtCore.QRect(360, 160, 35, 16))
        self.label_LnkDwn.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_LnkDwn.setObjectName("label_LnkDwn")
        self.label_LnkRet = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_LnkRet.setGeometry(QtCore.QRect(360, 190, 35, 10))
        self.label_LnkRet.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_LnkRet.setObjectName("label_LnkRet")
        self.label_LnkEqu = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_LnkEqu.setGeometry(QtCore.QRect(360, 220, 35, 10))
        self.label_LnkEqu.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_LnkEqu.setObjectName("label_LnkEqu")
        self.label_pm = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_pm.setGeometry(QtCore.QRect(360, 250, 35, 10))
        self.label_pm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pm.setObjectName("label_pm")
        self.label_aspm = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_aspm.setGeometry(QtCore.QRect(360, 280, 35, 10))
        self.label_aspm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_aspm.setObjectName("label_aspm")
        def aspm_test():
            if self.checkBox_aspm.isChecked() == True and self.aspmtest_run == False:
                self.test_param["aspm_test"] = True
                self.test_param["aspm_test_count"] = self.spinBox_aspm.value()
                self.label_aspm.setText("Run")
                self.aspmtest_run = True
                logging.info("Run aspm test count %d", self.test_param["aspm_test_count"])
                test(self.test_param)
            else:
                logging.info("Dont Run Link down test")
        self.pushButton_aspm.clicked.connect(aspm_test)
        self.lineEdit_devEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_devEP.setGeometry(QtCore.QRect(262, 60, 51, 20))
        self.lineEdit_devEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_devEP.setText("0")
        self.lineEdit_devEP.setObjectName("lineEdit_devEP")
        self.label_11 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_11.setGeometry(QtCore.QRect(220, 60, 31, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_busEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_busEP.setGeometry(QtCore.QRect(162, 60, 51, 20))
        self.lineEdit_busEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_busEP.setText("1")
        self.lineEdit_busEP.setObjectName("lineEdit_busEP")
        self.label_12 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_12.setGeometry(QtCore.QRect(120, 60, 31, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_segEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_segEP.setGeometry(QtCore.QRect(62, 60, 51, 20))
        self.lineEdit_segEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_segEP.setText("0")
        self.lineEdit_segEP.setObjectName("lineEdit_segEP")
        self.label_13 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_busRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_busRP.setGeometry(QtCore.QRect(162, 20, 51, 20))
        self.lineEdit_busRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_busRP.setText("0")
        self.lineEdit_busRP.setObjectName("lineEdit_busRP")
        self.pushButton_RPok = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_RPok.setGeometry(QtCore.QRect(430, 20, 56, 17))
        self.pushButton_RPok.setObjectName("pushButton_RPok")
        def bdf_rp_ok():
            self.test_param["segrp"] = self.lineEdit_segRP.text()
            self.test_param["busrp"] = self.lineEdit_busRP.text()
            self.test_param["devrp"] = self.lineEdit_devRP.text()
            self.test_param["funrp"] = self.lineEdit_funcRP.text()
            #logging.info(self.test_param["segrp"], self.test_param["busrp"], self.test_param["devrp"], self.test_param["funrp"])
        self.pushButton_RPok.clicked.connect(bdf_rp_ok)
        self.lineEdit_funcRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_funcRP.setGeometry(QtCore.QRect(362, 20, 51, 20))
        self.lineEdit_funcRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_funcRP.setText("0")
        self.lineEdit_funcRP.setObjectName("lineEdit_funcRP")
        self.label_15 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_15.setGeometry(QtCore.QRect(220, 20, 31, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_segRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_segRP.setGeometry(QtCore.QRect(62, 20, 51, 20))
        self.lineEdit_segRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_segRP.setText("0")
        self.lineEdit_segRP.setObjectName("lineEdit_segRP")
        self.label_16 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_16.setGeometry(QtCore.QRect(320, 20, 31, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_devRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_devRP.setGeometry(QtCore.QRect(262, 20, 51, 20))
        self.lineEdit_devRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_devRP.setText("1")
        self.lineEdit_devRP.setObjectName("lineEdit_devRP")
        self.label_17 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_17.setGeometry(QtCore.QRect(120, 20, 31, 16))
        self.label_17.setObjectName("label_17")
        self.retranslateUi(PCIeApplicationStressTest)
        QtCore.QMetaObject.connectSlotsByName(PCIeApplicationStressTest)

    def retranslateUi(self, PCIeApplicationStressTest):
        _translate = QtCore.QCoreApplication.translate
        PCIeApplicationStressTest.setWindowTitle(_translate(
            "PCIeApplicationStressTest", "Cadence PCIe Application Stress Test"))
        self.label_2.setText(_translate("PCIeApplicationStressTest", "Func "))
        self.pushButton_EPok.setText(
            _translate("PCIeApplicationStressTest", "OK"))
        self.checkBox_LnkDwn.setText(_translate(
            "PCIeApplicationStressTest", "Link Down Test"))
        self.checkBox_LnkRetrain.setText(_translate(
            "PCIeApplicationStressTest", "Link Retrain Test"))
        self.checkBox_LinkEqua.setText(_translate(
            "PCIeApplicationStressTest", "Link Equalization Test"))
        self.checkBox_PM.setText(_translate(
            "PCIeApplicationStressTest", "PCI Power Down Test"))
        self.checkBox_aspm.setText(_translate(
            "PCIeApplicationStressTest", "ASPM Power Down Test"))
        self.label_3.setText(_translate(
            "PCIeApplicationStressTest", "Test Name"))
        self.label_4.setText(_translate("PCIeApplicationStressTest", "Count"))
        self.pushButton_LnkDwn.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_LnkRet.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_LnkEq.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_PM.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_aspm.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_aspmstp.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_LnkStop.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_LnkRetStop.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_LnkDwn_stop2.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_PMStp.setText(_translate(
            "PCIeApplicationStressTest", "Stop"))
        self.pushButton_RunAll.setText(_translate(
            "PCIeApplicationStressTest", "Run All "))
        self.pushButton_StopAll.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.label_5.setText(_translate("PCIeApplicationStressTest", "Status"))
        self.label_LnkDwn.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_LnkRet.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_LnkEqu.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_pm.setText(_translate("PCIeApplicationStressTest", "Idle"))
        self.label_aspm.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_11.setText(_translate("PCIeApplicationStressTest", "Dev"))
        self.label_12.setText(_translate("PCIeApplicationStressTest", "Bus"))
        self.label_13.setText(_translate("PCIeApplicationStressTest", "EP-Seg"))
        self.label_14.setText(_translate("PCIeApplicationStressTest", "RP-Seg"))
        self.pushButton_RPok.setText(
            _translate("PCIeApplicationStressTest", "OK"))
        self.label_15.setText(_translate("PCIeApplicationStressTest", "Dev"))
        self.label_16.setText(_translate("PCIeApplicationStressTest", "Func "))
        self.label_17.setText(_translate("PCIeApplicationStressTest", "Bus"))



def comedy(self, dictval):
    print("Comedy %d", 10)
    val = 10
    while(1):
        val = val + 10
        self.progressBar.setValue(val)
        time.sleep(1)
        if val == 100:
            break
    


def progress_bar(self, dictval):
    if dictval["link_disable_test"] is True:
        val = maxval = dictval["link_disable_test_count"]
        while val != 0:
            val = dictval["link_disable_test_count"] * (100/maxval)
            self.progressBar.setValue(val)




def test(test_param):
    ptest.main_test_fun(test_param)
    t1 = threading.Thread(target=progress_bar, args=(self,value,))
    t1.start()
    t1.join()
    
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PCIeApplicationStressTest = QtWidgets.QDialog()
    ui = Ui_PCIeApplicationStressTest()
    ui.setupUi(PCIeApplicationStressTest)
    #ui.prbar(100)
    dlg = MyDialog()
    dlg.show()
    dlg.raise_()
    PCIeApplicationStressTest.show()
sys.exit(app.exec_())
"""
