# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/UI/dock_01.ui'
#
# Created: Thu Jul 19 21:51:31 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets#.QFileSystemModel
import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as mui
import shiboken2
import random


#from PySide2.QtCore import QString
import os,math,json,shutil
import sys,subprocess
try:
   ## sys.path.append("C:/Program Files/Pixar/RenderManProServer-22.1/lib/python2.7/Libs/ite-packages")
    #sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.7/lib/python2.7/Lib/site-packages")
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/22")
    sys.path.append("C:/Users/alpha/Documents/GitHub/spineToolAdv")

    import ice
    import spineUI_A
    reload(spineUI_A)
except:
    pass
     

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))

        print ('1',MainWindow)


class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        spineUI_A.buildDock(self)
        spineUI_A.defineImageButtonDock(self,16)
        
        
        
#def spineToolMain():
def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main()

