# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/alphaOnly/github/mayaTool/keyFrameTools/UI/ui01.ui'
#
# Created: Thu Apr 26 09:29:35 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
from maya import OpenMaya as om
import sys
import random
import math

try:
    mel.eval("rmanLoadPlugin")
except:
    pass

try:
    import maya.mel as mel

   # mel.eval("rmanLoadPlugin")
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha")
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/Lib")
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/Lib/site-packages")
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/Lib/site-packages/ice")
    #sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/Lib/site-packages/ice")
    import ice
    
except:
    pass




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 55, 441, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_trimAfterFrame = QtWidgets.QPushButton(self.tab)
        self.pushButton_trimAfterFrame.setGeometry(QtCore.QRect(225, 30, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_trimAfterFrame.setFont(font)
        self.pushButton_trimAfterFrame.setObjectName("pushButton_trimAfterFrame")
        self.label_sf_8 = QtWidgets.QLabel(self.tab)
        self.label_sf_8.setGeometry(QtCore.QRect(15, 200, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_8.setFont(font)
        self.label_sf_8.setObjectName("label_sf_8")
        self.lineEdit_trimAfterFrame = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_trimAfterFrame.setGeometry(QtCore.QRect(340, 30, 50, 20))
        self.lineEdit_trimAfterFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_trimAfterFrame.setObjectName("lineEdit_trimAfterFrame")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(15, 270, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_sf_10 = QtWidgets.QLabel(self.tab)
        self.label_sf_10.setGeometry(QtCore.QRect(15, 290, 131, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_10.setFont(font)
        self.label_sf_10.setObjectName("label_sf_10")
        self.pushButton_alignKey = QtWidgets.QPushButton(self.tab)
        self.pushButton_alignKey.setGeometry(QtCore.QRect(30, 85, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_alignKey.setFont(font)
        self.pushButton_alignKey.setObjectName("pushButton_alignKey")
        self.radioButton_replaceV = QtWidgets.QRadioButton(self.tab)
        self.radioButton_replaceV.setGeometry(QtCore.QRect(280, 296, 111, 16))
        self.radioButton_replaceV.setObjectName("radioButton_replaceV")
        self.label_sf_9 = QtWidgets.QLabel(self.tab)
        self.label_sf_9.setGeometry(QtCore.QRect(15, 55, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_9.setFont(font)
        self.label_sf_9.setObjectName("label_sf_9")
        self.lineEdit_alignKey = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_alignKey.setGeometry(QtCore.QRect(145, 85, 50, 20))
        self.lineEdit_alignKey.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_alignKey.setObjectName("lineEdit_alignKey")
        self.radioButton_offsetV = QtWidgets.QRadioButton(self.tab)
        self.radioButton_offsetV.setGeometry(QtCore.QRect(170, 296, 91, 16))
        self.radioButton_offsetV.setChecked(True)
        self.radioButton_offsetV.setObjectName("radioButton_offsetV")
        self.label_ef_18 = QtWidgets.QLabel(self.tab)
        self.label_ef_18.setGeometry(QtCore.QRect(30, 360, 25, 16))
        self.label_ef_18.setObjectName("label_ef_18")
        self.lineEdit_minValue = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_minValue.setEnabled(True)
        self.lineEdit_minValue.setGeometry(QtCore.QRect(60, 360, 40, 16))
        self.lineEdit_minValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_minValue.setObjectName("lineEdit_minValue")
        self.label_ef_19 = QtWidgets.QLabel(self.tab)
        self.label_ef_19.setGeometry(QtCore.QRect(30, 390, 25, 16))
        self.label_ef_19.setObjectName("label_ef_19")
        self.lineEdit_maxValue = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_maxValue.setEnabled(True)
        self.lineEdit_maxValue.setGeometry(QtCore.QRect(60, 390, 40, 16))
        self.lineEdit_maxValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_maxValue.setObjectName("lineEdit_maxValue")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(15, 480, 411, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit_modifyFrame = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_modifyFrame.setGeometry(QtCore.QRect(30, 440, 111, 21))
        self.lineEdit_modifyFrame.setObjectName("lineEdit_modifyFrame")
        self.label_sf_6 = QtWidgets.QLabel(self.tab)
        self.label_sf_6.setGeometry(QtCore.QRect(30, 420, 111, 20))
        self.label_sf_6.setObjectName("label_sf_6")
        self.pushButton_makdModify = QtWidgets.QPushButton(self.tab)
        self.pushButton_makdModify.setGeometry(QtCore.QRect(30, 330, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_makdModify.setFont(font)
        self.pushButton_makdModify.setObjectName("pushButton_makdModify")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(150, 330, 271, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_translateX = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_translateX.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.checkBox_translateX.setObjectName("checkBox_translateX")
        self.checkBox_translateY = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_translateY.setGeometry(QtCore.QRect(100, 30, 91, 16))
        self.checkBox_translateY.setObjectName("checkBox_translateY")
        self.checkBox_translateZ = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_translateZ.setEnabled(False)
        self.checkBox_translateZ.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.checkBox_translateZ.setObjectName("checkBox_translateZ")
        self.checkBox_rotateY = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_rotateY.setEnabled(False)
        self.checkBox_rotateY.setGeometry(QtCore.QRect(100, 60, 91, 16))
        self.checkBox_rotateY.setObjectName("checkBox_rotateY")
        self.checkBox_rotateZ = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_rotateZ.setGeometry(QtCore.QRect(180, 60, 91, 16))
        self.checkBox_rotateZ.setObjectName("checkBox_rotateZ")
        self.checkBox_rotateX = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_rotateX.setEnabled(False)
        self.checkBox_rotateX.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.checkBox_rotateX.setObjectName("checkBox_rotateX")
        self.checkBox_scaleAll = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_scaleAll.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.checkBox_scaleAll.setObjectName("checkBox_scaleAll")
        self.checkBox_scaleX = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_scaleX.setGeometry(QtCore.QRect(100, 90, 91, 16))
        self.checkBox_scaleX.setObjectName("checkBox_scaleX")
        self.checkBox_scaleY = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_scaleY.setGeometry(QtCore.QRect(180, 90, 91, 16))
        self.checkBox_scaleY.setObjectName("checkBox_scaleY")
        self.checkBox_colorGain = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_colorGain.setEnabled(False)
        self.checkBox_colorGain.setGeometry(QtCore.QRect(100, 120, 91, 16))
        self.checkBox_colorGain.setObjectName("checkBox_colorGain")
        self.checkBox_alphaGain = QtWidgets.QRadioButton(self.groupBox_3)
        self.checkBox_alphaGain.setEnabled(False)
        self.checkBox_alphaGain.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.checkBox_alphaGain.setObjectName("checkBox_alphaGain")
        self.pushButton_trimBeforeFrame = QtWidgets.QPushButton(self.tab)
        self.pushButton_trimBeforeFrame.setGeometry(QtCore.QRect(30, 30, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_trimBeforeFrame.setFont(font)
        self.pushButton_trimBeforeFrame.setObjectName("pushButton_trimBeforeFrame")
        self.lineEdit_trimBeforeFrame = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_trimBeforeFrame.setGeometry(QtCore.QRect(145, 30, 50, 20))
        self.lineEdit_trimBeforeFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_trimBeforeFrame.setObjectName("lineEdit_trimBeforeFrame")
        self.label_sf_15 = QtWidgets.QLabel(self.tab)
        self.label_sf_15.setGeometry(QtCore.QRect(15, 5, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_15.setFont(font)
        self.label_sf_15.setObjectName("label_sf_15")
        self.pushButton_scaleFrame = QtWidgets.QPushButton(self.tab)
        self.pushButton_scaleFrame.setGeometry(QtCore.QRect(30, 140, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_scaleFrame.setFont(font)
        self.pushButton_scaleFrame.setObjectName("pushButton_scaleFrame")
        self.label_sf_16 = QtWidgets.QLabel(self.tab)
        self.label_sf_16.setGeometry(QtCore.QRect(15, 110, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_16.setFont(font)
        self.label_sf_16.setObjectName("label_sf_16")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(160, 120, 120, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_originalOut = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_originalOut.setGeometry(QtCore.QRect(70, 20, 50, 20))
        self.lineEdit_originalOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_originalOut.setObjectName("lineEdit_originalOut")
        self.lineEdit_originalIn = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_originalIn.setGeometry(QtCore.QRect(5, 20, 50, 20))
        self.lineEdit_originalIn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_originalIn.setObjectName("lineEdit_originalIn")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(290, 120, 120, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_newOut = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_newOut.setGeometry(QtCore.QRect(70, 20, 50, 20))
        self.lineEdit_newOut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_newOut.setObjectName("lineEdit_newOut")
        self.lineEdit_newIn = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_newIn.setGeometry(QtCore.QRect(5, 20, 50, 20))
        self.lineEdit_newIn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_newIn.setObjectName("lineEdit_newIn")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(150, 200, 281, 61))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_offsetFrame = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_offsetFrame.setGeometry(QtCore.QRect(165, 30, 61, 20))
        self.lineEdit_offsetFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_offsetFrame.setObjectName("lineEdit_offsetFrame")
        self.label_ef_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_ef_2.setGeometry(QtCore.QRect(89, 3, 71, 25))
        self.label_ef_2.setObjectName("label_ef_2")
        self.label_sf_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_sf_2.setGeometry(QtCore.QRect(12, 3, 71, 25))
        self.label_sf_2.setObjectName("label_sf_2")
        self.lineEdit_offfsetendFrame = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_offfsetendFrame.setGeometry(QtCore.QRect(89, 30, 61, 20))
        self.lineEdit_offfsetendFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_offfsetendFrame.setObjectName("lineEdit_offfsetendFrame")
        self.lineEdit_offfsetStartFrame = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_offfsetStartFrame.setGeometry(QtCore.QRect(12, 30, 61, 20))
        self.lineEdit_offfsetStartFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_offfsetStartFrame.setObjectName("lineEdit_offfsetStartFrame")
        self.label_rt_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_rt_2.setGeometry(QtCore.QRect(165, 3, 71, 25))
        self.label_rt_2.setObjectName("label_rt_2")
        self.checkBox_offsetRandom = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_offsetRandom.setGeometry(QtCore.QRect(218, 3, 61, 25))
        self.checkBox_offsetRandom.setObjectName("checkBox_offsetRandom")
        self.pushButton_makeOffsetFrame = QtWidgets.QPushButton(self.tab)
        self.pushButton_makeOffsetFrame.setGeometry(QtCore.QRect(30, 230, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_makeOffsetFrame.setFont(font)
        self.pushButton_makeOffsetFrame.setObjectName("pushButton_makeOffsetFrame")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(15, 170, 411, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_sf_17 = QtWidgets.QLabel(self.tab)
        self.label_sf_17.setGeometry(QtCore.QRect(15, 490, 131, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf_17.setFont(font)
        self.label_sf_17.setObjectName("label_sf_17")
        self.pushButton_addKeySin = QtWidgets.QPushButton(self.tab)
        self.pushButton_addKeySin.setEnabled(False)
        self.pushButton_addKeySin.setGeometry(QtCore.QRect(40, 520, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_addKeySin.setFont(font)
        self.pushButton_addKeySin.setObjectName("pushButton_addKeySin")
        self.pushButton_addKeyStep = QtWidgets.QPushButton(self.tab)
        self.pushButton_addKeyStep.setEnabled(False)
        self.pushButton_addKeyStep.setGeometry(QtCore.QRect(40, 550, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_addKeyStep.setFont(font)
        self.pushButton_addKeyStep.setObjectName("pushButton_addKeyStep")
        self.pushButton_addKeyStep_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_addKeyStep_2.setEnabled(False)
        self.pushButton_addKeyStep_2.setGeometry(QtCore.QRect(40, 580, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_addKeyStep_2.setFont(font)
        self.pushButton_addKeyStep_2.setObjectName("pushButton_addKeyStep_2")
        self.pushButton_addKeyStep_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_addKeyStep_3.setEnabled(False)
        self.pushButton_addKeyStep_3.setGeometry(QtCore.QRect(40, 610, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_addKeyStep_3.setFont(font)
        self.pushButton_addKeyStep_3.setObjectName("pushButton_addKeyStep_3")
        self.pushButton_addKeyStep_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_addKeyStep_4.setEnabled(False)
        self.pushButton_addKeyStep_4.setGeometry(QtCore.QRect(40, 640, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_addKeyStep_4.setFont(font)
        self.pushButton_addKeyStep_4.setObjectName("pushButton_addKeyStep_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_convertSelectToSlot = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_convertSelectToSlot.setEnabled(False)
        self.pushButton_convertSelectToSlot.setGeometry(QtCore.QRect(230, 700, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_convertSelectToSlot.setFont(font)
        self.pushButton_convertSelectToSlot.setObjectName("pushButton_convertSelectToSlot")
        self.pushButton_saveMotionToFIle = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_saveMotionToFIle.setEnabled(False)
        self.pushButton_saveMotionToFIle.setGeometry(QtCore.QRect(20, 700, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_saveMotionToFIle.setFont(font)
        self.pushButton_saveMotionToFIle.setObjectName("pushButton_saveMotionToFIle")
        self.pushButton_modifyName = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_modifyName.setEnabled(False)
        self.pushButton_modifyName.setGeometry(QtCore.QRect(20, 670, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_modifyName.setFont(font)
        self.pushButton_modifyName.setObjectName("pushButton_modifyName")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(5, 650, 420, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox_dynamic = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_dynamic.setGeometry(QtCore.QRect(30, 220, 73, 25))
        self.checkBox_dynamic.setChecked(False)
        self.checkBox_dynamic.setObjectName("checkBox_dynamic")
        self.lineEdit_numberJoints = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_numberJoints.setGeometry(QtCore.QRect(30, 50, 41, 22))
        self.lineEdit_numberJoints.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_numberJoints.setObjectName("lineEdit_numberJoints")
        self.label_ef = QtWidgets.QLabel(self.tab_2)
        self.label_ef.setGeometry(QtCore.QRect(32, 29, 71, 16))
        self.label_ef.setObjectName("label_ef")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(30, 250, 370, 391))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_createRad = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_createRad.setGeometry(QtCore.QRect(20, 60, 70, 16))
        self.radioButton_createRad.setChecked(True)
        self.radioButton_createRad.setObjectName("radioButton_createRad")
        self.radioButton_createDirection = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_createDirection.setGeometry(QtCore.QRect(20, 150, 70, 16))
        self.radioButton_createDirection.setObjectName("radioButton_createDirection")
        self.radioButton_createSquare = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_createSquare.setGeometry(QtCore.QRect(20, 90, 70, 16))
        self.radioButton_createSquare.setObjectName("radioButton_createSquare")
        self.radioButton_createSector = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_createSector.setGeometry(QtCore.QRect(20, 120, 70, 16))
        self.radioButton_createSector.setObjectName("radioButton_createSector")
        self.lineEdit_AngleA_start = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_AngleA_start.setEnabled(False)
        self.lineEdit_AngleA_start.setGeometry(QtCore.QRect(115, 120, 41, 16))
        self.lineEdit_AngleA_start.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_AngleA_start.setObjectName("lineEdit_AngleA_start")
        self.lineEdit_WidthA = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_WidthA.setEnabled(False)
        self.lineEdit_WidthA.setGeometry(QtCore.QRect(115, 90, 41, 16))
        self.lineEdit_WidthA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_WidthA.setObjectName("lineEdit_WidthA")
        self.lineEdit_HeightA = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_HeightA.setEnabled(False)
        self.lineEdit_HeightA.setGeometry(QtCore.QRect(175, 90, 41, 16))
        self.lineEdit_HeightA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_HeightA.setObjectName("lineEdit_HeightA")
        self.lineEdit_HeightB = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_HeightB.setEnabled(False)
        self.lineEdit_HeightB.setGeometry(QtCore.QRect(175, 150, 40, 16))
        self.lineEdit_HeightB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_HeightB.setObjectName("lineEdit_HeightB")
        self.lineEdit_WidthB = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_WidthB.setEnabled(False)
        self.lineEdit_WidthB.setGeometry(QtCore.QRect(115, 150, 40, 16))
        self.lineEdit_WidthB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_WidthB.setObjectName("lineEdit_WidthB")
        self.lineEdit_RadiusA = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_RadiusA.setEnabled(False)
        self.lineEdit_RadiusA.setGeometry(QtCore.QRect(115, 60, 41, 16))
        self.lineEdit_RadiusA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_RadiusA.setObjectName("lineEdit_RadiusA")
        self.lineEdit_shapeEndFrame = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_shapeEndFrame.setGeometry(QtCore.QRect(200, 25, 40, 16))
        self.lineEdit_shapeEndFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_shapeEndFrame.setObjectName("lineEdit_shapeEndFrame")
        self.lineEdit_shapeStartFrame = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_shapeStartFrame.setGeometry(QtCore.QRect(80, 25, 40, 16))
        self.lineEdit_shapeStartFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_shapeStartFrame.setObjectName("lineEdit_shapeStartFrame")
        self.label_sf_13 = QtWidgets.QLabel(self.groupBox)
        self.label_sf_13.setGeometry(QtCore.QRect(20, 20, 61, 25))
        self.label_sf_13.setObjectName("label_sf_13")
        self.checkBox_offsetRandom_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_offsetRandom_2.setGeometry(QtCore.QRect(270, 25, 73, 16))
        self.checkBox_offsetRandom_2.setChecked(True)
        self.checkBox_offsetRandom_2.setObjectName("checkBox_offsetRandom_2")
        self.label_ef_4 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_4.setGeometry(QtCore.QRect(140, 20, 71, 25))
        self.label_ef_4.setObjectName("label_ef_4")
        self.lineEdit_AngleA_end = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_AngleA_end.setEnabled(False)
        self.lineEdit_AngleA_end.setGeometry(QtCore.QRect(175, 120, 41, 16))
        self.lineEdit_AngleA_end.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_AngleA_end.setObjectName("lineEdit_AngleA_end")
        self.label_ef_6 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_6.setGeometry(QtCore.QRect(96, 150, 25, 16))
        self.label_ef_6.setObjectName("label_ef_6")
        self.label_ef_7 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_7.setGeometry(QtCore.QRect(161, 150, 21, 16))
        self.label_ef_7.setObjectName("label_ef_7")
        self.label_ef_8 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_8.setGeometry(QtCore.QRect(161, 90, 21, 16))
        self.label_ef_8.setObjectName("label_ef_8")
        self.label_ef_9 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_9.setGeometry(QtCore.QRect(96, 90, 25, 16))
        self.label_ef_9.setObjectName("label_ef_9")
        self.label_ef_10 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_10.setGeometry(QtCore.QRect(96, 120, 25, 16))
        self.label_ef_10.setObjectName("label_ef_10")
        self.label_ef_11 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_11.setGeometry(QtCore.QRect(96, 60, 25, 16))
        self.label_ef_11.setObjectName("label_ef_11")
        self.lineEdit_directionDegree = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_directionDegree.setEnabled(False)
        self.lineEdit_directionDegree.setGeometry(QtCore.QRect(236, 150, 41, 16))
        self.lineEdit_directionDegree.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_directionDegree.setObjectName("lineEdit_directionDegree")
        self.label_ef_12 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_12.setGeometry(QtCore.QRect(222, 150, 16, 16))
        self.label_ef_12.setObjectName("label_ef_12")
        self.lineEdit_directionSpread = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_directionSpread.setEnabled(False)
        self.lineEdit_directionSpread.setGeometry(QtCore.QRect(295, 150, 41, 16))
        self.lineEdit_directionSpread.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_directionSpread.setObjectName("lineEdit_directionSpread")
        self.label_ef_13 = QtWidgets.QLabel(self.groupBox)
        self.label_ef_13.setGeometry(QtCore.QRect(283, 150, 16, 16))
        self.label_ef_13.setObjectName("label_ef_13")
        self.radioButton_createFromImageWeight = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_createFromImageWeight.setGeometry(QtCore.QRect(20, 310, 91, 16))
        self.radioButton_createFromImageWeight.setObjectName("radioButton_createFromImageWeight")
        self.lineEdit_selectMotionFIle = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_selectMotionFIle.setEnabled(False)
        self.lineEdit_selectMotionFIle.setGeometry(QtCore.QRect(115, 310, 222, 16))
        self.lineEdit_selectMotionFIle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_selectMotionFIle.setObjectName("lineEdit_selectMotionFIle")
        self.toolButton_selectMotionFile = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_selectMotionFile.setGeometry(QtCore.QRect(340, 310, 22, 18))
        self.toolButton_selectMotionFile.setObjectName("toolButton_selectMotionFile")
        self.radioButton_createFollowCurve = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_createFollowCurve.setGeometry(QtCore.QRect(20, 180, 91, 16))
        self.radioButton_createFollowCurve.setObjectName("radioButton_createFollowCurve")
        self.lineEdit_selectCurve = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_selectCurve.setEnabled(False)
        self.lineEdit_selectCurve.setGeometry(QtCore.QRect(115, 180, 222, 16))
        self.lineEdit_selectCurve.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_selectCurve.setObjectName("lineEdit_selectCurve")
        self.toolButton_selectCurve = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_selectCurve.setEnabled(False)
        self.toolButton_selectCurve.setGeometry(QtCore.QRect(340, 180, 22, 18))
        self.toolButton_selectCurve.setObjectName("toolButton_selectCurve")
        self.groupBox_keysOption = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_keysOption.setGeometry(QtCore.QRect(30, 200, 331, 91))
        self.groupBox_keysOption.setTitle("")
        self.groupBox_keysOption.setObjectName("groupBox_keysOption")
        self.horizontalSlider_powA = QtWidgets.QSlider(self.groupBox_keysOption)
        self.horizontalSlider_powA.setGeometry(QtCore.QRect(110, 60, 211, 16))
        self.horizontalSlider_powA.setMinimum(1)
        self.horizontalSlider_powA.setMaximum(100)
        self.horizontalSlider_powA.setProperty("value", 10)
        self.horizontalSlider_powA.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_powA.setObjectName("horizontalSlider_powA")
        self.label_ef_14 = QtWidgets.QLabel(self.groupBox_keysOption)
        self.label_ef_14.setGeometry(QtCore.QRect(20, 10, 25, 16))
        self.label_ef_14.setObjectName("label_ef_14")
        self.label_ef_15 = QtWidgets.QLabel(self.groupBox_keysOption)
        self.label_ef_15.setGeometry(QtCore.QRect(20, 35, 41, 16))
        self.label_ef_15.setObjectName("label_ef_15")
        self.horizontalSlider_NoiseA = QtWidgets.QSlider(self.groupBox_keysOption)
        self.horizontalSlider_NoiseA.setGeometry(QtCore.QRect(110, 35, 211, 16))
        self.horizontalSlider_NoiseA.setMinimum(0)
        self.horizontalSlider_NoiseA.setMaximum(500)
        self.horizontalSlider_NoiseA.setProperty("value", 0)
        self.horizontalSlider_NoiseA.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_NoiseA.setObjectName("horizontalSlider_NoiseA")
        self.lineEdit_pow = QtWidgets.QLineEdit(self.groupBox_keysOption)
        self.lineEdit_pow.setEnabled(False)
        self.lineEdit_pow.setGeometry(QtCore.QRect(60, 60, 40, 16))
        self.lineEdit_pow.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_pow.setObjectName("lineEdit_pow")
        self.label_ef_16 = QtWidgets.QLabel(self.groupBox_keysOption)
        self.label_ef_16.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_ef_16.setObjectName("label_ef_16")
        self.lineEdit_keysA = QtWidgets.QLineEdit(self.groupBox_keysOption)
        self.lineEdit_keysA.setEnabled(False)
        self.lineEdit_keysA.setGeometry(QtCore.QRect(60, 10, 40, 16))
        self.lineEdit_keysA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_keysA.setObjectName("lineEdit_keysA")
        self.horizontalSlider_keysA = QtWidgets.QSlider(self.groupBox_keysOption)
        self.horizontalSlider_keysA.setGeometry(QtCore.QRect(110, 10, 211, 16))
        self.horizontalSlider_keysA.setMinimum(2)
        self.horizontalSlider_keysA.setMaximum(50)
        self.horizontalSlider_keysA.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_keysA.setObjectName("horizontalSlider_keysA")
        self.lineEdit_NoiseA = QtWidgets.QLineEdit(self.groupBox_keysOption)
        self.lineEdit_NoiseA.setEnabled(False)
        self.lineEdit_NoiseA.setGeometry(QtCore.QRect(60, 35, 40, 16))
        self.lineEdit_NoiseA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_NoiseA.setObjectName("lineEdit_NoiseA")
        self.checkBox_squareFillIn = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_squareFillIn.setGeometry(QtCore.QRect(238, 90, 73, 16))
        self.checkBox_squareFillIn.setChecked(False)
        self.checkBox_squareFillIn.setObjectName("checkBox_squareFillIn")
        self.label_sf = QtWidgets.QLabel(self.tab_2)
        self.label_sf.setGeometry(QtCore.QRect(10, 2, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_sf.setFont(font)
        self.label_sf.setObjectName("label_sf")
        self.pushButton_modifyName_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_modifyName_2.setEnabled(False)
        self.pushButton_modifyName_2.setGeometry(QtCore.QRect(230, 670, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_modifyName_2.setFont(font)
        self.pushButton_modifyName_2.setObjectName("pushButton_modifyName_2")
        self.horizontalSlider_numberJoints = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_numberJoints.setGeometry(QtCore.QRect(80, 50, 231, 25))
        self.horizontalSlider_numberJoints.setMinimum(1)
        self.horizontalSlider_numberJoints.setMaximum(300)
        self.horizontalSlider_numberJoints.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_numberJoints.setObjectName("horizontalSlider_numberJoints")
        self.pushButton_createJoint = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_createJoint.setGeometry(QtCore.QRect(328, 50, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_createJoint.setFont(font)
        self.pushButton_createJoint.setObjectName("pushButton_createJoint")
        self.toolButton_dynReset = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_dynReset.setEnabled(True)
        self.toolButton_dynReset.setGeometry(QtCore.QRect(360, 240, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.toolButton_dynReset.setFont(font)
        self.toolButton_dynReset.setObjectName("toolButton_dynReset")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 80, 370, 131))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_jointName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_jointName.setGeometry(QtCore.QRect(100, 0, 111, 22))
        self.lineEdit_jointName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_jointName.setObjectName("lineEdit_jointName")
        self.label_ef_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_ef_3.setGeometry(QtCore.QRect(18, 0, 61, 22))
        self.label_ef_3.setObjectName("label_ef_3")
        self.label_sf_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_sf_14.setGeometry(QtCore.QRect(170, 30, 41, 25))
        self.label_sf_14.setObjectName("label_sf_14")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(161, 59, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_ef_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_ef_5.setGeometry(QtCore.QRect(246, 30, 41, 25))
        self.label_ef_5.setObjectName("label_ef_5")
        self.lineEdit_imageWidth = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_imageWidth.setGeometry(QtCore.QRect(201, 29, 40, 22))
        self.lineEdit_imageWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_imageWidth.setObjectName("lineEdit_imageWidth")
        self.lineEdit_imageHeight = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_imageHeight.setGeometry(QtCore.QRect(281, 29, 40, 22))
        self.lineEdit_imageHeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_imageHeight.setObjectName("lineEdit_imageHeight")
        self.checkBox_witImagePlanes = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_witImagePlanes.setGeometry(QtCore.QRect(21, 29, 111, 25))
        self.checkBox_witImagePlanes.setChecked(True)
        self.checkBox_witImagePlanes.setObjectName("checkBox_witImagePlanes")
        self.checkBox_getShader = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_getShader.setGeometry(QtCore.QRect(20, 60, 111, 25))
        self.checkBox_getShader.setChecked(False)
        self.checkBox_getShader.setObjectName("checkBox_getShader")
        self.label_ef_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_ef_17.setGeometry(QtCore.QRect(60, 90, 81, 22))
        self.label_ef_17.setObjectName("label_ef_17")
        self.lineEdit_imageFile = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_imageFile.setEnabled(False)
        self.lineEdit_imageFile.setGeometry(QtCore.QRect(162, 90, 161, 22))
        self.lineEdit_imageFile.setText("")
        self.lineEdit_imageFile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_imageFile.setObjectName("lineEdit_imageFile")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.plainTextEdit_exportPath = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_exportPath.setEnabled(False)
        self.plainTextEdit_exportPath.setGeometry(QtCore.QRect(104, 10, 291, 41))
        self.plainTextEdit_exportPath.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit_exportPath.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit_exportPath.setBackgroundVisible(False)
        self.plainTextEdit_exportPath.setCenterOnScroll(False)
        self.plainTextEdit_exportPath.setObjectName("plainTextEdit_exportPath")
        self.label_sf_12 = QtWidgets.QLabel(self.tab_3)
        self.label_sf_12.setGeometry(QtCore.QRect(14, 10, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_sf_12.setFont(font)
        self.label_sf_12.setObjectName("label_sf_12")
        self.toolButton_selectExportPath = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_selectExportPath.setGeometry(QtCore.QRect(400, 10, 22, 20))
        self.toolButton_selectExportPath.setObjectName("toolButton_selectExportPath")
        self.label_ef_20 = QtWidgets.QLabel(self.tab_3)
        self.label_ef_20.setGeometry(QtCore.QRect(60, 110, 41, 20))
        self.label_ef_20.setObjectName("label_ef_20")
        self.lineEdit_exportSpeedValue = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_exportSpeedValue.setEnabled(True)
        self.lineEdit_exportSpeedValue.setGeometry(QtCore.QRect(110, 110, 40, 20))
        self.lineEdit_exportSpeedValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_exportSpeedValue.setObjectName("lineEdit_exportSpeedValue")
        self.horizontalSlider_speedValue = QtWidgets.QSlider(self.tab_3)
        self.horizontalSlider_speedValue.setGeometry(QtCore.QRect(160, 110, 211, 20))
        self.horizontalSlider_speedValue.setMinimum(1)
        self.horizontalSlider_speedValue.setMaximum(100)
        self.horizontalSlider_speedValue.setProperty("value", 10)
        self.horizontalSlider_speedValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_speedValue.setObjectName("horizontalSlider_speedValue")
        self.lineEdit_exportStrtFrame = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_exportStrtFrame.setEnabled(True)
        self.lineEdit_exportStrtFrame.setGeometry(QtCore.QRect(110, 80, 40, 20))
        self.lineEdit_exportStrtFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_exportStrtFrame.setObjectName("lineEdit_exportStrtFrame")
        self.label_ef_21 = QtWidgets.QLabel(self.tab_3)
        self.label_ef_21.setGeometry(QtCore.QRect(40, 80, 61, 20))
        self.label_ef_21.setObjectName("label_ef_21")
        self.label_ef_22 = QtWidgets.QLabel(self.tab_3)
        self.label_ef_22.setGeometry(QtCore.QRect(170, 80, 61, 20))
        self.label_ef_22.setObjectName("label_ef_22")
        self.lineEdit_exportEndFrame = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_exportEndFrame.setEnabled(True)
        self.lineEdit_exportEndFrame.setGeometry(QtCore.QRect(240, 80, 40, 20))
        self.lineEdit_exportEndFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_exportEndFrame.setObjectName("lineEdit_exportEndFrame")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_sf_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_sf_11.setGeometry(QtCore.QRect(30, 10, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_sf_11.setFont(font)
        self.label_sf_11.setObjectName("label_sf_11")
        self.toolButton_selectProj = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_selectProj.setGeometry(QtCore.QRect(416, 10, 22, 20))
        self.toolButton_selectProj.setObjectName("toolButton_selectProj")
        self.tableWidget_imagesA = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_imagesA.setGeometry(QtCore.QRect(460, 60, 381, 361))
        self.tableWidget_imagesA.setObjectName("tableWidget_imagesA")
        self.tableWidget_imagesA.setColumnCount(0)
        self.tableWidget_imagesA.setRowCount(0)
        self.plainTextEdit_metaData = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_metaData.setGeometry(QtCore.QRect(460, 430, 381, 151))
        self.plainTextEdit_metaData.setObjectName("plainTextEdit_metaData")
        self.pushButton_debugA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_debugA.setGeometry(QtCore.QRect(470, 620, 75, 23))
        self.pushButton_debugA.setObjectName("pushButton_debugA")
        self.pushButton_debugB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_debugB.setGeometry(QtCore.QRect(570, 620, 75, 23))
        self.pushButton_debugB.setObjectName("pushButton_debugB")
        self.pushButton_debugC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_debugC.setGeometry(QtCore.QRect(680, 620, 75, 23))
        self.pushButton_debugC.setObjectName("pushButton_debugC")
        self.plainTextEdit_proj = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_proj.setEnabled(False)
        self.plainTextEdit_proj.setGeometry(QtCore.QRect(120, 10, 290, 40))
        self.plainTextEdit_proj.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit_proj.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit_proj.setBackgroundVisible(False)
        self.plainTextEdit_proj.setCenterOnScroll(False)
        self.plainTextEdit_proj.setObjectName("plainTextEdit_proj")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "keyFrameTool", None, -1))
        self.pushButton_trimAfterFrame.setText(QtWidgets.QApplication.translate("MainWindow", "Trim After Frame", None, -1))
        self.label_sf_8.setText(QtWidgets.QApplication.translate("MainWindow", "Offset All Keys", None, -1))
        self.label_sf_10.setText(QtWidgets.QApplication.translate("MainWindow", "Random All Keys", None, -1))
        self.pushButton_alignKey.setText(QtWidgets.QApplication.translate("MainWindow", "Align To Frame", None, -1))
        self.radioButton_replaceV.setText(QtWidgets.QApplication.translate("MainWindow", "replace Value", None, -1))
        self.label_sf_9.setText(QtWidgets.QApplication.translate("MainWindow", "Align All Keys", None, -1))
        self.radioButton_offsetV.setText(QtWidgets.QApplication.translate("MainWindow", "offset Value", None, -1))
        self.label_ef_18.setText(QtWidgets.QApplication.translate("MainWindow", "Min", None, -1))
        self.lineEdit_minValue.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_ef_19.setText(QtWidgets.QApplication.translate("MainWindow", "Max", None, -1))
        self.lineEdit_maxValue.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.lineEdit_modifyFrame.setText(QtWidgets.QApplication.translate("MainWindow", "all", None, -1))
        self.label_sf_6.setText(QtWidgets.QApplication.translate("MainWindow", "Frames index [0,1,...]", None, -1))
        self.pushButton_makdModify.setText(QtWidgets.QApplication.translate("MainWindow", "modify Keys", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "channel select", None, -1))
        self.checkBox_translateX.setText(QtWidgets.QApplication.translate("MainWindow", "translateX", None, -1))
        self.checkBox_translateY.setText(QtWidgets.QApplication.translate("MainWindow", "translateY", None, -1))
        self.checkBox_translateZ.setText(QtWidgets.QApplication.translate("MainWindow", "translateZ", None, -1))
        self.checkBox_rotateY.setText(QtWidgets.QApplication.translate("MainWindow", "rotateY", None, -1))
        self.checkBox_rotateZ.setText(QtWidgets.QApplication.translate("MainWindow", "rotateZ", None, -1))
        self.checkBox_rotateX.setText(QtWidgets.QApplication.translate("MainWindow", "rotateX", None, -1))
        self.checkBox_scaleAll.setText(QtWidgets.QApplication.translate("MainWindow", "scale", None, -1))
        self.checkBox_scaleX.setText(QtWidgets.QApplication.translate("MainWindow", "scaleX", None, -1))
        self.checkBox_scaleY.setText(QtWidgets.QApplication.translate("MainWindow", "scaleY", None, -1))
        self.checkBox_colorGain.setText(QtWidgets.QApplication.translate("MainWindow", "color Gain", None, -1))
        self.checkBox_alphaGain.setText(QtWidgets.QApplication.translate("MainWindow", "alpha Gain", None, -1))
        self.pushButton_trimBeforeFrame.setText(QtWidgets.QApplication.translate("MainWindow", "Trim Before Frame", None, -1))
        self.label_sf_15.setText(QtWidgets.QApplication.translate("MainWindow", "Trim Frame", None, -1))
        self.pushButton_scaleFrame.setText(QtWidgets.QApplication.translate("MainWindow", "Scale Frame Range", None, -1))
        self.label_sf_16.setText(QtWidgets.QApplication.translate("MainWindow", "Scale Frame", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Original In/Out", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "New In/Out", None, -1))
        self.label_ef_2.setText(QtWidgets.QApplication.translate("MainWindow", "end frame", None, -1))
        self.label_sf_2.setText(QtWidgets.QApplication.translate("MainWindow", "start frame", None, -1))
        self.label_rt_2.setText(QtWidgets.QApplication.translate("MainWindow", "offset ", None, -1))
        self.checkBox_offsetRandom.setText(QtWidgets.QApplication.translate("MainWindow", "random", None, -1))
        self.pushButton_makeOffsetFrame.setText(QtWidgets.QApplication.translate("MainWindow", "offset Keys", None, -1))
        self.label_sf_17.setText(QtWidgets.QApplication.translate("MainWindow", "Graphic Keys", None, -1))
        self.pushButton_addKeySin.setText(QtWidgets.QApplication.translate("MainWindow", "add Sin", None, -1))
        self.pushButton_addKeyStep.setText(QtWidgets.QApplication.translate("MainWindow", "add Step", None, -1))
        self.pushButton_addKeyStep_2.setText(QtWidgets.QApplication.translate("MainWindow", "add Graphic A", None, -1))
        self.pushButton_addKeyStep_3.setText(QtWidgets.QApplication.translate("MainWindow", "add Graphic B", None, -1))
        self.pushButton_addKeyStep_4.setText(QtWidgets.QApplication.translate("MainWindow", "add Graphic C", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "adjust Keys", None, -1))
        self.pushButton_convertSelectToSlot.setText(QtWidgets.QApplication.translate("MainWindow", "convert Select To Slot", None, -1))
        self.pushButton_saveMotionToFIle.setText(QtWidgets.QApplication.translate("MainWindow", "save motion to file", None, -1))
        self.pushButton_modifyName.setText(QtWidgets.QApplication.translate("MainWindow", "modify Joints and slot  Names", None, -1))
        self.checkBox_dynamic.setText(QtWidgets.QApplication.translate("MainWindow", "dynamic", None, -1))
        self.lineEdit_numberJoints.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_ef.setText(QtWidgets.QApplication.translate("MainWindow", "amount", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "style select", None, -1))
        self.radioButton_createRad.setText(QtWidgets.QApplication.translate("MainWindow", "Radiation", None, -1))
        self.radioButton_createDirection.setText(QtWidgets.QApplication.translate("MainWindow", "Direction", None, -1))
        self.radioButton_createSquare.setText(QtWidgets.QApplication.translate("MainWindow", "Square", None, -1))
        self.radioButton_createSector.setText(QtWidgets.QApplication.translate("MainWindow", "Sector", None, -1))
        self.lineEdit_AngleA_start.setText(QtWidgets.QApplication.translate("MainWindow", "-90", None, -1))
        self.lineEdit_WidthA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_HeightA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_HeightB.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_WidthB.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_RadiusA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_shapeEndFrame.setText(QtWidgets.QApplication.translate("MainWindow", "60", None, -1))
        self.lineEdit_shapeStartFrame.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_sf_13.setText(QtWidgets.QApplication.translate("MainWindow", "start frame", None, -1))
        self.checkBox_offsetRandom_2.setText(QtWidgets.QApplication.translate("MainWindow", "random", None, -1))
        self.label_ef_4.setText(QtWidgets.QApplication.translate("MainWindow", "end frame", None, -1))
        self.lineEdit_AngleA_end.setText(QtWidgets.QApplication.translate("MainWindow", "90", None, -1))
        self.label_ef_6.setText(QtWidgets.QApplication.translate("MainWindow", "X:", None, -1))
        self.label_ef_7.setText(QtWidgets.QApplication.translate("MainWindow", "Y:", None, -1))
        self.label_ef_8.setText(QtWidgets.QApplication.translate("MainWindow", "H:", None, -1))
        self.label_ef_9.setText(QtWidgets.QApplication.translate("MainWindow", "W:", None, -1))
        self.label_ef_10.setText(QtWidgets.QApplication.translate("MainWindow", "D:", None, -1))
        self.label_ef_11.setText(QtWidgets.QApplication.translate("MainWindow", "R:", None, -1))
        self.lineEdit_directionDegree.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_ef_12.setText(QtWidgets.QApplication.translate("MainWindow", "D:", None, -1))
        self.lineEdit_directionSpread.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_ef_13.setText(QtWidgets.QApplication.translate("MainWindow", "S:", None, -1))
        self.radioButton_createFromImageWeight.setText(QtWidgets.QApplication.translate("MainWindow", "Image Weight", None, -1))
        self.lineEdit_selectMotionFIle.setText(QtWidgets.QApplication.translate("MainWindow", "select file", None, -1))
        self.toolButton_selectMotionFile.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.radioButton_createFollowCurve.setText(QtWidgets.QApplication.translate("MainWindow", "Follow Curve", None, -1))
        self.lineEdit_selectCurve.setText(QtWidgets.QApplication.translate("MainWindow", "select curve", None, -1))
        self.toolButton_selectCurve.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label_ef_14.setText(QtWidgets.QApplication.translate("MainWindow", "Keys", None, -1))
        self.label_ef_15.setText(QtWidgets.QApplication.translate("MainWindow", "Noise:", None, -1))
        self.lineEdit_pow.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_ef_16.setText(QtWidgets.QApplication.translate("MainWindow", "Pow:", None, -1))
        self.lineEdit_keysA.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.lineEdit_NoiseA.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.checkBox_squareFillIn.setText(QtWidgets.QApplication.translate("MainWindow", "Fill in", None, -1))
        self.label_sf.setText(QtWidgets.QApplication.translate("MainWindow", "create Joints", None, -1))
        self.pushButton_modifyName_2.setText(QtWidgets.QApplication.translate("MainWindow", "fit to images", None, -1))
        self.pushButton_createJoint.setText(QtWidgets.QApplication.translate("MainWindow", "create Joint", None, -1))
        self.toolButton_dynReset.setText(QtWidgets.QApplication.translate("MainWindow", "RESET", None, -1))
        self.lineEdit_jointName.setText(QtWidgets.QApplication.translate("MainWindow", "bone_", None, -1))
        self.label_ef_3.setText(QtWidgets.QApplication.translate("MainWindow", "name proxy:", None, -1))
        self.label_sf_14.setText(QtWidgets.QApplication.translate("MainWindow", "width", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "-- select shader", None, -1))
        self.label_ef_5.setText(QtWidgets.QApplication.translate("MainWindow", "height", None, -1))
        self.lineEdit_imageWidth.setText(QtWidgets.QApplication.translate("MainWindow", "50", None, -1))
        self.lineEdit_imageHeight.setText(QtWidgets.QApplication.translate("MainWindow", "50", None, -1))
        self.checkBox_witImagePlanes.setText(QtWidgets.QApplication.translate("MainWindow", "with image plane", None, -1))
        self.checkBox_getShader.setText(QtWidgets.QApplication.translate("MainWindow", "with image plane", None, -1))
        self.label_ef_17.setText(QtWidgets.QApplication.translate("MainWindow", "Image Name:", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "create Joints", None, -1))
        self.plainTextEdit_exportPath.setPlainText(QtWidgets.QApplication.translate("MainWindow", "export path", None, -1))
        self.label_sf_12.setText(QtWidgets.QApplication.translate("MainWindow", "export Project:", None, -1))
        self.toolButton_selectExportPath.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label_ef_20.setText(QtWidgets.QApplication.translate("MainWindow", "Speed", None, -1))
        self.lineEdit_exportSpeedValue.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.lineEdit_exportStrtFrame.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.label_ef_21.setText(QtWidgets.QApplication.translate("MainWindow", "Start Frame", None, -1))
        self.label_ef_22.setText(QtWidgets.QApplication.translate("MainWindow", "End Frame", None, -1))
        self.lineEdit_exportEndFrame.setText(QtWidgets.QApplication.translate("MainWindow", "60", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "export", None, -1))
        self.label_sf_11.setText(QtWidgets.QApplication.translate("MainWindow", "Current Project:", None, -1))
        self.toolButton_selectProj.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.pushButton_debugA.setText(QtWidgets.QApplication.translate("MainWindow", "debugA", None, -1))
        self.pushButton_debugB.setText(QtWidgets.QApplication.translate("MainWindow", "debugB", None, -1))
        self.pushButton_debugC.setText(QtWidgets.QApplication.translate("MainWindow", "debugC", None, -1))
        self.plainTextEdit_proj.setPlainText(QtWidgets.QApplication.translate("MainWindow", "current Project", None, -1))

        
        ##initial Setting
        self.checkBox_squareFillIn.setEnabled(False)


class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):pushButton_modifyName checkBox_scaleAll
     #   self.setAttrStateList()
       # self.pushButton_mc.clicked.connect(self.getItems)
        self.plainTextEdit_proj.setPlainText( cmds.workspace(q=True, directory=True) )
        self.pushButton_makeOffsetFrame.clicked.connect(self.offsetKeyFrames)
        self.pushButton_trimAfterFrame.clicked.connect(self.trimAfterFrame)
        self.pushButton_trimBeforeFrame.clicked.connect(self.trimBeforeFrame)

        self.pushButton_scaleFrame.clicked.connect(self.scaleFrames)


        self.pushButton_alignKey.clicked.connect(self.alignKeys)
        self.pushButton_makdModify.clicked.connect(self.modifyKeyValue)
       # self.pushButton_modifyName.clicked.connect(self.createJoints) horizontalSlider_numberJoints_2 lineEdit_numberJoints_2
        self.horizontalSlider_numberJoints.valueChanged.connect(self.modifyJointInputSlider)
        self.horizontalSlider_keysA.valueChanged.connect(self.modifyJointInputSlider)
        self.horizontalSlider_NoiseA.valueChanged.connect(self.modifyJointInputSlider)
        self.horizontalSlider_powA.valueChanged.connect(self.modifyJointInputSlider)


        self.lineEdit_numberJoints.textChanged.connect(self.modifyJointInputText)
       # self.lineEdit_numberJoints_2.textChanged.connect(self.modifyJointInputText) pushButton_createJoint_2 checkBox_modify_all checkBox_dynamic

        self.pushButton_createJoint.clicked.connect(self.createJoints)
        
        #self.checkBox_modify_all.stateChanged.connect(self.modifyAllAttrStateDict)
       # self.checkBox_modify_unlockAll.stateChanged.connect(self.modifyAllAttrStateDict)    checkBox_scaleAll   
        
        self.checkBox_translateX.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_translateY.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_translateZ.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_rotateX.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_rotateY.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_rotateZ.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_scaleAll.clicked.connect(self.modifyAttrStateDict)

        self.checkBox_scaleX.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_scaleY.clicked.connect(self.modifyAttrStateDict)
       # self.checkBox_scaleZ.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_alphaGain.clicked.connect(self.modifyAttrStateDict)
        self.checkBox_colorGain.clicked.connect(self.modifyAttrStateDict)

        self.radioButton_createRad.clicked.connect(self.changeShapeState)
        self.radioButton_createSquare.clicked.connect(self.changeShapeState)
        self.radioButton_createSquare.clicked.connect(self.changeShapeState)
        self.radioButton_createSector.clicked.connect(self.changeShapeState)
        self.radioButton_createDirection.clicked.connect(self.changeShapeState)
        self.radioButton_createFollowCurve.clicked.connect(self.changeShapeState)
        
        self.radioButton_createFromImageWeight.clicked.connect(self.changeShapeState)
        
        self.toolButton_selectCurve.clicked.connect(self.getCurve)

        ## get image file checkBox_getShader
       # self.pushButton_getImageFile.clicked.connect(self.getImageFile)
       # self.checkBox_getShader.stateChanged.connect(self.getShaderInfo)
        self.checkBox_getShader.stateChanged.connect(self.enableComboBox)

        self.comboBox.currentIndexChanged.connect(self.getImageFile)
        
        self.toolButton_selectProj.clicked.connect(self.setProj)
        
        
        self.lineEdit_keysA.textChanged.connect(self.changeSlideBar)
        self.lineEdit_NoiseA.textChanged.connect(self.changeSlideBar)
        self.lineEdit_pow.textChanged.connect(self.changeSlideBar) 
        
        #self.toolButton_dynReset.clicked.connect(self.getCurves)
        self.checkBox_dynamic.stateChanged.connect(self.modifyDynamicState)
        #reset button
        self.toolButton_dynReset.clicked.connect(self.resetDynamicValue)

    
        self.attrCheckStateDict = {"translateX":0,
                                   "translateY":0,
                                   "translateZ":0,
                                   "rotateX":0,
                                   "rotateY":0,
                                   "rotateZ":0,
                                   "scaleX":0,
                                   "scaleY":0,
                                   "scaleZ":0,
                                   "alphaGain":0,
                                   "colorGain":0
                                   }
   

        
    def resetDynamicValue(self):
        
        self.lineEdit_shapeStartFrame.setText("1")
        self.lineEdit_shapeEndFrame.setText("60")
        self.checkBox_offsetRandom_2.setChecked(True)
        self.lineEdit_RadiusA.setText("500")
        self.lineEdit_WidthA.setText("500")
        self.lineEdit_HeightA.setText("500")
        self.lineEdit_AngleA_start.setText("-90")
        self.lineEdit_AngleA_end.setText("90")
        self.lineEdit_WidthB.setText("500")
        self.lineEdit_HeightB.setText("500")
        self.lineEdit_directionDegree.setText("0")
        self.lineEdit_directionSpread.setText("0")
        self.lineEdit_keysA.setText("2")
        self.lineEdit_NoiseA.setText("0")
        self.lineEdit_pow.setText("1")


        
        
    def setProj(self):
        proj = cmds.fileDialog2(fm=3)[0]
        print proj
        self.plainTextEdit_proj.setPlainText(proj)
        cmds.workspace(dir=proj)
        #print cmds.workspace(q=True,dir=True)
        
        
    def test(self):
        print "asdasdsad"
    
    def enableComboBox(self):
        #self.comboBox.clear()
        if self.checkBox_getShader.isChecked() == True:
            self.comboBox.setEnabled(True)
            self.getShaderInfo()
        else:
            self.comboBox.setEnabled(False)
        
        
        
    def getShaderInfo(self):
    
        print"get shader"
        self.comboBox.clear()
        shaderType = ["lambert","blinn","phong","surfaceShader","phongE","StingrayPBS"]
        shaderComboBoxList = []
        for i in cmds.ls():
            if cmds.nodeType(i) in shaderType:
                shaderComboBoxList.append(i)
     #   print shaderComboBoxList
        for shaderNode in shaderComboBoxList:
            self.comboBox.addItem(shaderNode)
    
    def getImageFile(self):
        #self.getShaderInfo() getImageFile
        try:
            getShaderSelected = self.comboBox.currentText()
            imageFile = cmds.listConnections("%s.color"%getShaderSelected,t="file")[0]

            currentFile = cmds.getAttr("%s.fileTextureName" %imageFile)

            imageFileName = currentFile.split("/")[-1]
            self.lineEdit_imageFile.setText(imageFileName)

            
            image = ice.Load(currentFile)
            metaData = image.GetMetaData()
            imageWidth= metaData['Original Size'].split(' ')[0].split('(')[-1]
            imageHeight= metaData['Original Size'].split(' ')[1].split(')')[0]
            self.lineEdit_imageWidth.setText(imageWidth)
            self.lineEdit_imageHeight.setText(imageHeight)
            proxyName = imageFileName.split('.')[0]+"_"
            self.lineEdit_jointName.setText(proxyName)
        except:
            pass

        
    def changeSlideBar(self):
        keyNum= int(self.lineEdit_keysA.text())
        self.horizontalSlider_keysA.setValue(keyNum)

        noise = int(float(self.lineEdit_NoiseA.text())*1.0)

        self.horizontalSlider_NoiseA.setValue(noise)
        logNum = int(float(self.lineEdit_pow.text())*10.0)

        self.horizontalSlider_powA.setValue(logNum)

        
        
    def getCurve(self):
        
        allObj = cmds.ls(sl=True,dag=2)
        self.allSelectCurveList = []
        for i in allObj:
            if cmds.nodeType(i) == "nurbsCurve":
                self.allSelectCurveList.append(i)
              
        if len(self.allSelectCurveList) == 0:
            self.statusbar.showMessage("select at least one curve")
            self.statusbar.setStyleSheet("\
                                                QStatusBar {\
                                                    color: rgb(255,0,0);\
                                                    border-color: rgb(60,80,80); \
                                                    font-size: 14px;\
                                                }\
                                                ")  
            
      #  print len(allSelectCurveList),allSelectCurveList
        #return allSelectCurveList
        
        self.lineEdit_selectCurve.setText("%s"%self.allSelectCurveList)
        self.allSelectCurveList
        
    def changeShapeState(self):  
        print "dsfdsfdfdsfdsf"
        
        
        if self.radioButton_createRad.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(True)
            self.lineEdit_WidthA.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)

            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)

            self.lineEdit_WidthB.setEnabled(False)
            self.lineEdit_HeightB.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.lineEdit_selectMotionFIle.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)




        
        if self.radioButton_createSquare.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_WidthA.setEnabled(True)
            self.lineEdit_HeightA.setEnabled(True)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(True)

            self.lineEdit_WidthB.setEnabled(False)
            self.lineEdit_HeightB.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.lineEdit_selectMotionFIle.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)

        
        if self.radioButton_createSector.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_WidthA.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(True)
            self.lineEdit_AngleA_end.setEnabled(True)
            self.checkBox_squareFillIn.setEnabled(False)

            self.lineEdit_WidthB.setEnabled(False)
            self.lineEdit_HeightB.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.lineEdit_selectMotionFIle.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)
       
        
        if self.radioButton_createDirection.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(True)
            self.lineEdit_WidthA.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)

            self.lineEdit_WidthB.setEnabled(True)
            self.lineEdit_HeightB.setEnabled(True)
            self.lineEdit_directionDegree.setEnabled(True)
            self.lineEdit_directionSpread.setEnabled(True)
            self.lineEdit_selectCurve.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)

            self.lineEdit_selectMotionFIle.setEnabled(False)
            self.lineEdit_RadiusA.setText("2000")
          
            self.lineEdit_WidthB.setText("0")
            self.lineEdit_HeightB.setText("0")
            
                                
        if self.radioButton_createFollowCurve.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_WidthA.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)

            self.lineEdit_WidthB.setEnabled(False)
            self.lineEdit_HeightB.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(True)
            self.lineEdit_selectMotionFIle.setEnabled(False)
            self.toolButton_selectCurve.setEnabled(True)
            ## groupBox_keysOption
            self.groupBox_keysOption.setEnabled(True)
            self.lineEdit_keysA.setEnabled(True)
            self.lineEdit_NoiseA.setEnabled(True)
            self.lineEdit_pow.setEnabled(True)

            
                                                                
        if self.radioButton_createFromImageWeight.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_WidthA.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)

            self.lineEdit_WidthB.setEnabled(False)
            self.lineEdit_HeightB.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.lineEdit_selectMotionFIle.setEnabled(True)

            
                                
                                
                                        
    def modifyDynamicState(self):
        if self.checkBox_dynamic.isChecked() == True:
            self.groupBox.setEnabled(True)
            self.groupBox_keysOption.setEnabled(False)

            self.lineEdit_RadiusA.setEnabled(True)

            
        else:
            
            self.groupBox.setEnabled(False)


        
        
 #   def creatJoint(self,x,y,w,h): createRadiation
        

    
    #create joints with plane(slot) or copy key from other object
    def createJoints(self):
        self.statusbar.clearMessage()
        print "create joints"
        jointAmount = int(self.lineEdit_numberJoints.text())
        
        proxyName =  str(self.lineEdit_jointName.text()) 
        tempJointList = cmds.ls(type="joint")
        jointList= []
        for i in tempJointList:
           # print i
            jointList.append(i.split("|")[-1].split("_")[0])
       
        print jointList
        count = 0 
        for i in jointList:
            proxyTempName = i+"_"
            if proxyTempName == proxyName:
                count = count +1
        print "count",count
        
        createdJointList = []
        slotPlaneList = []
        for i in range(0,jointAmount):
            sn = count + 1+i
            proxyNameSN = proxyName +"%03d"%sn


            
            
            joint = cmds.createNode("joint",n= proxyNameSN)
            cmds.addAttr( longName='spineAttribute', numberOfChildren=8, attributeType='compound' )
            cmds.addAttr( longName='slotName', dataType="string",parent='spineAttribute')

            cmds.addAttr( longName='alphaGain', attributeType='float',defaultValue=1.0, minValue=0.0, maxValue=1.0,parent='spineAttribute',k=True)
            cmds.addAttr( longName='fadeGain', attributeType='float',defaultValue=1.0, minValue=0.0, maxValue=1.0,parent='spineAttribute',k=True)

            cmds.addAttr(longName='colorGain', usedAsColor=True, attributeType='float3',parent='spineAttribute' )
            cmds.addAttr( longName='redColorGain', attributeType='float', defaultValue=1.0, parent='colorGain' )
            cmds.addAttr( longName='greenColorGain', attributeType='float',defaultValue=1.0, parent='colorGain' )
            cmds.addAttr( longName='blueColorGain', attributeType='float',defaultValue=1.0, parent='colorGain' )
            cmds.addAttr(longName='darkColor', usedAsColor=True, attributeType='float3',parent='spineAttribute' )
            cmds.addAttr( longName='redDarkColor', attributeType='float', defaultValue=0.0, parent='darkColor' )
            cmds.addAttr( longName='greenDarkColor', attributeType='float',defaultValue=0.0, parent='darkColor' )
            cmds.addAttr( longName='blueDarkColor', attributeType='float',defaultValue=0.0, parent='darkColor' )
            cmds.addAttr( longName='slotW', attributeType='long',defaultValue=50, minValue=0, maxValue=2048,parent='spineAttribute')
            cmds.addAttr( longName='slotH', attributeType='long',defaultValue=50, minValue=0, maxValue=2048,parent='spineAttribute')
            cmds.addAttr( longName='blendMode', attributeType='enum',en="normal:additive:multiply:screen",parent='spineAttribute',k=True)
            createdJointList.append(joint)
            
            if self.checkBox_witImagePlanes.isChecked() == True:
                slotWidth = int(self.lineEdit_imageWidth.text())
                slotHeight = int(self.lineEdit_imageHeight.text())
                print "slotWidth",slotWidth,"slotHeight",slotHeight
                slotName = proxyName +"sl_"+"%03d"%sn
               # print "slotName",slotName,"proxyNameSN",proxyNameSN
                 
                slotPlane = cmds.polyPlane(n= slotName,sx=1, sy=1, w=1, h=1)
                slotPlaneList.append(slotPlane[0])
                
                shapeName =cmds.listRelatives(slotPlane,c=True)
               # print "slotPlane",slotPlane,"shapeName",shapeName,"proxyNameSN",proxyNameSN
                allMeshList = []
                for i in cmds.ls(type="mesh"):
                    allMeshList.append(i.split("|")[-1])
                    
              #  print allMeshList radioButton_createSquarre

              #  print "shapeName",shapeName
                if shapeName in allMeshList:
                    self.statusbar.showMessage("more than one %s"%shapeName)
                    
                    self.statusbar.setStyleSheet("\
                                                QStatusBar {\
                                                    color: rgb(255,0,0);\
                                                    border-color: rgb(60,80,80); \
                                                    font-size: 14px;\
                                                }\
                                                ")
                    print "more than one %s"%shapeName
                    
                else:

                    
                    cmds.setAttr("%s.scaleX"%slotName,slotWidth)
                    cmds.setAttr("%s.scaleZ"%slotName,slotHeight)
                    cmds.setAttr("%s.rotateX"%slotName,90)
                    cmds.parent(slotName,proxyNameSN)
                    self.statusbar.showMessage("joint %s and slot %s created"%(proxyNameSN,slotName))
                    
                    self.statusbar.setStyleSheet("\
                                                QStatusBar {\
                                                    color: rgb(255,255,255);\
                                                    border-color: rgb(60,80,80); \
                                                    font-size: 14px;\
                                                }\
                                                ")
                    
                    

            else:
                pass
        print "slotPlaneList",slotPlaneList   
        if self.checkBox_getShader.isChecked()== True:
            
            selectShader = self.comboBox.currentText()
            shaderSG = cmds.sets(renderable=True,noSurfaceShader=True,empty=True)
            cmds.select(shaderSG)
            newSGNameTemp= selectShader+"_SG#"
            newSGName = cmds.rename(shaderSG,newSGNameTemp)
            print "shaderSG",shaderSG,newSGName

            cmds.connectAttr("%s.outColor"%selectShader,"%s.surfaceShader"%newSGName)
            '''
            try:
                shaderSG = cmds.listConnections(selectShader,t="shadingEngine")[0]
            except:
                print "connect shadingEngine to shader"
                pass
            '''   
            #getShaderSelected = self.comboBox.currentText()
            for obj in slotPlaneList:
           # print allMeshList,shaderSG
                print "obj,newSGName",obj,newSGName
               # cmds.select(obj)
                
               # cmds.sets("shine_L5_sl_001", e=True, fe="lambert2_SG1")
                cmds.sets(obj, e=True, fe=newSGName)

        if self.checkBox_dynamic.isChecked() == True:
            
            if self.radioButton_createRad.isChecked() ==True:
                print "Radiation shape"
                
                self.setToRadiation(createdJointList)
                
                
            elif self.radioButton_createSquare.isChecked() == True:
                self.setSquare(createdJointList)
           
            elif self.radioButton_createSector.isChecked() == True:
                print "Sector shape"
                self.setSector(createdJointList)
            elif self.radioButton_createDirection.isChecked() == True:
                self.setDirection(createdJointList)
                
            elif self.radioButton_createFollowCurve.isChecked() == True:
                self.setAlongCurve(createdJointList)
                                
  
  
    def getDagPath(self,node=None):
        sel = om.MSelectionList()
        sel.add(node)
        curveFn = om.MDagPath()
        sel.getDagPath(0, curveFn)
        return curveFn



        
                
                
    def setAlongCurve(self,jointList):
      #  print "setAlongCurve"
        self.statusbar.clearMessage()
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        frameTotal = endFrame - startFrame
        keys =  int(self.lineEdit_keysA.text())
        noise = float(self.lineEdit_NoiseA.text())
        selectCurve = self.allSelectCurveList
        #selecturve = self.getCurves()
        print "selectCurve",selectCurve,type(selectCurve)
        
        powNum = float(self.lineEdit_pow.text())
        #print keys,noise,logNum getCurves
       
        newFrameTable = []
        yStepTable = []
        for i in range(0,keys):
            y = math.pow(i,powNum)
            yStepTable.append(y)
        print yStepTable
        
        for i in yStepTable:
            newFrame = ((i - yStepTable[0])/(yStepTable[-1]-yStepTable[0]))*(endFrame-startFrame) + startFrame
            newFrameTable.append(newFrame)
        print "newFrameTable",newFrameTable  
         
        if len(selectCurve) == 0:
            pass

        else:

            for jointIndex in range(0,len(jointList)):
                joint = jointList[jointIndex]
                
                curveIndex = jointIndex % len(selectCurve)
                curve = selectCurve[curveIndex]
                print "joint",joint,"selectCurve",curve
                
                
                curveFn = om.MFnNurbsCurve(self.getDagPath("%s"%curve))
               # curveFn = om.MFnNurbsCurve(self.getDagPath("curve5"))

                print "curve",curve,"joint",joint
                k = 1.0/float(keys-1)                   
                
                
                for i in range(0,keys):
                    frame = newFrameTable[i]
                    noiseX = random.uniform(-noise,noise)
                    noiseY = random.uniform(-noise,noise)

                   # parameter = curveFn.findParamFromLength(curveFn.length() * k * (i+1))
                    parameter = curveFn.findParamFromLength(curveFn.length() * k * (i))

                    point = om.MPoint()
                    curveFn.getPointAtParam(parameter, point)
                    cmds.setKeyframe(joint, t=[frame,frame], at="translateX",v=(point.x + noiseX) )
                    cmds.setKeyframe(joint, t=[frame,frame], at="translateY",v=(point.y +noiseY) )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
                  
                    
   
    def setDirection(self,jointList):
        print "set to direction"
        originX = int(self.lineEdit_WidthB.text())
        originY = int(self.lineEdit_HeightB.text())
        directionDegree = float(self.lineEdit_directionDegree.text())
        directionSpread = float(self.lineEdit_directionSpread.text())
        radius = int(self.lineEdit_RadiusA.text())

        
        amount = len(jointList)
       # jointAmount = int(self.lineEdit_shapeStartFrame.text())
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())


        
        for i in range(0,amount):
            rad = (directionDegree *math.pi)/180 + (random.uniform(-directionSpread,directionSpread)*math.pi)/180
            x = originX + int(radius * math.cos(rad))
            y = originY + int(radius * math.sin(rad))

            joint = jointList[i]
            #print 'joint',joint
            cmds.setAttr("%s.translateX"%joint,x)
            cmds.setAttr("%s.translateY"%joint,y)
            cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateX",v=x )
            cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateY",v=y )        
            cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=originX )
            cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=originY )    
            cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0)
            cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
            cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
            cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=0)
            cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
            cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
              
                
    
    def setSector(self,jointList):
        print "sector shape"
        
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        amount = len(jointList)
        sectorStartAngle = int(self.lineEdit_AngleA_start.text())
        sectorEndAngle = int(self.lineEdit_AngleA_end.text())
        angleMax = sectorEndAngle - sectorStartAngle
        angleStep = int(angleMax/amount)
        if self.checkBox_offsetRandom_2.isChecked() == True:
            for i in range(0,amount):
                joint = jointList[i]

                angle = random.randint(sectorStartAngle,sectorEndAngle)
              #  print "angle",angle
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0 )       

                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=angle )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=0)
                cmds.setKeyframe(joint, t=[endFrame,startFrame], at="translateX",v=0)
                cmds.setKeyframe(joint, t=[endFrame,startFrame], at="translateY",v=0)

                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
                  
                    
        else:
            for i in range(0,amount):
                joint = jointList[i]

                angle = sectorStartAngle + angleStep*i
              #  print "angle",angle
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0 )       

                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=angle )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=0)
                cmds.setKeyframe(joint, t=[endFrame,startFrame], at="translateX",v=0)
                cmds.setKeyframe(joint, t=[endFrame,startFrame], at="translateY",v=0)
                  
                    

    

    def setSquare(self,jointList):
        print "square shape"
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        width = int(self.lineEdit_WidthA.text())
        height = int(self.lineEdit_HeightA.text())
        amount = len(jointList)
        if self.checkBox_squareFillIn.isChecked() == True:
            for i in range(0,amount):
                joint = jointList[i]
                x= random.randint(-int(width/2),int(width/2)+1)
                y= random.randint(-int(height/2),int(height/2)+1)
                print "square fill in X Y",x,y
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateX",v=x )
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateY",v=y )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=0 )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=0 )       
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)               
            
            pass
        else:
            for i in range(0,amount):
                sideIndex = random.randint(0,3)
             #   print sideIndex 

                if sideIndex == 0:
                    x= random.randint(int(-width/2),int(width/2))
                    y = int(height/2)
                elif sideIndex == 1:
                    x= int(width/2)
                    y = random.randint(int(-height/2),int(height/2))
                     
                elif sideIndex == 2:
                    x= random.randint(int(-width/2),int(width/2))
                    y = -int(height/2)
                    
                    
                elif sideIndex == 3:
                    x= -int(width/2)
                    y = random.randint(int(-height/2),int(height/2))

                joint = jointList[i]
                   # print 'joint',joint
                  #  cmds.setAttr("%s.translateX"%joint,x)
                  #  cmds.setAttr("%s.translateY"%joint,y)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateX",v=x )
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateY",v=y )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=0 )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=0 )       
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
                  
                
                
    def setToRadiation(self,jointList):
        
        radius = int(self.lineEdit_RadiusA.text())
        amount = len(jointList)
       # jointAmount = int(self.lineEdit_shapeStartFrame.text())
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        print startFrame,endFrame

        if self.checkBox_offsetRandom_2.isChecked() == True:
            for i in range(0,amount):
               
                rad =  random.uniform(0,math.pi*2) 
                x = radius * math.cos(rad)
                y = radius * math.sin(rad)

                joint = jointList[i]
               # print 'joint',joint
                cmds.setAttr("%s.translateX"%joint,x)
                cmds.setAttr("%s.translateY"%joint,y)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateX",v=x )
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateY",v=y )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=0 )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=0 )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
                  
                    
        else:
            for i in range(0,amount):
                dag = (360.0 / float(amount))*float(i)
              #  print dag
                rad = (dag *math.pi)/180
                x = radius * math.cos(rad)
                y = radius * math.sin(rad)
                joint = jointList[i]
                #print 'joint',joint
                cmds.setAttr("%s.translateX"%joint,x)
                cmds.setAttr("%s.translateY"%joint,y)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateX",v=x )
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="translateY",v=y )        
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateX",v=0 )
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="translateY",v=0 )            
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[startFrame,startFrame], at="scaleY",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="rotateZ",v=0)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleX",v=1)
                cmds.setKeyframe(joint, t=[endFrame,endFrame], at="scaleY",v=1)
                  
                    
        

    def modifyAllAttrStateDict(self):
      #  print "modify all key" 
        if self.checkBox_modify_all.isChecked() == True:
         #   print "all on"
            self.checkBox_translateX.setChecked(True)
            self.checkBox_translateY.setChecked(True)
            self.checkBox_translateZ.setChecked(True)
            self.checkBox_rotateX.setChecked(True)
            self.checkBox_rotateY.setChecked(True)
            self.checkBox_rotateZ.setChecked(True)
            self.checkBox_scaleX.setChecked(True)
            self.checkBox_scaleY.setChecked(True)
            self.checkBox_scaleZ.setChecked(True)
            self.checkBox_modify_alphaGain.setChecked(True)
            self.checkBox_modify_colorGain.setChecked(True)
            

        else:
         #   print "all off"
            self.checkBox_translateX.setChecked(False)
            self.checkBox_translateY.setChecked(False)
            self.checkBox_translateZ.setChecked(False)
            self.checkBox_rotateX.setChecked(False)
            self.checkBox_rotateY.setChecked(False)
            self.checkBox_rotateZ.setChecked(False)
            self.checkBox_scaleX.setChecked(False)
            self.checkBox_scaleY.setChecked(False)
            self.checkBox_scaleZ.setChecked(False)
            self.checkBox_modify_alphaGain.setChecked(False)
            self.checkBox_modify_colorGain.setChecked(False)
                        
        if self.checkBox_modify_unlockAll.isChecked() == True:
            self.checkBox_translateX.setEnabled(True)
            self.checkBox_translateY.setEnabled(True)
            self.checkBox_translateZ.setEnabled(True)
            self.checkBox_rotateX.setEnabled(True)
            self.checkBox_rotateY.setEnabled(True)
            self.checkBox_rotateZ.setEnabled(True)
            self.checkBox_scaleX.setEnabled(True)
            self.checkBox_scaleY.setEnabled(True)
            self.checkBox_scaleZ.setEnabled(True)
            #self.checkBox_modify_alphaGain.setEnabled(True)
            #self.checkBox_modify_colorGain.setEnabled(True)
        else:
            
            self.checkBox_translateX.setEnabled(True)
            self.checkBox_translateY.setEnabled(True)
            self.checkBox_translateZ.setEnabled(False)
            self.checkBox_rotateX.setEnabled(False)
            self.checkBox_rotateY.setEnabled(False)
            self.checkBox_rotateZ.setEnabled(True)
            self.checkBox_scaleX.setEnabled(True)
            self.checkBox_scaleY.setEnabled(True)
            self.checkBox_scaleZ.setEnabled(False)
            
            
            

        
    def setAllTransformUnChecked(self):
       # valueList= [tx,ty,tz,sx,sy,sz,rx,ry,rz]
        self.checkBox_translateX.setChecked(False)
        self.checkBox_translateY.setChecked(False)
        self.checkBox_translateZ.setChecked(False)
        self.checkBox_rotateX.setChecked(False)
        self.checkBox_rotateY.setChecked(False)
        self.checkBox_rotateZ.setChecked(False)
        self.checkBox_scaleX.setChecked(False)
        self.checkBox_scaleY.setChecked(False)
        self.checkBox_scaleZ.setChecked(False)
        
    def modifyTranslateAttrStateDict(self):
        self.checkBox_rotateX.setChecked(False)
        self.checkBox_rotateY.setChecked(False)
        self.checkBox_rotateZ.setChecked(False)
        self.checkBox_scaleX.setChecked(False)
        self.checkBox_scaleY.setChecked(False)
        self.checkBox_scaleZ.setChecked(False)
                
        
        
        
        
    def modifyAttrStateDict(self):
    #    print " modifyAttrStateDict" checkBox_scaleAll 

        if self.checkBox_translateX.isChecked() == True:


            self.attrCheckStateDict["translateX"] = 1

        else:
            self.attrCheckStateDict["translateX"] = 0
            
        if self.checkBox_translateY.isChecked() == True:


            self.attrCheckStateDict["translateY"] = 1

        else:
            self.attrCheckStateDict["translateY"] = 0            
            
        if self.checkBox_translateZ.isChecked() == True:
            self.attrCheckStateDict["translateZ"] = 1



        else:
            self.attrCheckStateDict["translateZ"] = 0        
            
            
        
        if self.checkBox_rotateX.isChecked() == True:
            self.attrCheckStateDict["rotateX"] = 1   

                                
        else:
            self.attrCheckStateDict["rotateX"] = 0       
                                      
        if self.checkBox_rotateY.isChecked() == True:
            self.attrCheckStateDict["rotateY"] = 1


        else:
            self.attrCheckStateDict["rotateY"] = 0    
                                           
        if self.checkBox_rotateZ.isChecked() == True:
            self.attrCheckStateDict["rotateZ"] = 1


        else:
            self.attrCheckStateDict["rotateZ"] = 0                                   
 

                                
        if self.checkBox_scaleX.isChecked() == True:
            self.attrCheckStateDict["scaleX"] = 1



        else:
            self.attrCheckStateDict["scaleX"] = 0                                   
                                        
        if self.checkBox_scaleY.isChecked() == True:

            self.attrCheckStateDict["scaleY"] = 1

        else:
            self.attrCheckStateDict["scaleY"] = 0                                   
                                        
       # if self.checkBox_scaleZ.isChecked() == True:
      #      self.attrCheckStateDict["scaleZ"] = 1


      #  else:
      #      self.attrCheckStateDict["scaleZ"] = 0                                   

        if self.checkBox_alphaGain.isChecked() == True:
            self.attrCheckStateDict["alphaGain"] = 1

        else:
            self.attrCheckStateDict["alphaGain"] = 0                                   
                                        
        if self.checkBox_colorGain.isChecked() == True:
            self.attrCheckStateDict["colorGain"] = 1

        else:
            self.attrCheckStateDict["colorGain"] = 0                                   
    
    
    
     
        if self.checkBox_scaleAll.isChecked() == True:
            self.attrCheckStateDict["scaleX"] = 1
            self.attrCheckStateDict["scaleY"] = 1



        else:
            self.attrCheckStateDict["scaleX"] = 0       
            self.attrCheckStateDict["scaleY"] = 0       
 
                                        
        print self.attrCheckStateDict["scaleX"]
        print self.attrCheckStateDict["scaleY"]

   #    print self.attrCheckStateDict

    def setAttrStateList(self):
        if self.checkBox_translateX.isChecked() == True:
            print "translate X is selected"
            if "translateX" not in self.attrCheckStateList:
                self.attrCheckStateList.append("translateX")
            else:
                pass
                
        else:
            try:
                self.attrCheckStateList.remove("translateX")
                print "translate X is unselected"
            except:
                pass
        print "self.attrCheckStateList",self.attrCheckStateList
    def modifyJointInputText(self):
    
        print "create Joints"
        
        jointAmount = int(self.lineEdit_numberJoints.text())
       # emitJointAmount = int(self.lineEdit_numberJoints_2.text())

       # print jointAmount
       # self.lineEdit_numberJoints.setText("ffdf") horizontalSlider_numberJoints_2
        
        self.horizontalSlider_numberJoints.setValue(jointAmount)
       # self.horizontalSlider_numberJoints_2.setValue(emitJointAmount)

        
    def modifyJointInputSlider(self):
        
       # print "slide change"
        
        jointAmount = int(self.horizontalSlider_numberJoints.value())

        keys = int(self.horizontalSlider_keysA.value())
       # print keys
        noise = float(float(self.horizontalSlider_NoiseA.value())/1.0)
       # print noise

        log = float(float(self.horizontalSlider_powA.value())/10.0)
       # print log

        self.lineEdit_numberJoints.setText(str(jointAmount))
        self.lineEdit_keysA.setText(str(keys))
        self.lineEdit_NoiseA.setText(str(noise))
        self.lineEdit_pow.setText(str(log))
                
        
       # emitJointAmount = int(self.horizontalSlider_numberJoints_2.value()) horizontalSlider_NoiseA
 
       # self.lineEdit_numberJoints_2.setText(str(emitJointAmount))

        
        
        
    def modifyKeyValue(self):
        print "modify select key Attribute"
       # if self.checkBox_translateX.isChecked() == True:
            
        #if self.checkBox_translateX.isChecked() == True: lineEdit_modifyValue
        frameList = self.lineEdit_modifyFrame.text().split(",")
       # valueList = self.lineEdit_modifyValue.text().split(",")
        objList = cmds.ls(sl=True,l=True)
        minValue = float(self.lineEdit_minValue.text())
        maxValue = float(self.lineEdit_maxValue.text())
        
        modifyAttrList=[]
        for attr in self.attrCheckStateDict.keys():
            if self.attrCheckStateDict[attr] == 1:
                modifyAttrList.append(attr)
              #  print attr
        
        print modifyAttrList
        
        print "frameList",frameList
     #   print valueList
     #   print objList
     #   print self.attrCheckStateDict
        for obj in objList:  
            for attr in modifyAttrList:
                keyframeList =  cmds.keyframe( obj,at=attr, query=True) 
                offsetValue =  random.uniform(minValue,maxValue)
                print "keyframeList",obj,attr,keyframeList
                
              #  print offsetValue
                if frameList[0] == "all":
                    for frame in keyframeList:
                        frameValue = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]
                        print attr,frame,frameValue
                        if self.radioButton_offsetV.isChecked() == 1:
                            
                            if attr == "scaleX":
                                changeValue = offsetValue * frameValue
                            elif attr == "scaleY":
                                changeValue = offsetValue * frameValue
                            elif attr == "scaleZ":
                                changeValue = offsetValue * frameValue
                            else:
                                changeValue = offsetValue + frameValue
                          #  print changeValue
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=changeValue )
                        else:
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=offsetValue )
                        if self.checkBox_scaleAll.isChecked() == True:
                            
                            frameScaleValue = cmds.keyframe(obj,at="scaleX",t=(frame,frame),q=True,eval=True)[0]
                            cmds.setKeyframe(obj, t=[frame,frame], at="scaleY",v=frameScaleValue )
                            cmds.setKeyframe(obj, t=[frame,frame], at="scaleX",v=frameScaleValue )

                        else:
                            pass

                            
                            
                    
                else:
                    for indexNum in frameList:
                        frame = keyframeList[int(indexNum)]
                        
                        frameValue = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]
                       # print attr,frame,startFrameValue checkBox_square
                        if self.radioButton_offsetV.isChecked() == 1:
                            print "modify value depend on key index"
                            if attr == "scaleX":
                                changeValue = offsetValue * frameValue
                            elif attr == "scaleY":
                                changeValue = offsetValue * frameValue
                            elif attr == "scaleZ":
                                changeValue = offsetValue * frameValue
                            else:
                                changeValue = offsetValue + frameValue

                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=changeValue )
                        else:
                            cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=offsetValue )     
                        
                        if self.checkBox_scaleAll.isChecked() == True:
                            
                            frameScaleValue = cmds.keyframe(obj,at="scaleX",t=(frame,frame),q=True,eval=True)[0]
                            cmds.setKeyframe(obj, t=[frame,frame], at="scaleY",v=frameScaleValue )
                            cmds.setKeyframe(obj, t=[frame,frame], at="scaleX",v=frameScaleValue )

                        else:
                            pass

                        

            
            

    def alignKeys(self):
        print "alignKeys"
        objList = self.getObjList()
        alignFrame = float(self.lineEdit_alignKey.text())  
       # print objList
        for obj in objList:
         #   print obj
            keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            for key in tempKeyFrameList:
                if key in keyFrameList:
                    pass
                else:
                    keyFrameList.append(key)

            if alignFrame <= keyFrameList[0]:  #align keyframe when align frame <= first keyframe
                for i in range(0,len(keyFrameList)):
                    originalFrame = keyFrameList[i]
                    newKeyFrame = i +alignFrame

                    try:
                        cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))
                    except:
                        pass
            else:
                offsetFrame =alignFrame -keyFrameList[0] #align keyframe when align frame > first keyframe
                print keyFrameList
                resveredKeyFrameList = list(reversed(keyFrameList))
                for i in range(0,len(keyFrameList)):
                    originalFrame =  resveredKeyFrameList[i]
                    
                    newKeyFrame = originalFrame +offsetFrame

                    cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))


    def scaleFrames(self):
        
        originalIn = float(self.lineEdit_originalIn.text())
        originalOut = float(self.lineEdit_originalOut.text())
        newIn = float(self.lineEdit_newIn.text())
        newOut = float(self.lineEdit_newOut.text())
        objList = self.getObjList()
    #    print originalIn,originalOut,newIn,newOut
        if originalOut - originalIn > 0 and newOut-newIn >0:
            originalAmount = originalOut -originalIn
            newAmount = newOut-newIn
            for obj in objList:
              #  keyFrameList= []
              #  tempKeyFrameList = cmds.keyframe(obj,q=True)            
                cmds.scaleKey( obj, time=(originalIn,originalOut), newStartTime=newIn, newEndTime= newOut)


           # print originalIn,originalOut,newIn,newOut
        else:
            print "not illegal frame pls check again"
            

           

        

    def trimAfterFrame(self):
        print "cutKeys"
        objList = self.getObjList()
        keepRange = int(self.lineEdit_trimAfterFrame.text())
       # cutStartFrame = float(cutFrames.split(",")[0])
        #cutEndFrame = float(cutFrames.split(",")[1])
       # print keepRange
        for obj in objList:
            keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            for key in tempKeyFrameList:
                if key in keyFrameList:
                    pass
                else:
                    keyFrameList.append(key)
            totalFrames= len(keyFrameList)
            for i in range(keepRange,totalFrames):
                frame = keyFrameList[i]
              #  print frame
                cmds.cutKey( obj, time=(frame,frame),option="keys" )
                
                

    def trimBeforeFrame(self):
        print "cutKeys"
        objList = self.getObjList()
        keepRange = int(self.lineEdit_trimBeforeFrame.text())
       # cutStartFrame = float(cutFrames.split(",")[0])
        #cutEndFrame = float(cutFrames.split(",")[1])
       # print keepRange
        for obj in objList:
            keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            for key in tempKeyFrameList:
                if key in keyFrameList:
                    pass
                else:
                    keyFrameList.append(key)
            totalFrames= len(keyFrameList)
            for i in range(0,keepRange):
                frame = keyFrameList[i]
              #  print frame
                cmds.cutKey( obj, time=(frame,frame),option="keys" )
                
                
                                
        
    
    def offsetKeyFrames(self):
        cmds.currentTime(0,e=True)
        offsetStartFrame = float(self.lineEdit_offfsetStartFrame.text())
        offsetEndFrame = float(self.lineEdit_offfsetendFrame.text())
       # offsetValue = float(self.lineEdit_offsetFrame.text())

        #divideNextFrame  = divideFrame +1 divideFrame

        keyFrameLength = offsetEndFrame-offsetStartFrame +1.0
        print "offsetKeyFrames"
        
        keyAbleAttList=["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ","alphaGain"] #["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]
        objList = self.getObjList()
        
        for obj in objList:
            if self.checkBox_offsetRandom.isChecked() == False:
                offsetValue = int(self.lineEdit_offsetFrame.text())
            else:
                offsetValue = random.randint(0,int(self.lineEdit_offsetFrame.text()))
    
            divideFrame = offsetStartFrame + offsetValue 
            divideStepFrame = divideFrame+0.01-1


          #  print obj offsetValue cmds.findKeyframe("bone_0021",at ="translateZ" )
           # if 
            for attr in keyAbleAttList :

              #  print attr,offsetStartFrame,offsetEndFrame,startFrameValue,endFrameValue
                try:
                    keyCount =  len(cmds.keyframe(obj,at=attr,q=True)) 
                except:
                    keyCount = 0 
                    
                print "attr",attr,"keyCount",keyCount
                if keyCount == 0 :
                    pass
                else:
                    try:
                        startFrameValue = cmds.keyframe(obj,at=attr,t=(offsetStartFrame,offsetStartFrame),q=True,eval=True)[0] # get startFrame value
                        endFrameValue = cmds.keyframe(obj,at=attr,t=(offsetEndFrame,offsetEndFrame),q=True,eval=True)[0] # get endFrame value
                        
                        cmds.setKeyframe(obj, t=[offsetStartFrame,offsetStartFrame], at=attr,v=startFrameValue ) #setKey to startFrame
                        cmds.setKeyframe(obj, t=[offsetEndFrame,offsetEndFrame], at=attr,v=endFrameValue ) #setKey to endFrame
                        
                                      
                        keyValueDict = {}
                        offsetKeyFrameDict={}
                        keyFrameList = cmds.keyframe(obj,at=attr,q=True)
                        frameBeNewEndFrame = offsetEndFrame - offsetValue
                        newEndFrameValue =  cmds.keyframe(obj,at=attr,t=(frameBeNewEndFrame,frameBeNewEndFrame),q=True,eval=True)[0]
                        frameBeNewStartFrame = frameBeNewEndFrame +1
                        newStartFrameValue =  cmds.keyframe(obj,at=attr,t=(frameBeNewStartFrame,frameBeNewStartFrame),q=True,eval=True)[0]

                            
                   #     divideFrame = offsetEndFrame - offsetValue
                       # modOffsetStepPreKeyFrame = float(offsetEndFrame - offsetValue -0.01)
                      #  modOffsetStepPosteKeyFrame = float(offsetEndFrame - offsetValue+0.01)
                       # divideFrameValue = cmds.keyframe(obj,at=attr,t=(divideFrame,divideFrame),q=True,eval=True)[0]
                     #   postKeyFrameValue = cmds.keyframe(obj,at=attr,t=(divideFrame,divideFrame),q=True,eval=True)[0]
                        #cmds.setKeyframe(obj, t=[modOffsetStepPreKeyFrame,modOffsetStepPreKeyFrame], at=attr,v=divideFrameValue )

                       # cmds.setKeyframe(obj, t=[modOffsetStepPosteKeyFrame,modOffsetStepPosteKeyFrame], at=attr,v=divideFrameValue )
                        
                     #   cmds.setKeyframe(obj, t=[divideFrame,divideFrame], at=attr,v=divideFrameValue )

       
                    except:
                        pass


                   # print "keyFrameList",keyFrameList
                    
                    try:
                        keyFrameLength =  float(keyFrameList[-1]-keyFrameList[0]+1.0)
                        startFrame = float(keyFrameList[0])
                       # print "%.2f"%keyFrameLength
                        endFrame = float(keyFrameList[-1])
                        
                        
                    #    print startFrame,endFrame
                                        
                        for i in keyFrameList:
                            getValue = float(cmds.keyframe(obj,at= attr,time=(i,i) ,query=True,ev=True)[0])

                            keyValueDict.update({"%.2f"%i:"%.2f"%getValue})
                            
                            

           

                            
                        for i in keyFrameList:
                            totalValue = float(i + offsetValue)
                            
                            if totalValue <= offsetEndFrame:
                                
                                newKey = totalValue
                              #  print "aaa"
                            else:
                                newKey = totalValue -offsetEndFrame + offsetStartFrame -1
                                
                          #  if i == 
                          #  print "newKey",keyFrameLength,i,newKey
                            #newKey = 
                            offsetKeyFrameDict.update({"%.2f"%i:"%.2f"%newKey})
                        
       
                        
                    except:
                        keyFrameLength = 0
                        
                        
                    try:#clear key in channel
                        print "clear key"
                        cmds.cutKey( obj, time=(keyFrameList[0],keyFrameList[-1]), attribute=attr, option="keys" )
                    except:
                        pass
                 #   print "offsetKeyFrameDict",offsetKeyFrameDict

                   # print keyFrameList[0]

                    try:
                        for key in keyFrameList:
                            offsetKey = float(offsetKeyFrameDict["%.2f"%key])
                          #  print key,offsetKey ,type(offsetKey),type("%.2f"%key)
                            setValue = float(keyValueDict["%.2f"%key])
                          #  print key,offsetKey,setValue ,type(setValue),attr,obj
                            cmds.setKeyframe(obj,v=setValue,at=attr,time=(offsetKey,offsetKey))
                         #   print "done"
                        cmds.setKeyframe(obj,v=startFrameValue,at=attr,time=(divideStepFrame,divideStepFrame))
                        cmds.setKeyframe(obj,v=newEndFrameValue,at=attr,time=(offsetEndFrame,offsetEndFrame))
                        cmds.setKeyframe(obj,v=newStartFrameValue,at=attr,time=(offsetStartFrame,offsetStartFrame))

                    except:
                        pass
                 #   print attr,keyFrameLength,keyFrameList

        for obj in objList: 
            keyFrameList = cmds.keyframe(obj,at=attr,q=True)
            firstFrame = keyFrameList[0]
            lastFrame = keyFrameList[-1]

            for attr in keyAbleAttList:
                try:
                    getValue = cmds.keyframe(obj,at= attr,time=(firstFrame,firstFrame) ,query=True,ev=True)[0]
                    cmds.setKeyframe(obj,v=getValue,at= attr,time=(lastFrame,lastFrame))
                except:
                    pass

            
    def getObjList(self):
        
        objList = cmds.ls(sl=True)
        
        return objList
        

    def getItems(self):
        
       # print self.checkBox_allzero.isChecked()
        objList = cmds.ls(sl=True)
        for obj in objList:
           # print obj
            self.cycleKeys(obj)
        
        
    def cycleKeys(self,obj):
        print obj
        offsetIn = float(self.lineEdit_sf.text())
        offsetOut = float(self.lineEdit_ef.text())
        repeatTimes = int(self.lineEdit_rt.text())
        keyAbleAttList= ["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]
        
        if self.checkBox_allzero.isChecked() == True:
            for attr in keyAbleAttList :
                keyFrameList = cmds.keyframe(obj,at=attr,q=True)
                preStartFrame = float(keyFrameList[0]) - 0.01
                postEndFrame = float(keyFrameList[-1]) + 0.01
                cmds.setKeyframe(obj,v=0,at=attr,time=(preStartFrame,preStartFrame))
                cmds.setKeyframe(obj,v=0,at=attr,time=(postEndFrame,postEndFrame))
                #print attr,preStartFrame,postEndFrame
                print attr,keyFrameList
                
            
        
        for attr in keyAbleAttList:
            keyFrameList = cmds.keyframe(obj,at=attr,q=True)
            startKeyFrame = keyFrameList[0]
            endKeyFrame = keyFrameList[-1]
            offsetRange = offsetOut -offsetIn +1
           # print attr,keyFrameList,startKeyFrame,endKeyFrame
            for i in range(0,repeatTimes):
                for j in keyFrameList:
                    frame = i*offsetRange + j
                   # print"attr",attr, i*offsetRange + j
                    getValue = float(cmds.keyframe(obj,at= attr,time=(j,j) ,query=True,ev=True)[0])
                    cmds.setKeyframe(obj,v=getValue,at=attr,time=(frame,frame))
                    print getValue
        
    
    
    
    
    
    
    
    
    
    
        
def keyFrameToolMain():
#def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
#if __name__ == '__main__':
#    main()


 