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
import os,math,json
import sys,subprocess
try:
    sys.path.append("C:/Program Files/Pixar/RenderManProServer-22.1/lib/python2.7/Libs/ite-packages")
    #sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.7/lib/python2.7/Lib/site-packages")

    import ice
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
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        self.fontScale = 1.2
          #initial data
       # self.folderDir = '//mcd-3d/data3d/spine_imageSources'  #'C:/Temp/testImage'
        self.imagesFilter = ['jpg','JPG','png','PNG']
       # self.currentOptionSelectState = [0,0,0,0,0,0,0,0,0,0]  
       # print ('2',self)
        self.createDock()
         # self.createImageTable()
        #  self.getImagesInFolder()

        self.defineImageInfoDock()
        self.defineImageButtonDock()
        self.initialWorkSpace()
        
       # self.setToSpineJobTree()
        try:
            self.initialSpineItemTree()
            self.defineAllSlotInSpine()
        except:
            pass
        #defineDockCamview
        self.createImageInfoTable()
        self.enableDynaSlotCheck.stateChanged.connect(self.enableDynamicSlot)   
        
        self.radioButton_createRad.clicked.connect(self.changeShapeState)  
        self.radioButton_createSquare.clicked.connect(self.changeShapeState)  
        self.radioButton_createSector.clicked.connect(self.changeShapeState)  
        
        self.toolButton_selectCurve.clicked.connect(self.getCurve)

        self.radioButton_createDirection.clicked.connect(self.changeShapeState)
        self.radioButton_createFollowCurve.clicked.connect(self.changeShapeState)     
           
    def initialWorkSpace(self):
        print "initialWorkSpace"
        #basicFilter = "*.json"
        #spineWorkSpace = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=1,fm=2)[0]
        
        ## 
        self.checkBox_squareFillIn.setEnabled(False)
        self.checkBox_squareAimO.setEnabled(False)
       
        
        
        
        try:
            currentWorkspace = cmds.workspace(dir=True,q=True)
        except:
            self.errorMsgLEdit.setText('pls select workspace first')
        
        if len(currentWorkspace) == 0:
            pass
        else:
            spineWorkSpace = currentWorkspace 
            spineImagesFolder = spineWorkSpace +'images'
            exportFolder = spineWorkSpace +'export'
            try:
                os.mkdir(spineWorkSpace)
            except:
                pass
                
            self.spineWorkSpaceLEdit.setText(spineWorkSpace)
            try :
                os.mkdir(spineImagesFolder)
            except:
                pass
            try:
                os.mkdir(exportFolder)
            except:
                pass
            
            self.spineImagesSpaceLEdit.setText(spineImagesFolder)
            self.spineExportSpaceLEdit.setText(exportFolder)
            self.selectImageFolderBtn.setChecked(False)
            self.selectImageFromDiskBTN.setChecked(False)
            self.selectSpineJobBtn.setChecked(True)
        #self.defineAllSlotInSpine()
          #  self.imageListTable.clear()
          

    def changeShapeState(self):  
        print "changeShapeState"
        
        
        if self.radioButton_createRad.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(True)
            self.lineEdit_widthSquare.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)
            self.checkBox_squareAimO.setEnabled(False)

            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)

            self.lineEdit_DirectionX.setEnabled(False)
            self.lineEdit_DirectionY.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)




        
        if self.radioButton_createSquare.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_widthSquare.setEnabled(True)
            self.lineEdit_HeightA.setEnabled(True)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(True)
            self.checkBox_squareAimO.setEnabled(True)

            self.lineEdit_DirectionX.setEnabled(False)
            self.lineEdit_DirectionY.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)

        
        if self.radioButton_createSector.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_widthSquare.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(True)
            self.lineEdit_AngleA_end.setEnabled(True)
            self.checkBox_squareFillIn.setEnabled(False)
            self.checkBox_squareAimO.setEnabled(False)

            self.lineEdit_DirectionX.setEnabled(False)
            self.lineEdit_DirectionY.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)
       
        
        if self.radioButton_createDirection.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(True)
            self.lineEdit_widthSquare.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)
            self.checkBox_squareAimO.setEnabled(False)

            self.lineEdit_DirectionX.setEnabled(True)
            self.lineEdit_DirectionY.setEnabled(True)
            self.lineEdit_directionDegree.setEnabled(True)
            self.lineEdit_directionSpread.setEnabled(True)
            self.lineEdit_selectCurve.setEnabled(False)
            self.groupBox_keysOption.setEnabled(False)

            self.lineEdit_RadiusA.setText("2000")
          
            self.lineEdit_DirectionX.setText("0")
            self.lineEdit_DirectionY.setText("0")
            
                                
        if self.radioButton_createFollowCurve.isChecked() == True:
            self.lineEdit_RadiusA.setEnabled(False)
            self.lineEdit_widthSquare.setEnabled(False)
            self.lineEdit_HeightA.setEnabled(False)
            self.lineEdit_AngleA_start.setEnabled(False)
            self.lineEdit_AngleA_end.setEnabled(False)
            self.checkBox_squareFillIn.setEnabled(False)
            self.checkBox_squareAimO.setEnabled(False)

            self.lineEdit_DirectionX.setEnabled(False)
            self.lineEdit_DirectionY.setEnabled(False)
            self.lineEdit_directionDegree.setEnabled(False)
            self.lineEdit_directionSpread.setEnabled(False)
            self.lineEdit_selectCurve.setEnabled(True)
            self.toolButton_selectCurve.setEnabled(True)
            ## groupBox_keysOption
            self.groupBox_keysOption.setEnabled(True)
            self.lineEdit_keys.setEnabled(True)
            self.lineEdit_NoiseA.setEnabled(True)
            self.lineEdit_pow.setEnabled(True)

            
                                                                
    
            
                                                    
          
          
          
          
    def enableDynamicSlot(self):
        print "enableDynamicSlot"
     #   print self.enableDynaSlotCheck.isChecked()
        if self.enableDynaSlotCheck.isChecked() == True:
           # print "aaaaaa"
            self.dynamicSlotGrp.setEnabled(True)

        else:
          #  print "bbbbb"
            self.dynamicSlotGrp.setEnabled(False)

    def createDock(self):
        print "createDock"
        self.dockWidgetImages = QtWidgets.QDockWidget(self)
        self.dockWidgetImages.setObjectName("dockWidget")
        self.dockWidgetImages.setMinimumWidth(280)
        self.dockWidgetImages.setMinimumHeight(600)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidgetImages)

        self.previewImageDock = QtWidgets.QDockWidget(self)
        self.previewImageDock.setObjectName("previewImageDock")
        self.previewImageDock.setMinimumWidth(290)
        self.previewImageDock.setMinimumHeight(300)
        
        
        self.workSpaceInfoDock = QtWidgets.QDockWidget(self)
        self.workSpaceInfoDock.setObjectName("workSpaceInfoDock")
        self.workSpaceInfoDock.setMinimumWidth(550)
        self.workSpaceInfoDock.setMinimumHeight(240)
        #self.workSpaceInfoDock.setMaximumHeight(200)
        
        
        
        self.dockWidgetImagesInfo = QtWidgets.QDockWidget(self)
        self.dockWidgetImagesInfo.setObjectName("dockWidget")
        self.dockWidgetImagesInfo.setMinimumWidth(550)
        self.dockWidgetImagesInfo.setMinimumHeight(630)
        #  self.dockWidgetImagesInfo.setMaximumHeight(330)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidgetImagesInfo)

        self.dockImageButton = QtWidgets.QDockWidget(self)
        self.dockImageButton.setObjectName("dockImageButton")
        self.dockImageButton.setMinimumWidth(300)
        self.dockImageButton.setMinimumHeight(150)


        self.dockSpineMeshProgress = QtWidgets.QDockWidget(self)
        self.dockSpineMeshProgress.setObjectName("dockMeshProgress")
        self.dockSpineMeshProgress.setMinimumWidth(400)
        self.dockSpineMeshProgress.setMinimumHeight(100)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockSpineMeshProgress)


       # self.dockExport = QtWidgets.QDockWidget(self)
       # self.dockExport.setObjectName("dockExport")
      #  self.dockExport.setMinimumWidth(400)
      #  self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockExport)

#dockWidgetImages workSpaceInfoDock dockSpineMeshProgress dockSpineItemTree

#dockSpineItemTree dockCamview
        self.dockSpineItemTree = QtWidgets.QDockWidget(self)
        self.dockSpineItemTree.setObjectName("dockSpineItemTree")
        self.dockSpineItemTree.setMinimumWidth(300)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockSpineItemTree)

        self.splitDockWidget( self.dockSpineItemTree, self.dockWidgetImages, QtCore.Qt.Horizontal)
        self.splitDockWidget( self.dockWidgetImages, self.dockSpineMeshProgress, QtCore.Qt.Horizontal)
        self.splitDockWidget( self.dockSpineMeshProgress, self.workSpaceInfoDock, QtCore.Qt.Horizontal)

        self.splitDockWidget( self.dockWidgetImages, self.previewImageDock, QtCore.Qt.Vertical)
        self.splitDockWidget( self.workSpaceInfoDock, self.dockWidgetImagesInfo, QtCore.Qt.Vertical)
        self.splitDockWidget( self.dockWidgetImagesInfo, self.dockImageButton, QtCore.Qt.Vertical)
      #  self.splitDockWidget( self.dockSpineMeshProgress, self.dockExport, QtCore.Qt.Vertical)



    def createImageInfoTable(self):
        print "createImageInfoTable"
        tableInfo =  "\
                 QTableWidget {\
                 font-size:12px;\
                 background-color:#333333;\
                 border-radius :8px;\
                 border-style:solid;\
                 border-width:1px;\
                 border-color:#666666;\
                 text-align:center;\
                 }\
                 "     
        
        
        self.imageInfoTable = QtWidgets.QTableWidget(self.dockSpineItemTree)
        self.imageInfoTable.setGeometry(QtCore.QRect(10, 610,280,330))
        columnCount = 2
        rowCount = 13
        rowHeight =25
        self.imageInfoTable.setObjectName("imageInfoTable")
        self.imageInfoTable.setColumnCount(columnCount)
        self.imageInfoTable.setRowCount(rowCount)
        self.imageInfoTable.setColumnWidth(0, 110)
        self.imageInfoTable.setColumnWidth(1, 170)
        self.imageInfoTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imageInfoTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.imageInfoTable.horizontalHeader().setVisible(False)
        self.imageInfoTable.verticalHeader().setVisible(False)
        for i in range(0,rowCount):
            self.imageInfoTable.setRowHeight(i, rowHeight)

        self.imageInfoTable.setStyleSheet(tableInfo);


                    
    def defineImageButtonDock(self):
        print "defineImageButtonDock"
   
        buttonStyle = "\
                         QLineEdit {\
                         height:50px;\
                         background-color:#333333;\
                         border-radius :5px;\
                         border-style:solid;\
                         border-width:3px;\
                         border-color:#5E749C;\
                         text-align:center;\
                         }\
                         QComboBox {\
                         height:50px;\
                         background-color:#333333;\
                         border-radius :5px;\
                         border-style:solid;\
                         border-width:3px;\
                         border-color:#5E749C;\
                         text-align:right;\
                         }\
                         QPushButton {\
                         background-color:#333333;\
                         border-radius:10px;\
                         border-style:solid;\
                         border-width:3px;\
                         border-color:#5E749C;\
                         }\
                         QPushButton:hover{\
                         background-color:#883333;\
                         border-radius:10px;\
                         border-style:solid;\
                         border-width:3px;\
                         border-color:#5E749C;\
                         }\
                         QPushButton:pressed{\
                         background-color:#AAAA33;\
                         border-radius:10px;\
                         border-style:solid;\
                         border-width:3px;\
                         border-color:#5E749C;\
                         }\
                         "
        buttonStyleB = "\
                         QPushButton {\
                         font-size:%s;\
                         background-color:#778888;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:hover{\
                         background-color:#883333;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#883333;\
                         }\
                         QPushButton:pressed{\
                         background-color:#AAAA33;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#AAAA33;\
                         }\
                         "%(str(self.fontScale*12)+'px')   
                         
        buttonStyleBLeft = "\
                         QPushButton {\
                         font-size:%s;\
                         background-color:#778888;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:hover{\
                         background-color:#883333;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#883333;\
                         }\
                         QPushButton:pressed{\
                         background-color:#AAAA33;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#AAAA33;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                      
                                                   
                                                                
                                                                             
                                                                                                       
        buttonStyleC = "\
                         QPushButton {\
                         background-color:#333333;\
                         color:#eeeeee;\
                         font-size:%s;\
                         border-radius:10px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#aaaaaa;\
                         }\
                         QPushButton:hover{\
                         background-color:#aaeeaa;\
                         color:#111111;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#aaeeaa;\
                         }\
                         QPushButton:pressed{\
                         background-color:#aaeeaa;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#aaeeaa;\
                         }\
                         QPushButton:checked{\
                         background-color:#99aa99;\
                         color:#111111;\
                         border-radius:8px;\
                         border-style:solid;\
                         border-width:2px;\
                         border-color:#99cc99;\
                         }\
                         "%(str(self.fontScale*12)+'px')             

        buttonStyleCMiddle = "\
                         QPushButton {\
                         background-color:#333333;\
                         color:#777777;\
                         font-size:%s;\
                         border-radius:0px;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:hover{\
                         background-color:#aaeeaa;\
                         color:#777777;\
                         border-radius:0px;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:pressed{\
                         background-color:#aaeeaa;\
                         border-radius:0px;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:checked{\
                         background-color:#99aa99;\
                         color:#777777;\
                         border-radius:0px;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                                      

        buttonStyleCRight = "\
                         QPushButton {\
                         background-color:#333333;\
                         color:#777777;\
                         font-size:%s;\
                         border-top-right-radius: 10px;\
                         border-bottom-right-radius: 10px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#aaaaaa;\
                         }\
                         QPushButton:hover{\
                         background-color:#aaeeaa;\
                         color:#777777;\
                         border-top-right-radius: 10px;\
                         border-bottom-right-radius: 10px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#aaeeaa;\
                         }\
                         QPushButton:pressed{\
                         background-color:#aaeeaa;\
                         border-top-right-radius: 10px;\
                         border-bottom-right-radius: 10px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#aaeeaa;\
                         }\
                         QPushButton:checked{\
                         background-color:#99aa99;\
                         color:#777777;\
                         border-top-right-radius: 10px;\
                         border-bottom-right-radius: 10px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#99cc99;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                                                                
        buttonStyleLeft = "\
                         QPushButton {\
                         background-color:#778888;\
                         font-size: %s;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:hover{\
                         background-color:#883333;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#883333;\
                         }\
                         QPushButton:pressed{\
                         background-color:#AAAA33;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#AAAA33;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                    
        buttonStyleLeftB = "\
                         QPushButton {\
                         background-color:#778888;\
                         font-size: %s;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#555555;\
                         }\
                         QPushButton:hover{\
                         background-color:#883333;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#883333;\
                         }\
                         QPushButton:pressed{\
                         background-color:#AAAA33;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#AAAA33;\
                         }\
                         " %(str(self.fontScale*12)+'px')                              
        lineEditRight = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#333333;\
                         border-top-right-radius: 8px;\
                         border-bottom-right-radius: 8px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#333333;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')        
        lineEditRightBMiddle = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#333333;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')         
                         
                                                
        lineEditRightBMiddleDark = "\
                         QLineEdit {\
                         font-size:%s;\
                         color:#aaaaaa;\
                         background-color:#333333;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                                                                                      

        lineEditRightB = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#333333;\
                         border-top-right-radius: 8px;\
                         border-bottom-right-radius: 8px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#333333;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')    
                                                                                                                                           
                                                                                                                         
        lineEditRightBDark = "\
                         QLineEdit {\
                         font-size:%s;\
                         color:#aaaaaa;\
                         background-color:#333333;\
                         border-top-right-radius: 8px;\
                         border-bottom-right-radius: 8px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#333333;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')    
                                                                                                                         
        lineEditBDark = "\
                         QLineEdit {\
                         font-size:%s;\
                         color:#aaaaaa;\
                         background-color:#333333;\
                         text-align:center;\
                         border-radius: 8px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#333333;\
                         }\
                         "%(str(self.fontScale*12)+'px')    
                                                                                                                        
                                                                                
        lineEditA = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#333333;\
                         border-radius :6px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')      
                         
        errMsgA = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#888888;\
                         color:#222222;\
                         border-radius :6px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#888888;\
                         text-align:left;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                
                         
                         
                         
        lineEditB = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#333333;\
                         border-radius :6px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "%(str(self.fontScale*12)+'px')      
                         
        lineEditC = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#333333;\
                         border-top-right-radius: 6px;\
                         border-bottom-right-radius: 6px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "                                           
                                                                         
        labelA  = "\
                         QLabel {\
                         height: 30px;\
                         background-color:#777777;\
                         color:#222222;\
                         border-top-left-radius:6px;\
                         border-bottom-left-radius: 6px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#777777;\
                         text-align:center;\
                         }\
                         "                     


        labelARight  = "\
                         QLabel {\
                         height: 30px;\
                         background-color:#777777;\
                         color:#222222;\
                         border-top-left-radius:6px;\
                         border-bottom-left-radius: 6px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#777777;\
                         text-align:center;\
                         }\
                         "       
        labelAMiddle  = "\
                         QLabel {\
                         height: 30px;\
                         background-color:#777777;\
                         color:#222222;\
                         border-style:solid;\
                         border-left-width:1px;\
                         border-right-width:1px;\
                         border-color:#777777;\
                         text-align:center;\
                         }\
                         "
        lineEditCMiddle = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#333333;\
                         border-style:solid;\
                         border-left-width:1px;\
                         border-right-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "                              
                         
        QGroupBoxA =  "\
                         QGroupBox {\
                         font-size:12px;\
                         background-color:#505050;\
                         border-radius :8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "     
                         
        treeA =  "\
                         QTreeWidget {\
                         font-size:%s;\
                         background-color:#505050;\
                         border-radius :8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "%(str(self.fontScale*12)+'px')                                                              
            
        tableA =  "\
                         QTableWidget {\
                         background-color:#333333;\
                         border-radius :8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         QTableWidget:item:hover{\
                         background-color:#883333;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#883333;\
                         }\
                         QTableWidget:pressed{\
                         background-color:#33AAA33;\
                         border-top-left-radius:8px;\
                         border-bottom-left-radius: 8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#AAAA33;\
                         }\
                         QTableWidget:item {\
                         font-size:1000000px;\
                         color:rgba(255,255,255,0);\
                         background-color:#333333;\
                         border-radius :8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "          
            

        
        #### define keyframe tool 
        

        
        
        self.keyFrameToolGrp = QtWidgets.QGroupBox(self.dockWidgetImagesInfo)
        self.keyFrameToolGrp.setGeometry(QtCore.QRect(10, 20, 530, 210))
        self.keyFrameToolGrp.setObjectName("keyFrameToolGrp")
        self.keyFrameToolGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.keyFrameToolGrp.setStyleSheet(QGroupBoxA)     
        self.keyFrameToolGrp.setVisible(True)
                
        self.trimBeforeFrameBtn = QtWidgets.QPushButton(self.keyFrameToolGrp)
        self.trimBeforeFrameBtn.setGeometry(QtCore.QRect(10, 10, 100,30))
        self.trimBeforeFrameBtn.setObjectName("trimBeforeFrameBtn")
        self.trimBeforeFrameBtn.setText(QtWidgets.QApplication.translate("MainWindow", "trim Before Num", None, -1))
        self.trimBeforeFrameBtn.clicked.connect(self.trimBeforeFrame)
        self.trimBeforeFrameBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.trimBeforeFrameLEdit = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.trimBeforeFrameLEdit.setGeometry(QtCore.QRect(110, 10, 100, 30))
        self.trimBeforeFrameLEdit.setObjectName("trimBeforeFrameLEdit")
        self.trimBeforeFrameLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.trimBeforeFrameLEdit.setText('1')
        self.trimBeforeFrameLEdit.setStyleSheet(lineEditRightBDark)     
        
        
        
            
        self.trimAfterFrameBtn = QtWidgets.QPushButton(self.keyFrameToolGrp)
        self.trimAfterFrameBtn.setGeometry(QtCore.QRect(250, 10, 100,30))
        self.trimAfterFrameBtn.setObjectName("trimAfterFrameBtn")
        self.trimAfterFrameBtn.setText(QtWidgets.QApplication.translate("MainWindow", "trim After Num", None, -1))
        self.trimAfterFrameBtn.clicked.connect(self.trimAfterFrame)
        self.trimAfterFrameBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.trimAfterFrameLEdit = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.trimAfterFrameLEdit.setGeometry(QtCore.QRect(350, 10, 100, 30))
        self.trimAfterFrameLEdit.setObjectName("trimAfterFrameLEdit")
        self.trimAfterFrameLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.trimAfterFrameLEdit.setText('1')
        self.trimAfterFrameLEdit.setStyleSheet(lineEditRightBDark)     
        
            
        self.trimBetweenFrameBTN = QtWidgets.QPushButton(self.keyFrameToolGrp)
        self.trimBetweenFrameBTN.setGeometry(QtCore.QRect(10, 50, 100,30))
        self.trimBetweenFrameBTN.setObjectName("trimBetweenFrameBTN")
        self.trimBetweenFrameBTN.setText(QtWidgets.QApplication.translate("MainWindow", "between Frame", None, -1))
        self.trimBetweenFrameBTN.clicked.connect(self.trimBetweenFrame)
        self.trimBetweenFrameBTN.setStyleSheet(buttonStyleLeftB)    
        
        self.trimBetweenFrameStartLEdit = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.trimBetweenFrameStartLEdit.setGeometry(QtCore.QRect(110, 50, 100, 30))
        self.trimBetweenFrameStartLEdit.setObjectName("trimBetweenFrameStartLEdit")
        self.trimBetweenFrameStartLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.trimBetweenFrameStartLEdit.setText('1')
        self.trimBetweenFrameStartLEdit.setStyleSheet(lineEditRightBMiddleDark)     
        
        
        self.trimBetweenFrameEndLEdit = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.trimBetweenFrameEndLEdit.setGeometry(QtCore.QRect(210, 50, 100, 30))
        self.trimBetweenFrameEndLEdit.setObjectName("trimBetweenFrameEndLEdit")
        self.trimBetweenFrameEndLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.trimBetweenFrameEndLEdit.setText('100')
        self.trimBetweenFrameEndLEdit.setStyleSheet(lineEditRightBDark)     
                                        
                                
                           
        self.alignToFrameBtn = QtWidgets.QPushButton(self.keyFrameToolGrp)
        self.alignToFrameBtn.setGeometry(QtCore.QRect(10, 90, 100,30))
        self.alignToFrameBtn.setObjectName("alignToFrameBtn")
        self.alignToFrameBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Align to Frame", None, -1))
        self.alignToFrameBtn.clicked.connect(self.alignKeys)
        self.alignToFrameBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.alignToFrameLEdit = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.alignToFrameLEdit.setGeometry(QtCore.QRect(110, 90, 100, 30))
        self.alignToFrameLEdit.setObjectName("alignToFrameLEdit")
        self.alignToFrameLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.alignToFrameLEdit.setText('1')
        self.alignToFrameLEdit.setStyleSheet(lineEditRightBDark)     
        
        #self.offsetFrameBtn = QtWidgets.QPushButton(self.keyFrameToolGrp)
       # self.offsetFrameBtn.setGeometry(QtCore.QRect(250, 90, 100,30))
       # self.offsetFrameBtn.setObjectName("offsetFrameBtn")
       # self.offsetFrameBtn.setText(QtWidgets.QApplication.translate("MainWindow", "offset Frame", None, -1))
       # self.offsetFrameBtn.clicked.connect(self.offsetKeyFrames)
       # self.offsetFrameBtn.setStyleSheet(buttonStyleLeftB)     

 
       # self.offsetFrameLEdit = QtWidgets.QLineEdit(self.keyFrameToolGrp)
       # self.offsetFrameLEdit.setGeometry(QtCore.QRect(350, 90, 100, 30))
       # self.offsetFrameLEdit.setObjectName("alignToFrameLEdit")
       # self.offsetFrameLEdit.setAlignment(QtCore.Qt.AlignCenter)
       # self.offsetFrameLEdit.setText('1')
       # self.offsetFrameLEdit.setStyleSheet(lineEditRightBDark)     
               
        
        self.scaleTimeBtn = QtWidgets.QPushButton(self.keyFrameToolGrp)
        self.scaleTimeBtn.setGeometry(QtCore.QRect(10, 130, 100, 30))
        self.scaleTimeBtn.setObjectName("scaleTimeBtn")
        self.scaleTimeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "scale frame", None, -1))
        self.scaleTimeBtn.clicked.connect(self.scaleFrames)
        self.scaleTimeBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.scaleTimeOriginIN = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.scaleTimeOriginIN.setGeometry(QtCore.QRect(110, 130, 100, 30))
        self.scaleTimeOriginIN.setObjectName("scaleTimeOriginIN")
        self.scaleTimeOriginIN.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleTimeOriginIN.setText('1')
        self.scaleTimeOriginIN.setStyleSheet(lineEditRightBMiddleDark)  
                 
        self.scaleTimeOriginOut = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.scaleTimeOriginOut.setGeometry(QtCore.QRect(210, 130, 100, 30))
        self.scaleTimeOriginOut.setObjectName("scaleTimeOriginOut")
        self.scaleTimeOriginOut.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleTimeOriginOut.setText('20')
        self.scaleTimeOriginOut.setStyleSheet(lineEditRightBMiddleDark)     
        
        self.scaleTimeNewIn = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.scaleTimeNewIn.setGeometry(QtCore.QRect(310, 130, 100, 30))
        self.scaleTimeNewIn.setObjectName("scaleTimeNewIn")
        self.scaleTimeNewIn.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleTimeNewIn.setText('1')
        self.scaleTimeNewIn.setStyleSheet(lineEditRightBMiddleDark)     
        
        self.scaleTimeNewOut = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.scaleTimeNewOut.setGeometry(QtCore.QRect(410,130, 100, 30))
        self.scaleTimeNewOut.setObjectName("scaleTimeNewOut")
        self.scaleTimeNewOut.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleTimeNewOut.setText('60')
        self.scaleTimeNewOut.setStyleSheet(lineEditRightBDark)           
                
        
         
        self.loopTimeBtn = QtWidgets.QPushButton(self.keyFrameToolGrp)
        self.loopTimeBtn.setGeometry(QtCore.QRect(10, 170, 100, 30))
        self.loopTimeBtn.setObjectName("loopTimeBtn")
        self.loopTimeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "loop frame", None, -1))
        self.loopTimeBtn.clicked.connect(self.loopFrames)
        self.loopTimeBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.loopTimeIn = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.loopTimeIn.setGeometry(QtCore.QRect(110, 170, 100, 30))
        self.loopTimeIn.setObjectName("loopTimeIn")
        self.loopTimeIn.setAlignment(QtCore.Qt.AlignCenter)
        self.loopTimeIn.setText('2')
        self.loopTimeIn.setStyleSheet(lineEditRightBMiddleDark)  
                 
        self.loopTimeOut = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.loopTimeOut.setGeometry(QtCore.QRect(210, 170, 100, 30))
        self.loopTimeOut.setObjectName("loopTimeOut")
        self.loopTimeOut.setAlignment(QtCore.Qt.AlignCenter)
        self.loopTimeOut.setText('20')
        self.loopTimeOut.setStyleSheet(lineEditRightBMiddleDark)     
        
        self.loopSpaceFrame = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.loopSpaceFrame.setGeometry(QtCore.QRect(310, 170, 100, 30))
        self.loopSpaceFrame.setObjectName("loopSpaceFrame")
        self.loopSpaceFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.loopSpaceFrame.setText('5')
        self.loopSpaceFrame.setStyleSheet(lineEditRightBMiddleDark)     
        
        self.loopTimes = QtWidgets.QLineEdit(self.keyFrameToolGrp)
        self.loopTimes.setGeometry(QtCore.QRect(410,170, 100, 30))
        self.loopTimes.setObjectName("loopTimes")
        self.loopTimes.setAlignment(QtCore.Qt.AlignCenter)
        self.loopTimes.setText('1')
        self.loopTimes.setStyleSheet(lineEditRightBDark)           
                       
                                               
        ##### fillet select
        self.filletSelectGrp = QtWidgets.QGroupBox(self.dockWidgetImagesInfo)
        self.filletSelectGrp.setGeometry(QtCore.QRect(10, 490, 530, 130))
        self.filletSelectGrp.setObjectName("filletSelectGrp")
        self.filletSelectGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.filletSelectGrp.setStyleSheet(QGroupBoxA)     
        self.filletSelectGrp.setVisible(True)
        
        
        self.defineSelectObjBtn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.defineSelectObjBtn.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.defineSelectObjBtn.setObjectName("defineSelectObjBtn")
        self.defineSelectObjBtn.setText(QtWidgets.QApplication.translate("MainWindow", "select Slots", None, -1))
        self.defineSelectObjBtn.clicked.connect(self.getSelectSlotBone)
        self.defineSelectObjBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.showAllSelectedObjLedit = QtWidgets.QLineEdit(self.filletSelectGrp)
        self.showAllSelectedObjLedit.setGeometry(QtCore.QRect(110, 10, 305, 30))
        self.showAllSelectedObjLedit.setObjectName("showAllSelectedObjLedit")
        self.showAllSelectedObjLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.showAllSelectedObjLedit.setText('')
        self.showAllSelectedObjLedit.setStyleSheet(lineEditRightBDark)          
        
        
        self.selectAnyTransform = QtWidgets.QPushButton(self.filletSelectGrp)
        self.selectAnyTransform.setGeometry(QtCore.QRect(420, 10, 90, 30))
        self.selectAnyTransform.setObjectName("createClipping")
        self.selectAnyTransform.setText(QtWidgets.QApplication.translate("MainWindow", "select Any", None, -1))
        self.selectAnyTransform.clicked.connect(self.getSelectAnyTransform)
        self.selectAnyTransform.setStyleSheet(buttonStyleB)             



        
 
        self.renameAllSelectBtn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.renameAllSelectBtn.setGeometry(QtCore.QRect(10, 50, 100, 30))
        self.renameAllSelectBtn.setObjectName("renameAllSelectBtn")
        self.renameAllSelectBtn.setText(QtWidgets.QApplication.translate("MainWindow", "rename selected", None, -1))
        self.renameAllSelectBtn.clicked.connect(self.renameSelectedBone)
        self.renameAllSelectBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.newNameSelectedLEdit = QtWidgets.QLineEdit(self.filletSelectGrp)
        self.newNameSelectedLEdit.setGeometry(QtCore.QRect(110, 50, 400, 30))
        self.newNameSelectedLEdit.setObjectName("newNameSelectedLEdit")
        self.newNameSelectedLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.newNameSelectedLEdit.setText('')
        self.newNameSelectedLEdit.setStyleSheet(lineEditRightBDark)          
                
        self.optionalSelctBt = QtWidgets.QPushButton(self.filletSelectGrp)
        self.optionalSelctBt.setGeometry(QtCore.QRect(10, 90, 100, 30))
        self.optionalSelctBt.setObjectName("optionalSelctBt")
        self.optionalSelctBt.setText(QtWidgets.QApplication.translate("MainWindow", "optional Select", None, -1))
        #self.optionalSelctBt.clicked.connect(self.createRootCtrl)
        self.optionalSelctBt.setStyleSheet(buttonStyleBLeft)                     
  
        self.fillet_odd_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_odd_btn.setGeometry(QtCore.QRect(110, 90, 40, 30))
        self.fillet_odd_btn.setObjectName("fillet_odd_btn")
        self.fillet_odd_btn.setCheckable(True)
        self.fillet_odd_btn.setChecked(False)
        self.fillet_odd_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#odd", None, -1))
        self.fillet_odd_btn.clicked.connect(self.optionalSelect)
        self.fillet_odd_btn.setStyleSheet(buttonStyleCMiddle)     
  
        self.fillet_even_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_even_btn.setGeometry(QtCore.QRect(150, 90, 40, 30))
        self.fillet_even_btn.setObjectName("fillet_even_btn")
        self.fillet_even_btn.setCheckable(True)
        self.fillet_even_btn.setChecked(False)  

        self.fillet_even_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#even", None, -1))
        self.fillet_even_btn.clicked.connect(self.optionalSelect)

        #self.fillet_even_btn.clicked.connect(self.doAnalyzeCharacterSet)
        self.fillet_even_btn.setStyleSheet(buttonStyleCMiddle)     
        
        self.fillet_n1_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n1_btn.setGeometry(QtCore.QRect(190, 90, 30, 30))
        self.fillet_n1_btn.setObjectName("fillet_n1_btn")
        self.fillet_n1_btn.setCheckable(True)
        self.fillet_n1_btn.setChecked(False)  
        self.fillet_n1_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#1", None, -1))
        self.fillet_n1_btn.clicked.connect(self.optionalSelect)
        self.fillet_n1_btn.setStyleSheet(buttonStyleCMiddle)     
         
        self.fillet_n2_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n2_btn.setGeometry(QtCore.QRect(220, 90, 30, 30))
        self.fillet_n2_btn.setObjectName("fillet_n2_btn")
        self.fillet_n2_btn.setCheckable(True)
        self.fillet_n2_btn.setChecked(False)  
        self.fillet_n2_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#2", None, -1))
        self.fillet_n2_btn.clicked.connect(self.optionalSelect)
        self.fillet_n2_btn.setStyleSheet(buttonStyleCMiddle)      
        self.fillet_n3_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n3_btn.setGeometry(QtCore.QRect(250, 90, 30, 30))
        self.fillet_n3_btn.setObjectName("fillet_n3_btn")
        self.fillet_n3_btn.setCheckable(True)
        self.fillet_n3_btn.setChecked(False)  
        self.fillet_n3_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#3", None, -1))
        self.fillet_n3_btn.clicked.connect(self.optionalSelect)
        self.fillet_n3_btn.setStyleSheet(buttonStyleCMiddle)                   
                    
        self.fillet_n4_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n4_btn.setGeometry(QtCore.QRect(280, 90, 30, 30))
        self.fillet_n4_btn.setObjectName("fillet_n4_btn")
        self.fillet_n4_btn.setCheckable(True)
        self.fillet_n4_btn.setChecked(False)  
        self.fillet_n4_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#4", None, -1))
        self.fillet_n4_btn.clicked.connect(self.optionalSelect)
        self.fillet_n4_btn.setStyleSheet(buttonStyleCMiddle)                   
        
                                     
        self.fillet_n5_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n5_btn.setGeometry(QtCore.QRect(310, 90, 30, 30))
        self.fillet_n5_btn.setObjectName("fillet_n5_btn")
        self.fillet_n5_btn.setCheckable(True)
        self.fillet_n5_btn.setChecked(False)  
        self.fillet_n5_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#5", None, -1))
        self.fillet_n5_btn.clicked.connect(self.optionalSelect)
        self.fillet_n5_btn.setStyleSheet(buttonStyleCMiddle)                   
                                                                            
        self.fillet_n6_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n6_btn.setGeometry(QtCore.QRect(340, 90, 30, 30))
        self.fillet_n6_btn.setObjectName("fillet_n6_btn")
        self.fillet_n6_btn.setCheckable(True)
        self.fillet_n6_btn.setChecked(False)  
        self.fillet_n6_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#6", None, -1))
        self.fillet_n6_btn.clicked.connect(self.optionalSelect)
        self.fillet_n6_btn.setStyleSheet(buttonStyleCMiddle)                                          
                                            
        self.fillet_n7_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n7_btn.setGeometry(QtCore.QRect(370, 90, 30, 30))
        self.fillet_n7_btn.setObjectName("fillet_n7_btn")
        self.fillet_n7_btn.setCheckable(True)
        self.fillet_n7_btn.setChecked(False)  
        self.fillet_n7_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#7", None, -1))
        self.fillet_n7_btn.clicked.connect(self.optionalSelect)
        self.fillet_n7_btn.setStyleSheet(buttonStyleCMiddle)       
                                            
        self.fillet_n8_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n8_btn.setGeometry(QtCore.QRect(400, 90, 30, 30))
        self.fillet_n8_btn.setObjectName("fillet_n8_btn")
        self.fillet_n8_btn.setCheckable(True)
        self.fillet_n8_btn.setChecked(False)  
        self.fillet_n8_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#8", None, -1))
        self.fillet_n8_btn.clicked.connect(self.optionalSelect)
        self.fillet_n8_btn.setStyleSheet(buttonStyleCMiddle)   
        
                                            
        self.fillet_n9_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n9_btn.setGeometry(QtCore.QRect(430, 90, 30, 30))
        self.fillet_n9_btn.setObjectName("fillet_n9_btn")
        self.fillet_n9_btn.setCheckable(True)
        self.fillet_n9_btn.setChecked(False)  
        self.fillet_n9_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#9", None, -1))
        self.fillet_n9_btn.clicked.connect(self.optionalSelect)
        self.fillet_n9_btn.setStyleSheet(buttonStyleCMiddle)   
        
                                            
        self.fillet_n0_btn = QtWidgets.QPushButton(self.filletSelectGrp)
        self.fillet_n0_btn.setGeometry(QtCore.QRect(460, 90, 30, 30))
        self.fillet_n0_btn.setObjectName("fillet_n0_btn")
        self.fillet_n0_btn.setCheckable(True)
        self.fillet_n0_btn.setChecked(False)  
        self.fillet_n0_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#0", None, -1))
        self.fillet_n0_btn.clicked.connect(self.optionalSelect)
        self.fillet_n0_btn.setStyleSheet(buttonStyleCRight)                                                                                                                                               
                                              
                                                                                                                                                                                                                                                                                                                                                                                                                     
        ###### Random Frame keys     
                                                                                                                      
        self.randomFrameKeyGrp = QtWidgets.QGroupBox(self.dockWidgetImagesInfo)
        self.randomFrameKeyGrp.setGeometry(QtCore.QRect(10, 235, 530, 250))
        self.randomFrameKeyGrp.setObjectName("randomFrameKeyGrp")
        self.randomFrameKeyGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.randomFrameKeyGrp.setStyleSheet(QGroupBoxA)     
        self.randomFrameKeyGrp.setVisible(True)
                  
       
        self.setModAllFrameBTN = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.setModAllFrameBTN.setGeometry(QtCore.QRect(10, 10, 50, 30))
        self.setModAllFrameBTN.setObjectName("setModAllFrameBTN")
        self.setModAllFrameBTN.setText(QtWidgets.QApplication.translate("MainWindow", "All", None, -1))
        self.setModAllFrameBTN.clicked.connect(self.setFrameFilletToAll)
        self.setModAllFrameBTN.setStyleSheet(buttonStyleB)     
        
        self.setModFirstFrameBTN = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.setModFirstFrameBTN.setGeometry(QtCore.QRect(65, 10, 50, 30))
        self.setModFirstFrameBTN.setObjectName("setModFirstFrameBTN")
        self.setModFirstFrameBTN.setText(QtWidgets.QApplication.translate("MainWindow", "first", None, -1))
        self.setModFirstFrameBTN.clicked.connect(self.setFrameFilletToFirst)
        self.setModFirstFrameBTN.setStyleSheet(buttonStyleB)   
              
        self.setModLastFrameBTN = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.setModLastFrameBTN.setGeometry(QtCore.QRect(120, 10, 50, 30))
        self.setModLastFrameBTN.setObjectName("setModLastFrameBTN")
        self.setModLastFrameBTN.setText(QtWidgets.QApplication.translate("MainWindow", "last", None, -1))
        self.setModLastFrameBTN.clicked.connect(self.setFrameFilletToLast)
        self.setModLastFrameBTN.setStyleSheet(buttonStyleB) 
                                                                                                                    
        self.modFrameIndxLEdt = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modFrameIndxLEdt.setGeometry(QtCore.QRect(180,10, 180, 30))
        self.modFrameIndxLEdt.setObjectName("modFrameIndxLEdt")
        self.modFrameIndxLEdt.setText(QtWidgets.QApplication.translate("MainWindow", "all", None, -1))
        self.modFrameIndxLEdt.setStyleSheet(lineEditBDark)     
        
        self.modReplaceModBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modReplaceModBtn.setGeometry(QtCore.QRect(370, 10, 30, 30))
        self.modReplaceModBtn.setObjectName("modReplaceModBtn")
        self.modReplaceModBtn.setCheckable(True)
        self.modReplaceModBtn.setChecked(False)
        self.modReplaceModBtn.setFlat(False)
        self.modReplaceModBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Re", None, -1))
        self.modReplaceModBtn.clicked.connect(self.changeRelaceMode)
        self.modReplaceModBtn.setStyleSheet(buttonStyleC)                  
        
        self.modOffsetBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modOffsetBtn.setGeometry(QtCore.QRect(405, 10, 30, 30))
        self.modOffsetBtn.setObjectName("modOffsetBtn")
        self.modOffsetBtn.setCheckable(True)
        self.modOffsetBtn.setChecked(True)
        self.modOffsetBtn.setFlat(False)
        self.modOffsetBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Of", None, -1))
        self.modOffsetBtn.clicked.connect(self.changeOffsetMode)
        self.modOffsetBtn.setStyleSheet(buttonStyleC)              
        
        self.modSinBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modSinBtn.setGeometry(QtCore.QRect(440, 10, 30, 30))
        self.modSinBtn.setObjectName("modSinBtn")
        self.modSinBtn.setCheckable(True)
        self.modSinBtn.setChecked(False)
        self.modSinBtn.setFlat(False)
        self.modSinBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Sin", None, -1))
       # self.modSinBtn.clicked.connect(self.changeOffsetMode)
        self.modSinBtn.setStyleSheet(buttonStyleC)               
        
        self.modStepBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modStepBtn.setGeometry(QtCore.QRect(475, 10, 30, 30))
        self.modStepBtn.setObjectName("modStepBtn")
        self.modStepBtn.setCheckable(True)
        self.modStepBtn.setChecked(False)
        self.modStepBtn.setFlat(False)
        self.modStepBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Step", None, -1))
       # self.modSinBtn.clicked.connect(self.changeOffsetMode)
        self.modStepBtn.setStyleSheet(buttonStyleC)               
                                
        self.modTransXBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modTransXBtn.setGeometry(QtCore.QRect(10, 50, 60, 30))
        self.modTransXBtn.setObjectName("modTransXBtn")
        self.modTransXBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod X", None, -1))
        self.modTransXBtn.clicked.connect(self.defineModX)
        self.modTransXBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modTransXminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modTransXminLedit.setGeometry(QtCore.QRect(70, 50, 50, 30))
        self.modTransXminLedit.setObjectName("modTransXminLedit")
        self.modTransXminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modTransXminLedit.setText('0')
        self.modTransXminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modTransXMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modTransXMaxLedit.setGeometry(QtCore.QRect(120, 50, 50, 30))
        self.modTransXMaxLedit.setObjectName("modTransXMaxLedit")
        self.modTransXMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modTransXMaxLedit.setText('100')
        self.modTransXMaxLedit.setStyleSheet(lineEditRightBDark)       
        
        self.modTransYBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modTransYBtn.setGeometry(QtCore.QRect(180, 50, 60, 30))
        self.modTransYBtn.setObjectName("modTransYBtn")
        self.modTransYBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Y", None, -1))
        self.modTransYBtn.clicked.connect(self.defineModY)
        self.modTransYBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modTransYminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modTransYminLedit.setGeometry(QtCore.QRect(240, 50, 50, 30))
        self.modTransYminLedit.setObjectName("modTransYminLedit")
        self.modTransYminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modTransYminLedit.setText('0')
        self.modTransYminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modTransYMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modTransYMaxLedit.setGeometry(QtCore.QRect(290, 50, 50, 30))
        self.modTransYMaxLedit.setObjectName("modTransYMaxLedit")
        self.modTransYMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modTransYMaxLedit.setText('100')
        self.modTransYMaxLedit.setStyleSheet(lineEditRightBDark)                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        self.modTransZBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modTransZBtn.setGeometry(QtCore.QRect(350, 50, 60, 30))
        self.modTransZBtn.setObjectName("modTransZBtn")
        self.modTransZBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Z", None, -1))
        self.modTransZBtn.clicked.connect(self.defineModZ)
        self.modTransZBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modTransZminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modTransZminLedit.setGeometry(QtCore.QRect(410, 50, 50, 30))
        self.modTransZminLedit.setObjectName("modTransZminLedit")
        self.modTransZminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modTransZminLedit.setText('0')
        self.modTransZminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modTransZMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modTransZMaxLedit.setGeometry(QtCore.QRect(460, 50, 50, 30))
        self.modTransZMaxLedit.setObjectName("modTransZMaxLedit")
        self.modTransZMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modTransZMaxLedit.setText('0')
        self.modTransZMaxLedit.setStyleSheet(lineEditRightBDark)        
        
        
        
        
        
        ##random rotate
        
        self.modRotateXBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modRotateXBtn.setGeometry(QtCore.QRect(10, 90, 60, 30))
        self.modRotateXBtn.setObjectName("modRotateXBtn")
        self.modRotateXBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Rx", None, -1))
        self.modRotateXBtn.clicked.connect(self.defineModRX)
        self.modRotateXBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modRotateXminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modRotateXminLedit.setGeometry(QtCore.QRect(70, 90, 50, 30))
        self.modRotateXminLedit.setObjectName("modRotateXminLedit")
        self.modRotateXminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modRotateXminLedit.setText('0.0')
        self.modRotateXminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modRotateXMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modRotateXMaxLedit.setGeometry(QtCore.QRect(120, 90, 50, 30))
        self.modRotateXMaxLedit.setObjectName("modRotateXMaxLedit")
        self.modRotateXMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modRotateXMaxLedit.setText('179.0')
        self.modRotateXMaxLedit.setStyleSheet(lineEditRightBDark)       
        
        self.modRotateYBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modRotateYBtn.setGeometry(QtCore.QRect(180, 90, 60, 30))
        self.modRotateYBtn.setObjectName("modRotateYBtn")
        self.modRotateYBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Ry", None, -1))
        self.modRotateYBtn.clicked.connect(self.defineModRY)
        self.modRotateYBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modRotateYminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modRotateYminLedit.setGeometry(QtCore.QRect(240, 90, 50, 30))
        self.modRotateYminLedit.setObjectName("modTransYminLedit")
        self.modRotateYminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modRotateYminLedit.setText('0.0')
        self.modRotateYminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modRotateYMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modRotateYMaxLedit.setGeometry(QtCore.QRect(290, 90, 50, 30))
        self.modRotateYMaxLedit.setObjectName("modTransYMaxLedit")
        self.modRotateYMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modRotateYMaxLedit.setText('179.0')
        self.modRotateYMaxLedit.setStyleSheet(lineEditRightBDark)                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        self.modRotateZBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modRotateZBtn.setGeometry(QtCore.QRect(350, 90, 60, 30))
        self.modRotateZBtn.setObjectName("modRotateZBtn")
        self.modRotateZBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Rz", None, -1))
        self.modRotateZBtn.clicked.connect(self.defineModRZ)
        self.modRotateZBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modRotateZminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modRotateZminLedit.setGeometry(QtCore.QRect(410, 90, 50, 30))
        self.modRotateZminLedit.setObjectName("modTransZminLedit")
        self.modRotateZminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modRotateZminLedit.setText('0.0')
        self.modRotateZminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modRotateZMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modRotateZMaxLedit.setGeometry(QtCore.QRect(460, 90, 50, 30))
        self.modRotateZMaxLedit.setObjectName("modTransZMaxLedit")
        self.modRotateZMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modRotateZMaxLedit.setText('179.0')
        self.modRotateZMaxLedit.setStyleSheet(lineEditRightBDark)                               
                                        

        ##random scale
        
        self.modScaleXBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modScaleXBtn.setGeometry(QtCore.QRect(10, 130, 60, 30))
        self.modScaleXBtn.setObjectName("modScaleXBtn")
        self.modScaleXBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Sx", None, -1))
        self.modScaleXBtn.clicked.connect(self.defineModSX)
        self.modScaleXBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modScaleXminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleXminLedit.setGeometry(QtCore.QRect(70, 130, 50, 30))
        self.modScaleXminLedit.setObjectName("modScaleXminLedit")
        self.modScaleXminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleXminLedit.setText('0.1')
        self.modScaleXminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modScaleXMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleXMaxLedit.setGeometry(QtCore.QRect(120, 130, 50, 30))
        self.modScaleXMaxLedit.setObjectName("modScaleXMaxLedit")
        self.modScaleXMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleXMaxLedit.setText('2.0')
        self.modScaleXMaxLedit.setStyleSheet(lineEditRightBDark)       
        
        self.modScaleYBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modScaleYBtn.setGeometry(QtCore.QRect(180, 130, 60, 30))
        self.modScaleYBtn.setObjectName("modScaleYBtn")
        self.modScaleYBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Sy", None, -1))
        self.modScaleYBtn.clicked.connect(self.defineModSY)
        self.modScaleYBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modScaleYminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleYminLedit.setGeometry(QtCore.QRect(240, 130, 50, 30))
        self.modScaleYminLedit.setObjectName("modScaleYminLedit")
        self.modScaleYminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleYminLedit.setText('0.1')
        self.modScaleYminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modScaleYMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleYMaxLedit.setGeometry(QtCore.QRect(290, 130, 50, 30))
        self.modScaleYMaxLedit.setObjectName("modScaleYMaxLedit")
        self.modScaleYMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleYMaxLedit.setText('2.0')
        self.modScaleYMaxLedit.setStyleSheet(lineEditRightBDark)                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        self.modScaleZBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modScaleZBtn.setGeometry(QtCore.QRect(350, 130, 60, 30))
        self.modScaleZBtn.setObjectName("modScaleZBtn")
        self.modScaleZBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Sz", None, -1))
        self.modScaleZBtn.clicked.connect(self.defineModSZ)
        self.modScaleZBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modScaleZminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleZminLedit.setGeometry(QtCore.QRect(410, 130, 50, 30))
        self.modScaleZminLedit.setObjectName("modScaleZminLedit")
        self.modScaleZminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleZminLedit.setText('0.1')
        self.modScaleZminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modScaleZMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleZMaxLedit.setGeometry(QtCore.QRect(460, 130, 50, 30))
        self.modScaleZMaxLedit.setObjectName("modTransZMaxLedit")
        self.modScaleZMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleZMaxLedit.setText('2.0')
        self.modScaleZMaxLedit.setStyleSheet(lineEditRightBDark)                               
                                                                                                                
        self.modScaleAllBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modScaleAllBtn.setGeometry(QtCore.QRect(10, 170, 60, 30))
        self.modScaleAllBtn.setObjectName("modScaleAllBtn")
        self.modScaleAllBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod All", None, -1))
        self.modScaleAllBtn.clicked.connect(self.defineModSAll)
        self.modScaleAllBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modScaleAllminLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleAllminLedit.setGeometry(QtCore.QRect(70, 170, 50, 30))
        self.modScaleAllminLedit.setObjectName("modScaleAllminLedit")
        self.modScaleAllminLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleAllminLedit.setText('0.1')
        self.modScaleAllminLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modScaleAllMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modScaleAllMaxLedit.setGeometry(QtCore.QRect(120, 170, 50, 30))
        self.modScaleAllMaxLedit.setObjectName("modScaleAllMaxLedit")
        self.modScaleAllMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modScaleAllMaxLedit.setText('2.0')
        self.modScaleAllMaxLedit.setStyleSheet(lineEditRightBDark)                               
       
        ####   modift alpha colr
        self.modAlphaGainBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modAlphaGainBtn.setGeometry(QtCore.QRect(10, 210, 60, 30))
        self.modAlphaGainBtn.setObjectName("modAlphaGainBtn")
        self.modAlphaGainBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod A", None, -1))
        self.modAlphaGainBtn.clicked.connect(self.defineModAlpha)
        self.modAlphaGainBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modAlphaMinLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modAlphaMinLedit.setGeometry(QtCore.QRect(70, 210, 50, 30))
        self.modAlphaMinLedit.setObjectName("modAlphaMinLedit")
        self.modAlphaMinLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modAlphaMinLedit.setText('0.1')
        self.modAlphaMinLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modAlphaMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modAlphaMaxLedit.setGeometry(QtCore.QRect(120, 210, 50, 30))
        self.modAlphaMaxLedit.setObjectName("modAlphaMaxLedit")
        self.modAlphaMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modAlphaMaxLedit.setText('1.0')
        self.modAlphaMaxLedit.setStyleSheet(lineEditRightBDark)      
        
                                 
        self.modColorBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modColorBtn.setGeometry(QtCore.QRect(180, 210, 60, 30))
        self.modColorBtn.setObjectName("modColorBtn")
        self.modColorBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod C", None, -1))
        self.modColorBtn.clicked.connect(self.createRootCtrl)
        self.modColorBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modColorMinLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modColorMinLedit.setGeometry(QtCore.QRect(240, 210, 50, 30))
        self.modColorMinLedit.setObjectName("modColorMinLedit")
        self.modColorMinLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modColorMinLedit.setText('0.1')
        self.modColorMinLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modColorMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modColorMaxLedit.setGeometry(QtCore.QRect(290, 210, 50, 30))
        self.modColorMaxLedit.setObjectName("modColorMaxLedit")
        self.modColorMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modColorMaxLedit.setText('1.0')
        self.modColorMaxLedit.setStyleSheet(lineEditRightBDark)                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        self.modFadeBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
        self.modFadeBtn.setGeometry(QtCore.QRect(350, 210, 60, 30))
        self.modFadeBtn.setObjectName("modFadeBtn")
        self.modFadeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Fade", None, -1))
        self.modFadeBtn.clicked.connect(self.createRootCtrl)
        self.modFadeBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.modFadeMinLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modFadeMinLedit.setGeometry(QtCore.QRect(410, 210, 50, 30))
        self.modFadeMinLedit.setObjectName("modFadeMinLedit")
        self.modFadeMinLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modFadeMinLedit.setText('0.1')
        self.modFadeMinLedit.setStyleSheet(lineEditRightBMiddleDark)  
        
        self.modFadeMaxLedit = QtWidgets.QLineEdit(self.randomFrameKeyGrp)
        self.modFadeMaxLedit.setGeometry(QtCore.QRect(460, 210, 50, 30))
        self.modFadeMaxLedit.setObjectName("modFadeMaxLedit")
        self.modFadeMaxLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.modFadeMaxLedit.setText('1.0')
        self.modFadeMaxLedit.setStyleSheet(lineEditRightBDark)                                                                    
                                                                                                            
               
        ###dockSpineItemTree    
        
        
        
        self.selectImageFolderBtn = QtWidgets.QPushButton(self.dockSpineItemTree)
        self.selectImageFolderBtn.setGeometry(QtCore.QRect(10, 20, 70,30))
        self.selectImageFolderBtn.setObjectName("selectImageFolderBtn")
        self.selectImageFolderBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Database", None, -1))
        self.selectImageFolderBtn.setCheckable(True)
        self.selectImageFolderBtn.setChecked(False)
        self.selectImageFolderBtn.setFlat(False)
        self.selectImageFolderBtn.clicked.connect(self.setImageSourceToDatabase)
        self.selectImageFolderBtn.setStyleSheet(buttonStyleC)     

        self.selectImageFromDiskBTN = QtWidgets.QPushButton(self.dockSpineItemTree)
        self.selectImageFromDiskBTN.setGeometry(QtCore.QRect(85, 20, 70,30))
        self.selectImageFromDiskBTN.setObjectName("selectImageFromDisk")
        self.selectImageFromDiskBTN.setText(QtWidgets.QApplication.translate("MainWindow", "Disk", None, -1))
        self.selectImageFromDiskBTN.setCheckable(True)
        self.selectImageFromDiskBTN.setChecked(False)
        self.selectImageFromDiskBTN.setFlat(False)
        self.selectImageFromDiskBTN.clicked.connect(self.setToDisk)
        self.selectImageFromDiskBTN.setStyleSheet(buttonStyleC)     
    
        self.selectSpineJobBtn = QtWidgets.QPushButton(self.dockSpineItemTree)
        self.selectSpineJobBtn.setGeometry(QtCore.QRect(160, 20, 70,30))
        self.selectSpineJobBtn.setObjectName("selectSpineJobBtn")
        self.selectSpineJobBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Spine Job", None, -1))
        self.selectSpineJobBtn.setCheckable(True)
        self.selectSpineJobBtn.setChecked(False)
        self.selectSpineJobBtn.setFlat(False)       
        self.selectSpineJobBtn.clicked.connect(self.setToSpineJobTree)
        self.selectSpineJobBtn.setStyleSheet(buttonStyleC)     

        self.openSelectedFolderBtn = QtWidgets.QPushButton(self.dockSpineItemTree)
        self.openSelectedFolderBtn.setGeometry(QtCore.QRect(250, 20, 40,30))
        self.openSelectedFolderBtn.setObjectName("selectSpineJobBtn")
        self.openSelectedFolderBtn.setText(QtWidgets.QApplication.translate("MainWindow", "--", None, -1))
        self.openSelectedFolderBtn.clicked.connect(self.openSelectedFolder)
        self.openSelectedFolderBtn.setStyleSheet(buttonStyleC)                  
                                          
                      
        self.spineItemTree = QtWidgets.QTreeWidget(self.dockSpineItemTree)
        self.spineItemTree.setGeometry(QtCore.QRect(10, 60, 280, 550))
        self.spineItemTree.setDragEnabled(True)
        self.spineItemTree.setDragDropOverwriteMode(True)
        self.spineItemTree.header().setVisible(False)

        self.spineItemTree.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.spineItemTree.setObjectName("spineItemTree")
        self.spineItemTree.setStyleSheet(treeA)     
        self.spineItemTree.itemClicked.connect(self.defineImageTableFromSel)

        ### previewImageDock
        self.imagePreviewLabel = QtWidgets.QLabel(self.previewImageDock)
        self.imagePreviewLabel.setGeometry(QtCore.QRect(5, 30, 280, 280))
        self.imagePreviewLabel.setStyleSheet("background-color:#333333;\
                                                  border-radius:10px;\
                                                  border-style:solid;\
                                                  border-width:1px;\
                                                  border-color:#5E749C")
        self.imagePreviewLabel.setText("")
        self.imagePreviewLabel.setPixmap(QtGui.QPixmap())
        self.imagePreviewLabel.setScaledContents(True)
        self.imagePreviewLabel.setObjectName("imagePreview")





        ##### dockWidgetImages

        self.imageListTable = QtWidgets.QTableWidget(self.dockWidgetImages)
        self.imageListTable.clear()
        self.imageListTable.setGeometry(QtCore.QRect(5, 60,280, 570))
        self.imageListTable.setObjectName("tableWidget")

        self.imageListTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageListTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageListTable.horizontalHeader().setVisible(False)
        self.imageListTable.verticalHeader().setVisible(False)
        self.imageListTable.setStyleSheet(tableA);





        ##### workSpaceInfoDock
        
        
        self.environmentSetGrp = QtWidgets.QGroupBox(self.workSpaceInfoDock)
        self.environmentSetGrp.setGeometry(QtCore.QRect(10, 20, 530, 215))
        self.environmentSetGrp.setObjectName("environmentSetGrp")
        self.environmentSetGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.environmentSetGrp.setStyleSheet(QGroupBoxA)     
        self.environmentSetGrp.setVisible(True)
        
        
        
        
        self.selectSpineWorkSpaceBtn = QtWidgets.QPushButton(self.environmentSetGrp)
        self.selectSpineWorkSpaceBtn.setGeometry(QtCore.QRect(10, 20, 110,30))
        self.selectSpineWorkSpaceBtn.setObjectName("selectSpineWorkSpaceBtn")
        self.selectSpineWorkSpaceBtn.setText(QtWidgets.QApplication.translate("MainWindow", "work space", None, -1))
        self.selectSpineWorkSpaceBtn.clicked.connect(self.defineSpineWorkSpace)
        self.selectSpineWorkSpaceBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.spineWorkSpaceLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
        self.spineWorkSpaceLEdit.setGeometry(QtCore.QRect(120, 20, 400, 30))
        self.spineWorkSpaceLEdit.setObjectName("spineWorkSpaceLEdit")
        self.spineWorkSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineWorkSpaceLEdit.setText('')
        self.spineWorkSpaceLEdit.setStyleSheet(lineEditRightB)     
        
        
        self.selectImageDitBtn = QtWidgets.QPushButton(self.environmentSetGrp)
        self.selectImageDitBtn.setGeometry(QtCore.QRect(10, 60, 110,30))
        self.selectImageDitBtn.setObjectName("selectImageDitBtn")
        self.selectImageDitBtn.setText(QtWidgets.QApplication.translate("MainWindow", "images Folder", None, -1))
       # self.selectImageDitBtn.clicked.connect(self.defineSpineWorkSpace)
        self.selectImageDitBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.spineImagesSpaceLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
        self.spineImagesSpaceLEdit.setGeometry(QtCore.QRect(120, 60, 400, 30))
        self.spineImagesSpaceLEdit.setObjectName("spineImagesSpaceLEdit")
        self.spineImagesSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineImagesSpaceLEdit.setText('')
        self.spineImagesSpaceLEdit.setStyleSheet(lineEditRightB)     
        
        self.selectExportFolderBtn = QtWidgets.QPushButton(self.environmentSetGrp)
        self.selectExportFolderBtn.setGeometry(QtCore.QRect(10, 100, 110,30))
        self.selectExportFolderBtn.setObjectName("selectExportFolderBtn")
        self.selectExportFolderBtn.setText(QtWidgets.QApplication.translate("MainWindow", "export Folder", None, -1))
       # self.selectExportFolderBtn.clicked.connect(self.defineSpineWorkSpace)
        self.selectExportFolderBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.spineExportSpaceLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
        self.spineExportSpaceLEdit.setGeometry(QtCore.QRect(120, 100, 400, 30))
        self.spineExportSpaceLEdit.setObjectName("spineExportSpaceLEdit")
        self.spineExportSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineExportSpaceLEdit.setText('')
        self.spineExportSpaceLEdit.setStyleSheet(lineEditRightB)  




        self.createBGBtn = QtWidgets.QPushButton(self.environmentSetGrp)
        self.createBGBtn.setGeometry(QtCore.QRect(10, 140, 110, 30))
        self.createBGBtn.setObjectName("createBGBtn")
        self.createBGBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Define BG", None, -1))
        self.createBGBtn.clicked.connect(self.defineCreateBGBtn)
        self.createBGBtn.setStyleSheet(buttonStyleLeftB)


        self.createBG_comboBox = QtWidgets.QComboBox(self.environmentSetGrp)
        self.createBG_comboBox.setGeometry(QtCore.QRect(120, 140, 400, 30))
        self.createBG_comboBox.setObjectName("comboBox")
        itemNameList = ["100x100","200x200","250x250","300x300","400x400",
                         "512x512","600x600","800x800","1000x1000","1024x1024",
                         "1200x1200","1500x1500","1600x1600","1920x1080","1920x1920","2000x2000","2048x2048"]
        for i in range(0,len(itemNameList)):
            self.createBG_comboBox.addItem("")
            self.createBG_comboBox.setItemText(i, QtWidgets.QApplication.translate("MainWindow", itemNameList[i], None, -1))

        self.createBG_comboBox.setCurrentIndex(13)
        self.createBG_comboBox.setStyleSheet(lineEditRightB)
          
          
        self.jointSizeLabel = QtWidgets.QLabel(self.environmentSetGrp)
        self.jointSizeLabel.setGeometry(QtCore.QRect(30, 180, 500, 30))
        self.jointSizeLabel.setObjectName("jointSizeLabel")
        self.jointSizeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "joint size", None, -1))

        self.jointSizeValueLabel = QtWidgets.QLabel(self.environmentSetGrp)
        self.jointSizeValueLabel.setGeometry(QtCore.QRect(100, 180, 500, 30))
        self.jointSizeValueLabel.setObjectName("jointSizeLabel")
        self.jointSizeValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", "10", None, -1))

        self.horizontalSlider = QtWidgets.QSlider(self.environmentSetGrp)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 180, 300, 30))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")





        ##



       # self.createMeshBtn.setStyleSheet(buttonStyle)             
       # self.createClippingBtn.setStyleSheet(buttonStyle)             


        #self.testABtn.setStyleSheet(buttonStyle)             
        #self.testBBtn.setStyleSheet(buttonStyle)             
        #self.testCBtn.setStyleSheet(buttonStyle)             



        #### dockSpineMeshProgress BTN


        self.characterCreateBtn = QtWidgets.QPushButton(self.dockSpineMeshProgress)
        self.characterCreateBtn.setGeometry(QtCore.QRect(10, 20, 80, 30))
        self.characterCreateBtn.setObjectName("initialSpineRootBtn")
        self.characterCreateBtn.setCheckable(True)
        self.characterCreateBtn.setChecked(True)
        self.characterCreateBtn.setFlat(False)
        self.characterCreateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Character", None, -1))
       # self.characterCreateBtn.clicked.connect(self.defineSpineRootSkeleton)
        self.characterCreateBtn.setStyleSheet(buttonStyleC)  

        
        self.defineSpineBoneBtn = QtWidgets.QPushButton(self.dockSpineMeshProgress)
        self.defineSpineBoneBtn.setGeometry(QtCore.QRect(95, 20, 80, 30))
        self.defineSpineBoneBtn.setObjectName("defineSpineBoneBtn")
        self.defineSpineBoneBtn.setCheckable(True)
        self.defineSpineBoneBtn.setChecked(False)
        self.defineSpineBoneBtn.setFlat(False)
        self.defineSpineBoneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Bone", None, -1))
       # self.characterCreateBtn.clicked.connect(self.defineSpineRootSkeleton)
        self.defineSpineBoneBtn.setStyleSheet(buttonStyleC)          
                
                        
        self.defineSpineMaskBtn = QtWidgets.QPushButton(self.dockSpineMeshProgress)
        self.defineSpineMaskBtn.setGeometry(QtCore.QRect(180, 20, 80, 30))
        self.defineSpineMaskBtn.setObjectName("defineSpineMaskBtn")
        self.defineSpineMaskBtn.setCheckable(True)
        self.defineSpineMaskBtn.setChecked(False)
        self.defineSpineMaskBtn.setFlat(False)
        self.defineSpineMaskBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Mask", None, -1))
       # self.characterCreateBtn.clicked.connect(self.defineSpineRootSkeleton)
        self.defineSpineMaskBtn.setStyleSheet(buttonStyleC)          
        
        
        
        
        
        self.exportSpineJsonCheckBtn = QtWidgets.QPushButton(self.dockSpineMeshProgress)
        self.exportSpineJsonCheckBtn.setGeometry(QtCore.QRect(300, 20, 80, 30))
        self.exportSpineJsonCheckBtn.setObjectName("exportSpineJsonCheckBtn")
        self.exportSpineJsonCheckBtn.setCheckable(True)
        self.exportSpineJsonCheckBtn.setChecked(False)
        self.exportSpineJsonCheckBtn.setFlat(False)
        self.exportSpineJsonCheckBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Export", None, -1))
       # self.characterCreateBtn.clicked.connect(self.defineSpineRootSkeleton)
        self.exportSpineJsonCheckBtn.setStyleSheet(buttonStyleC)          
        
        

        self.errorMsgLEdit = QtWidgets.QLineEdit(self.dockSpineMeshProgress)
        self.errorMsgLEdit.setGeometry(QtCore.QRect(10, 55,370, 60))
        self.errorMsgLEdit.setObjectName("errorMsgLEdit")
        self.errorMsgLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.errorMsgLEdit.setText('')
        self.errorMsgLEdit.setStyleSheet(errMsgA)     
             

        
        self.defineSpineCharacterGrpBox = QtWidgets.QGroupBox(self.dockSpineMeshProgress)
        self.defineSpineCharacterGrpBox.setGeometry(QtCore.QRect(10, 120, 370, 230))
        self.defineSpineCharacterGrpBox.setObjectName("defineSpineCharacterGrpBox")
        self.defineSpineCharacterGrpBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.defineSpineCharacterGrpBox.setStyleSheet(QGroupBoxA)     
        self.defineSpineCharacterGrpBox.setVisible(True)

 
        self.initialSpineRootBtn = QtWidgets.QPushButton(self.defineSpineCharacterGrpBox)
        self.initialSpineRootBtn.setGeometry(QtCore.QRect(10, 20, 150, 30))
        self.initialSpineRootBtn.setObjectName("initialSpineRootBtn")
        self.initialSpineRootBtn.setText(QtWidgets.QApplication.translate("MainWindow", "initial Spine Root", None, -1))
        self.initialSpineRootBtn.clicked.connect(self.defineSpineRootSkeleton)
        self.initialSpineRootBtn.setStyleSheet(buttonStyleLeft)     
        
        self.spineRootLEdit = QtWidgets.QLineEdit(self.defineSpineCharacterGrpBox)
        self.spineRootLEdit.setGeometry(QtCore.QRect(160, 20, 200, 30))
        self.spineRootLEdit.setObjectName("spineRootLEdit")
        self.spineRootLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineRootLEdit.setText('spine_RootSkeleton')
        self.spineRootLEdit.setStyleSheet(lineEditRight)  


        
        
        self.createCharacterGrpBTn = QtWidgets.QPushButton(self.defineSpineCharacterGrpBox)
        self.createCharacterGrpBTn.setGeometry(QtCore.QRect(30, 60, 130,30))
        self.createCharacterGrpBTn.setObjectName("createCharacterGrp")
        self.createCharacterGrpBTn.setText(QtWidgets.QApplication.translate("MainWindow", "create Character Set", None, -1))
        self.createCharacterGrpBTn.clicked.connect(self.createCharacterGrp)
        self.createCharacterGrpBTn.setStyleSheet(buttonStyleLeftB)     

 
        self.characterNameLEdit = QtWidgets.QLineEdit(self.defineSpineCharacterGrpBox)
        self.characterNameLEdit.setGeometry(QtCore.QRect(160, 60, 200, 30))
        self.characterNameLEdit.setObjectName("rootJointLineEdit")
        self.characterNameLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.characterNameLEdit.setText('')
        self.characterNameLEdit.setStyleSheet(lineEditRightB)     
        
        self.createRootBtn = QtWidgets.QPushButton(self.defineSpineCharacterGrpBox)
        self.createRootBtn.setGeometry(QtCore.QRect(30, 100, 130, 30))
        self.createRootBtn.setObjectName("createRoot")
        self.createRootBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Root", None, -1))
        self.createRootBtn.clicked.connect(self.createRootCtrl)
        self.createRootBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.rootNameEdit = QtWidgets.QLineEdit(self.defineSpineCharacterGrpBox)
        self.rootNameEdit.setGeometry(QtCore.QRect(160, 100, 140, 30))
        self.rootNameEdit.setObjectName("rootNameEdit")
        self.rootNameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rootNameEdit.setText('')
        self.rootNameEdit.setStyleSheet(lineEditRightBMiddle)           
        
        self.rootCtrlScaleEdit = QtWidgets.QLineEdit(self.defineSpineCharacterGrpBox)
        self.rootCtrlScaleEdit.setGeometry(QtCore.QRect(300,100, 60, 30))
        self.rootCtrlScaleEdit.setObjectName("rootCtrlScaleEdit")
        self.rootCtrlScaleEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rootCtrlScaleEdit.setText('10.0')
        self.rootCtrlScaleEdit.setStyleSheet(lineEditRightB)           
        


        self.createImagePlaneBtn = QtWidgets.QPushButton(self.defineSpineCharacterGrpBox)
        self.createImagePlaneBtn.setGeometry(QtCore.QRect(30, 140, 130,30))
        self.createImagePlaneBtn.setObjectName("createImagePlaneBtn")
        self.createImagePlaneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Image Plane", None, -1))
        self.createImagePlaneBtn.clicked.connect(self.createImagePlane)
        self.createImagePlaneBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.imageSourceLEdit = QtWidgets.QLineEdit(self.defineSpineCharacterGrpBox)
        self.imageSourceLEdit.setGeometry(QtCore.QRect(160, 140, 200, 30))
        self.imageSourceLEdit.setObjectName("imageSourceLEdit")
        self.imageSourceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.imageSourceLEdit.setText('')
        self.imageSourceLEdit.setStyleSheet(lineEditRightB)     
        


        self.defineMeshBtn = QtWidgets.QPushButton(self.defineSpineCharacterGrpBox)
        self.defineMeshBtn.setGeometry(QtCore.QRect(30, 180, 330, 30))
        self.defineMeshBtn.setObjectName("defineMesh")
        self.defineMeshBtn.setText(QtWidgets.QApplication.translate("MainWindow", "define Mesh", None, -1))
        self.defineMeshBtn.clicked.connect(self.getSkinData)
        self.defineMeshBtn.setStyleSheet(buttonStyleB)     
        
        ###### defineSpineSlotBoneGrpBox
        self.defineSpineSlotBoneGrpBox = QtWidgets.QGroupBox(self.dockSpineMeshProgress )
        self.defineSpineSlotBoneGrpBox.setGeometry(QtCore.QRect(10, 355, 370, 170))
        self.defineSpineSlotBoneGrpBox.setObjectName("defineSpineCharacterGrpBox")
        self.defineSpineSlotBoneGrpBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.defineSpineSlotBoneGrpBox.setStyleSheet(QGroupBoxA)     
        self.defineSpineSlotBoneGrpBox.setVisible(True)
     
        

        self.createSlotBtn = QtWidgets.QPushButton(self.defineSpineSlotBoneGrpBox)
        self.createSlotBtn.setGeometry(QtCore.QRect(30, 50, 330, 30))
        self.createSlotBtn.setObjectName("createSlot")
        self.createSlotBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Slot", None, -1))
        self.createSlotBtn.clicked.connect(self.createSlot)              
        self.createSlotBtn.setStyleSheet(buttonStyleB)   
        

        
        self.createBoneBtn = QtWidgets.QPushButton(self.defineSpineSlotBoneGrpBox)
        self.createBoneBtn.setGeometry(QtCore.QRect(30, 10, 120, 30))
        self.createBoneBtn.setObjectName("createBoneBtn")
        self.createBoneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Clean Bone", None, -1))
        self.createBoneBtn.clicked.connect(self.createCleanBone)
        self.createBoneBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.createBoneNameLEdit = QtWidgets.QLineEdit(self.defineSpineSlotBoneGrpBox)
        self.createBoneNameLEdit.setGeometry(QtCore.QRect(150, 10, 210, 30))
        self.createBoneNameLEdit.setObjectName("createBoneNameLEdit")
        self.createBoneNameLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.createBoneNameLEdit.setText('')
        
        self.createBoneNameLEdit.setStyleSheet(lineEditRightB)     
        
        
     
        self.slotAmountLabel = QtWidgets.QLabel(self.defineSpineSlotBoneGrpBox)
        self.slotAmountLabel.setGeometry(QtCore.QRect(35, 70, 500, 50))
        self.slotAmountLabel.setObjectName("slotAmountLabel")
        self.slotAmountLabel.setText(QtWidgets.QApplication.translate("MainWindow", "slot amount", None, -1))
        
        self.amountSliderNumLEdit = QtWidgets.QLineEdit(self.defineSpineSlotBoneGrpBox)
        self.amountSliderNumLEdit.setGeometry(QtCore.QRect(30, 110, 60, 30))
        self.amountSliderNumLEdit.setObjectName("amountSliderNumLEdit")
        self.amountSliderNumLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.amountSliderNumLEdit.setText('1')
        self.amountSliderNumLEdit.textChanged.connect(self.slotAmountEditChange)
        self.amountSliderNumLEdit.setStyleSheet(lineEditA)            
        
   
        self.amountSlotSlider = QtWidgets.QSlider(self.defineSpineSlotBoneGrpBox)
        self.amountSlotSlider.setGeometry(QtCore.QRect(100, 110, 250, 30))
        self.amountSlotSlider.setMinimum(1)
        self.amountSlotSlider.setMaximum(300)
        self.amountSlotSlider.setProperty("value", 1)
        self.amountSlotSlider.setOrientation(QtCore.Qt.Horizontal)
        self.amountSlotSlider.setObjectName("amountSlotSlider")
        self.amountSlotSlider.valueChanged.connect(self.slotAmountSliderChange)
        
        
        
        self.enableDynaSlotCheck = QtWidgets.QCheckBox(self.defineSpineSlotBoneGrpBox)
        self.enableDynaSlotCheck.setGeometry(QtCore.QRect(30, 145, 120, 20))
        #self.enableDynaSlotCheck.setChecked(True)
        self.enableDynaSlotCheck.setObjectName("enableDynaSlotCheck")
        self.enableDynaSlotCheck.setText(QtWidgets.QApplication.translate("MainWindow", "Dynamic Slot", None, -1))
        self.enableDynaSlotCheck.setStyleSheet(lineEditA)   

     
        
        
        
      #  self.amountSlotSlider.setStyleSheet(lineEditA)

        self.dynamicSlotGrp = QtWidgets.QGroupBox(self.dockSpineMeshProgress )
        self.dynamicSlotGrp.setGeometry(QtCore.QRect(10,530, 370, 300))
        self.dynamicSlotGrp.setObjectName("dynamicSlotGrp")
        self.dynamicSlotGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.dynamicSlotGrp.setStyleSheet(QGroupBoxA)     
        self.dynamicSlotGrp.setVisible(True)
        self.dynamicSlotGrp.setEnabled(False)
     

 
       #### define dynamic slots
     
             
                  
                       
                                 
        
        radioBtnStyleA =  "\
                 QRadioButton {\
                 text-align:center;\
                 color:#aaaaaa;\
                 }\
                 QRadioButton:Disable {\
                 text-align:center;\
                 color:#333333;\
                 }\
                 "     
        optionLabelA  = "\
                         QLabel {\
                         font-size:%s;\
                         color:#bbbbbb;\
                         text-align:right;\
                         }\
                         "%(str(self.fontScale*12)+'px')    
        optionEditA  = "\
                         QLineEdit {\
                         font-size:%s;\
                         background-color:#333333;\
                         color:#aaaaaa;\
                         border-radius:3px;\
                         border-style:solid;\
                         border-color:#777777;\
                         text-align:center;\
                         };\
                         QLineEdit::hover{\
                         font-size:%s;\
                         background-color:#993333;\
                         color:#aaaaaa;\
                         border-radius:3px;\
                         border-style:solid;\
                         border-color:#777777;\
                         text-align:center;\
                         };\
                         QLineEdit:read-only {\
                         font-size:%s;\
                         background-color:#777777;\
                         color:#333333;\
                         border-radius:3px;\
                         border-style:solid;\
                         border-color:#777777;\
                         text-align:center;\
                         }\
                         "%((str(self.fontScale*12)+'px'),(str(self.fontScale*12)+'px'),(str(self.fontScale*12)+'px'))

        
        self.slotDynaStartFrame = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.slotDynaStartFrame.setGeometry(QtCore.QRect(20, 10, 60, 20))
        self.slotDynaStartFrame.setObjectName("slotDynaStartFrame")
        self.slotDynaStartFrame.setText(QtWidgets.QApplication.translate("MainWindow", "Start Frame", None, -1))  
       # self.slotDynaStartFrame.setStyleSheet(optionLabelA)   
        
        self.lineEdit_shapeStartFrame = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_shapeStartFrame.setGeometry(QtCore.QRect(90, 10, 40, 20))
        self.lineEdit_shapeStartFrame.setObjectName("lineEdit_shapeStartFrame")       
        self.lineEdit_shapeStartFrame.setText(QtWidgets.QApplication.translate("MainWindow", "1.0", None, -1))  
       # self.lineEdit_shapeStartFrame.setStyleSheet(optionEditA)   
       
        
        self.slotDynaEndFrame = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.slotDynaEndFrame.setGeometry(QtCore.QRect(140, 10, 60, 20))
        self.slotDynaEndFrame.setObjectName("slotDynaEndFrame")
        self.slotDynaEndFrame.setText(QtWidgets.QApplication.translate("MainWindow", "End Frame", None, -1))  
       # self.slotDynaEndFrame.setStyleSheet(optionLabelA)   

        self.lineEdit_shapeEndFrame = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_shapeEndFrame.setGeometry(QtCore.QRect(210, 10, 40, 20))
        self.lineEdit_shapeEndFrame.setObjectName("lineEdit_shapeEndFrame")
        self.lineEdit_shapeEndFrame.setText(QtWidgets.QApplication.translate("MainWindow", "20.0", None, -1))  
       # self.lineEdit_shapeEndFrame.setStyleSheet(optionEditA)   

        self.checkBox_offsetRandom = QtWidgets.QCheckBox(self.dynamicSlotGrp)
        self.checkBox_offsetRandom.setGeometry(QtCore.QRect(270, 10, 73, 20))
        self.checkBox_offsetRandom.setChecked(True)
        self.checkBox_offsetRandom.setObjectName("checkBox_offsetRandom")
        self.checkBox_offsetRandom.setText(QtWidgets.QApplication.translate("MainWindow", "random", None, -1))
       # self.checkBox_offsetRandom.setStyleSheet(optionEditA)   





        #### dyna Raditional
        self.radioButton_createRad = QtWidgets.QRadioButton(self.dynamicSlotGrp)
        self.radioButton_createRad.setGeometry(QtCore.QRect(20, 40, 70, 20))
        self.radioButton_createRad.setChecked(True)
        self.radioButton_createRad.setObjectName("radioButton_createRad")
        self.radioButton_createRad.setText(QtWidgets.QApplication.translate("MainWindow", "Radiation", None, -1))
        #self.radioButton_createRad.setStyleSheet(radioBtnStyleA)     
        
        self.RValueLabel = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.RValueLabel.setGeometry(QtCore.QRect(100, 40, 30, 20))
        self.RValueLabel.setObjectName("RValueLabel")
        self.RValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", "R:", None, -1))
        #self.RValueLabel.setStyleSheet(optionLabelA)   
        
        self.lineEdit_RadiusA = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_RadiusA.setEnabled(True)
        self.lineEdit_RadiusA.setGeometry(QtCore.QRect(115, 40, 40, 20))
        self.lineEdit_RadiusA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_RadiusA.setObjectName("lineEdit_RadiusA") 
      #  self.lineEdit_RadiusA.setStyleSheet(optionEditA)   

        #### dyna Square
        self.radioButton_createSquare = QtWidgets.QRadioButton(self.dynamicSlotGrp)
        self.radioButton_createSquare.setGeometry(QtCore.QRect(20, 70, 70, 20))
        self.radioButton_createSquare.setObjectName("radioButton_createSquare")  
        self.radioButton_createSquare.setText(QtWidgets.QApplication.translate("MainWindow", "Square", None, -1))
       # self.radioButton_createSquare.setStyleSheet(radioBtnStyleA)        
         
        self.lineEdit_widthSquare = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_widthSquare.setEnabled(False)
        self.lineEdit_widthSquare.setGeometry(QtCore.QRect(115, 70, 40, 20))
        self.lineEdit_widthSquare.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_widthSquare.setObjectName("lineEdit_widthSquare")
      #  self.lineEdit_widthSquare.setStyleSheet(optionEditA)   
        
        self.label_WidthSquare = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_WidthSquare.setGeometry(QtCore.QRect(100, 70, 30, 20))
        self.label_WidthSquare.setObjectName("label_WidthSquare")
        self.label_WidthSquare.setText(QtWidgets.QApplication.translate("MainWindow", "W:", None, -1))
        #self.label_WidthSquare.setStyleSheet(optionLabelA)   

        self.lineEdit_HeightA = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_HeightA.setEnabled(False)
        self.lineEdit_HeightA.setGeometry(QtCore.QRect(175,70, 40, 20))
        self.lineEdit_HeightA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
        self.lineEdit_HeightA.setObjectName("lineEdit_HeightA")                  
      #  self.lineEdit_HeightA.setStyleSheet(optionEditA)   
        

        self.label_HeighthSquare = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_HeighthSquare.setGeometry(QtCore.QRect(160, 70, 30, 20))
        self.label_HeighthSquare.setObjectName("label_HeighthSquare")                    
        self.label_HeighthSquare.setText(QtWidgets.QApplication.translate("MainWindow", "H:", None, -1))
        #self.label_HeighthSquare.setStyleSheet(optionLabelA)                      
                        
        self.checkBox_squareFillIn = QtWidgets.QCheckBox(self.dynamicSlotGrp)
        self.checkBox_squareFillIn.setGeometry(QtCore.QRect(240, 70, 70, 20))
        self.checkBox_squareFillIn.setChecked(False)
        self.checkBox_squareFillIn.setObjectName("checkBox_squareFillIn")   
        self.checkBox_squareFillIn.setText(QtWidgets.QApplication.translate("MainWindow", "Fill in", None, -1))
        #self.checkBox_squareFillIn.setStyleSheet(optionEditA)   
 
        self.checkBox_squareAimO = QtWidgets.QCheckBox(self.dynamicSlotGrp)
        self.checkBox_squareAimO.setGeometry(QtCore.QRect(300, 70, 70, 20))
        self.checkBox_squareAimO.setChecked(False)
        self.checkBox_squareAimO.setObjectName("checkBox_squareAimO")   
        self.checkBox_squareAimO.setText(QtWidgets.QApplication.translate("MainWindow", "Aim O.O", None, -1))
        #self.checkBox_squareFillIn.setStyleSheet(optionEditA)                             
           
    ### set dyna sector
            
        self.radioButton_createSector = QtWidgets.QRadioButton(self.dynamicSlotGrp)
        self.radioButton_createSector.setGeometry(QtCore.QRect(20, 100, 70, 20))
        self.radioButton_createSector.setObjectName("radioButton_createSector")
        self.radioButton_createSector.setText(QtWidgets.QApplication.translate("MainWindow", "Sector", None, -1))
        #self.radioButton_createSector.setStyleSheet(radioBtnStyleA)        

                                                                                                              
        self.label_dynaSectorDegree = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_dynaSectorDegree.setGeometry(QtCore.QRect(100, 100, 30, 20))
        self.label_dynaSectorDegree.setObjectName("label_dynaSectorDegree")                                                
        self.label_dynaSectorDegree.setText(QtWidgets.QApplication.translate("MainWindow", "D:", None, -1))
       # self.label_dynaSectorDegree.setStyleSheet(optionLabelA)                      
                                                                     
        self.lineEdit_AngleA_start = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_AngleA_start.setEnabled(False)
        self.lineEdit_AngleA_start.setGeometry(QtCore.QRect(115, 100, 40, 20))
        self.lineEdit_AngleA_start.setText(QtWidgets.QApplication.translate("MainWindow", "-90", None, -1))
        self.lineEdit_AngleA_start.setObjectName("lineEdit_AngleA_start")
    #    self.lineEdit_AngleA_start.setStyleSheet(optionEditA)   

        self.lineEdit_AngleA_end = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_AngleA_end.setEnabled(False)
        self.lineEdit_AngleA_end.setGeometry(QtCore.QRect(175, 100, 40, 20))
        self.lineEdit_AngleA_end.setText(QtWidgets.QApplication.translate("MainWindow", "90", None, -1))
        self.lineEdit_AngleA_end.setObjectName("lineEdit_AngleA_end")    
       # self.lineEdit_AngleA_end.setStyleSheet(optionEditA)   


    #### set dyna direction
        self.radioButton_createDirection = QtWidgets.QRadioButton(self.dynamicSlotGrp)
        self.radioButton_createDirection.setGeometry(QtCore.QRect(20, 130, 70, 20))
        self.radioButton_createDirection.setObjectName("radioButton_createDirection")
        
        self.radioButton_createDirection.setText(QtWidgets.QApplication.translate("MainWindow", "Direction", None, -1))
        #self.radioButton_createDirection.setStyleSheet(radioBtnStyleA)        

        self.label_dynDirectionX = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_dynDirectionX.setGeometry(QtCore.QRect(100, 130, 30, 20))
        self.label_dynDirectionX.setObjectName("label_dynDirectionX")
        self.label_dynDirectionX.setText(QtWidgets.QApplication.translate("MainWindow", "X:", None, -1))
       # self.label_dynDirectionX.setStyleSheet(optionLabelA)    
        
                          
        self.lineEdit_DirectionX = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_DirectionX.setEnabled(False)
        self.lineEdit_DirectionX.setGeometry(QtCore.QRect(115, 130, 40, 20))
        self.lineEdit_DirectionX.setObjectName("lineEdit_DirectionX")    
        self.lineEdit_DirectionX.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))                                                       
      #  self.lineEdit_DirectionX.setStyleSheet(optionEditA)   

        self.label_dynDirectionY = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_dynDirectionY.setGeometry(QtCore.QRect(160, 130, 30, 20))
        self.label_dynDirectionY.setObjectName("label_dynDirectionY")
        self.label_dynDirectionY.setText(QtWidgets.QApplication.translate("MainWindow", "Y:", None, -1))
       # self.label_dynDirectionY.setStyleSheet(optionLabelA)    
        
        self.lineEdit_DirectionY = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_DirectionY.setEnabled(False)
        self.lineEdit_DirectionY.setGeometry(QtCore.QRect(175, 130, 40, 20))
        self.lineEdit_DirectionY.setObjectName("lineEdit_DirectionY")
        self.lineEdit_DirectionY.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))  
      #  self.lineEdit_DirectionY.setStyleSheet(optionEditA)   
        
        self.label_dynDirectionD = QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_dynDirectionD.setGeometry(QtCore.QRect(220, 130, 30, 20))
        self.label_dynDirectionD.setObjectName("label_dynDirectionD")     
        self.label_dynDirectionD.setText(QtWidgets.QApplication.translate("MainWindow", "D:", None, -1))
        #self.label_dynDirectionD.setStyleSheet(optionLabelA)    
        
       
        self.lineEdit_directionDegree = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_directionDegree.setEnabled(False)
        self.lineEdit_directionDegree.setGeometry(QtCore.QRect(240, 130, 40, 20))
        self.lineEdit_directionDegree.setObjectName("lineEdit_directionDegree") 
       # self.lineEdit_directionDegree.setStyleSheet(optionEditA)   
        self.lineEdit_directionDegree.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
      #  self.lineEdit_directionDegree.setStyleSheet(optionEditA)   

        
        
        self.label_dynDirectionS= QtWidgets.QLabel(self.dynamicSlotGrp)
        self.label_dynDirectionS.setGeometry(QtCore.QRect(285, 130, 30, 20))
        self.label_dynDirectionS.setObjectName("label_dynDirectionS")
        self.label_dynDirectionS.setText(QtWidgets.QApplication.translate("MainWindow", "S:", None, -1))
        
        self.lineEdit_directionSpread = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_directionSpread.setEnabled(False)
        self.lineEdit_directionSpread.setGeometry(QtCore.QRect(300, 130, 40, 20))
        self.lineEdit_directionSpread.setObjectName("lineEdit_directionSpread")
        self.lineEdit_directionSpread.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
      #  self.lineEdit_directionSpread.setStyleSheet(optionEditA)   



    #### dyna set follow curve
        self.radioButton_createFollowCurve = QtWidgets.QRadioButton(self.dynamicSlotGrp)
        self.radioButton_createFollowCurve.setGeometry(QtCore.QRect(20, 160, 110, 20))
        self.radioButton_createFollowCurve.setObjectName("radioButton_createFollowCurve")
        self.radioButton_createFollowCurve.setText(QtWidgets.QApplication.translate("MainWindow", "Follow Curve", None, -1))
       # self.radioButton_createFollowCurve.setStyleSheet(radioBtnStyleA)        


        self.lineEdit_selectCurve = QtWidgets.QLineEdit(self.dynamicSlotGrp)
        self.lineEdit_selectCurve.setEnabled(False)
        self.lineEdit_selectCurve.setGeometry(QtCore.QRect(120, 160, 220, 20))
        self.lineEdit_selectCurve.setObjectName("lineEdit_selectCurve")
        self.lineEdit_selectCurve.setText(QtWidgets.QApplication.translate("MainWindow", "select curve", None, -1))
        #self.lineEdit_selectCurve.setStyleSheet(optionEditA)   


        self.toolButton_selectCurve = QtWidgets.QToolButton(self.dynamicSlotGrp)
        self.toolButton_selectCurve.setEnabled(False)
        self.toolButton_selectCurve.setGeometry(QtCore.QRect(340, 160, 20, 20))
        self.toolButton_selectCurve.setObjectName("toolButton_selectCurve")
        self.toolButton_selectCurve.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))

        self.groupBox_keysOption = QtWidgets.QGroupBox(self.dynamicSlotGrp)
        self.groupBox_keysOption.setGeometry(QtCore.QRect(30, 200, 331, 91))
        self.groupBox_keysOption.setTitle("")
        self.groupBox_keysOption.setObjectName("groupBox_keysOption")

        self.label_dynCurveKeys = QtWidgets.QLabel(self.groupBox_keysOption)
        self.label_dynCurveKeys.setGeometry(QtCore.QRect(20, 10, 25, 16))
        self.label_dynCurveKeys.setObjectName("label_dynCurveKeys")
        self.label_dynCurveKeys.setText(QtWidgets.QApplication.translate("MainWindow", "Keys", None, -1))
        self.label_dynCurveKeys.setStyleSheet(optionEditA)    
       
        self.lineEdit_keys = QtWidgets.QLineEdit(self.groupBox_keysOption)
        self.lineEdit_keys.setEnabled(False)
        self.lineEdit_keys.setGeometry(QtCore.QRect(60, 10, 40, 16))
        self.lineEdit_keys.setObjectName("lineEdit_keysA")    
        self.lineEdit_keys.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
    #    self.lineEdit_keys.setStyleSheet(optionEditA)    
        
        
        self.label_dynCurveNoise = QtWidgets.QLabel(self.groupBox_keysOption)
        self.label_dynCurveNoise.setGeometry(QtCore.QRect(20, 35, 41, 16))
        self.label_dynCurveNoise.setObjectName("label_dynCurveNoise")
        self.label_dynCurveNoise.setText(QtWidgets.QApplication.translate("MainWindow", "Noise:", None, -1))
        self.label_dynCurveNoise.setStyleSheet(optionEditA)    
        
        self.lineEdit_NoiseA = QtWidgets.QLineEdit(self.groupBox_keysOption)
        self.lineEdit_NoiseA.setEnabled(False)
        self.lineEdit_NoiseA.setGeometry(QtCore.QRect(60, 35, 40, 16))
        self.lineEdit_NoiseA.setObjectName("lineEdit_NoiseA")     
        self.lineEdit_NoiseA.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
      #  self.lineEdit_NoiseA.setStyleSheet(optionEditA)    
                
        

        self.label_dynCurvePow = QtWidgets.QLabel(self.groupBox_keysOption)
        self.label_dynCurvePow.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_dynCurvePow.setObjectName("label_ef_16")    
        self.label_dynCurvePow.setText(QtWidgets.QApplication.translate("MainWindow", "Pow:", None, -1))
        self.label_dynCurvePow.setStyleSheet(optionEditA)    

        
        self.lineEdit_pow = QtWidgets.QLineEdit(self.groupBox_keysOption)
        self.lineEdit_pow.setEnabled(False)
        self.lineEdit_pow.setGeometry(QtCore.QRect(60, 60, 40, 16))
        self.lineEdit_pow.setObjectName("lineEdit_pow")
        self.lineEdit_pow.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
      #  self.lineEdit_pow.setStyleSheet(optionEditA)    
                

    
    
        self.horizontalSlider_powA = QtWidgets.QSlider(self.groupBox_keysOption)
        self.horizontalSlider_powA.setGeometry(QtCore.QRect(110, 60, 211, 16))
        self.horizontalSlider_powA.setMinimum(1)
        self.horizontalSlider_powA.setMaximum(100)
        self.horizontalSlider_powA.setProperty("value", 10)
        self.horizontalSlider_powA.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_powA.setObjectName("horizontalSlider_powA")

        self.horizontalSlider_NoiseA = QtWidgets.QSlider(self.groupBox_keysOption)
        self.horizontalSlider_NoiseA.setGeometry(QtCore.QRect(110, 35, 211, 16))
        self.horizontalSlider_NoiseA.setMinimum(0)
        self.horizontalSlider_NoiseA.setMaximum(500)
        self.horizontalSlider_NoiseA.setProperty("value", 0)
        self.horizontalSlider_NoiseA.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_NoiseA.setObjectName("horizontalSlider_NoiseA")


        self.horizontalSlider_keysA = QtWidgets.QSlider(self.groupBox_keysOption)
        self.horizontalSlider_keysA.setGeometry(QtCore.QRect(110, 10, 211, 16))
        self.horizontalSlider_keysA.setMinimum(2)
        self.horizontalSlider_keysA.setMaximum(50)
        self.horizontalSlider_keysA.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_keysA.setObjectName("horizontalSlider_keysA")
        

        #### extra Grp
        self.extraToolGrp = QtWidgets.QGroupBox(self.dockSpineMeshProgress)
        self.extraToolGrp.setGeometry(QtCore.QRect(10, 835, 370, 200))
        self.extraToolGrp.setTitle("")
        self.extraToolGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   

        self.extraToolGrp.setObjectName("extraToolGrp") 
        self.extraToolGrp.setStyleSheet(QGroupBoxA)     
        self.extraToolGrp.setVisible(True)

        self.startFrameLabel = QtWidgets.QLabel(self.extraToolGrp)
        self.startFrameLabel.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self.startFrameLabel.setObjectName("startFrameLabel")
        self.startFrameLabel.setText(QtWidgets.QApplication.translate("MainWindow", " Start Frame", None, -1))
        self.startFrameLabel.setStyleSheet(labelA)  


        self.timeStartLEdit = QtWidgets.QLineEdit(self.extraToolGrp)
        self.timeStartLEdit.setGeometry(QtCore.QRect(80, 10, 50, 30))
        self.timeStartLEdit.setObjectName("timeStartLEdit")
        self.timeStartLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0.0", None, -1))
        self.timeStartLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeStartLEdit.setStyleSheet(lineEditCMiddle)     

        self.endFrameLabel = QtWidgets.QLabel(self.extraToolGrp)
        self.endFrameLabel.setGeometry(QtCore.QRect(130, 10, 70, 30))
        self.endFrameLabel.setObjectName("endFrameLabel")
        self.endFrameLabel.setText(QtWidgets.QApplication.translate("MainWindow", "  End Frame", None, -1))
        self.endFrameLabel.setStyleSheet(labelAMiddle)  


        self.timeEndLEdit = QtWidgets.QLineEdit(self.extraToolGrp)
        self.timeEndLEdit.setGeometry(QtCore.QRect(200, 10, 60, 30))
        self.timeEndLEdit.setObjectName("timeEndLEdit")
        self.timeEndLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "120.0", None, -1))
        self.timeEndLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEndLEdit.setStyleSheet(lineEditCMiddle)   
        
        self.fpsLabel = QtWidgets.QLabel(self.extraToolGrp)
        self.fpsLabel.setGeometry(QtCore.QRect(260, 10, 50, 30))
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsLabel.setText(QtWidgets.QApplication.translate("MainWindow", "  FPS", None, -1))
        self.fpsLabel.setStyleSheet(labelAMiddle)  
          
        self.fpsLEdit = QtWidgets.QLineEdit(self.extraToolGrp)
        self.fpsLEdit.setGeometry(QtCore.QRect(310, 10, 50, 30))
        self.fpsLEdit.setObjectName("fpsLEdit")
        self.fpsLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "30.0", None, -1))
        self.fpsLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fpsLEdit.setStyleSheet(lineEditC)               
  
        self.exportSpineRootLabel = QtWidgets.QLabel(self.extraToolGrp)
        self.exportSpineRootLabel.setGeometry(QtCore.QRect(10, 50, 110, 30))
        self.exportSpineRootLabel.setObjectName("exportSpineRootLabel")
        self.exportSpineRootLabel.setText(QtWidgets.QApplication.translate("MainWindow", " export Spine Root", None, -1))
        self.exportSpineRootLabel.setStyleSheet(labelA)  
               
        self.exportSpineRootLabelLEdit = QtWidgets.QLineEdit(self.extraToolGrp)
        self.exportSpineRootLabelLEdit.setGeometry(QtCore.QRect(120, 50, 240, 30))
        self.exportSpineRootLabelLEdit.setObjectName("exportSpineRootLabelLEdit")
        self.exportSpineRootLabelLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "spine_RootSkeleton", None, -1))
        self.exportSpineRootLabelLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.exportSpineRootLabelLEdit.setStyleSheet(lineEditC)                                    
 
                                                          
        
        self.selectExportFileBTn = QtWidgets.QPushButton(self.extraToolGrp)
        self.selectExportFileBTn.setGeometry(QtCore.QRect(10, 90, 110,30))
        self.selectExportFileBTn.setObjectName("selectExportFileBTn")
        self.selectExportFileBTn.setText(QtWidgets.QApplication.translate("MainWindow", "file name", None, -1))
        self.selectExportFileBTn.clicked.connect(self.defineExportFileName)
        self.selectExportFileBTn.setStyleSheet(buttonStyleLeftB)     

 
        self.selectExportFileBTnLEdit = QtWidgets.QLineEdit(self.extraToolGrp)
        self.selectExportFileBTnLEdit.setGeometry(QtCore.QRect(120, 90, 240, 30))
        self.selectExportFileBTnLEdit.setObjectName("rootJointLineEdit")
        self.selectExportFileBTnLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.selectExportFileBTnLEdit.setText('')
        self.selectExportFileBTnLEdit.setStyleSheet(lineEditRightB)     

        self.exportToSpineFileBtn = QtWidgets.QPushButton(self.extraToolGrp)
        self.exportToSpineFileBtn.setGeometry(QtCore.QRect(10, 150, 350, 30))
        self.exportToSpineFileBtn.setObjectName("exportToSpineFileBtn")
        self.exportToSpineFileBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Export To Spine", None, -1))
        self.exportToSpineFileBtn.clicked.connect(self.exortTOSpineJson)              
        self.exportToSpineFileBtn.setStyleSheet(buttonStyleB)   
        



              
        self.testBtn = QtWidgets.QPushButton(self.dockSpineItemTree)
        self.testBtn.setGeometry(QtCore.QRect(10, 950, 100, 30))
        self.testBtn.setObjectName("testBtn")
        self.testBtn.setText(QtWidgets.QApplication.translate("MainWindow", "set color", None, -1))
        self.testBtn.setStyleSheet(buttonStyleLeftB)     

        self.testBtn.clicked.connect(self.on_clicked)
        self.testLabel = QtWidgets.QLabel()
        self.testLabel.setAutoFillBackground(True)
        self.testLabel = QtWidgets.QPushButton(self.dockSpineItemTree)
        self.testLabel.setGeometry(QtCore.QRect(130, 950, 100, 30))
        #lay.addWidget(self.testBtn)
        #lay.addWidget(self.testLabel)    
    
    
        

    


        

        self.exportSpineJsonBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.exportSpineJsonBtn.setGeometry(QtCore.QRect(150, 20, 130, 30))
        self.exportSpineJsonBtn.setObjectName("exportSpineJson")
        self.exportSpineJsonBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Export Spine Json", None, -1))
        self.exportSpineJsonBtn.clicked.connect(self.defineAllItemInRootCtrl)
        self.exportSpineJsonBtn.setStyleSheet(buttonStyleB)     

       
        self.analyzeCharacterSet = QtWidgets.QPushButton(self.dockImageButton)
        self.analyzeCharacterSet.setGeometry(QtCore.QRect(10, 20, 130, 30))
        self.analyzeCharacterSet.setObjectName("analyzeCharacterSet")
        self.analyzeCharacterSet.setText(QtWidgets.QApplication.translate("MainWindow", "analyze Character Set", None, -1))
        self.analyzeCharacterSet.clicked.connect(self.doAnalyzeCharacterSet)
        self.analyzeCharacterSet.setStyleSheet(buttonStyleB)     
        
        
        
        self.setCharacterSetBTn = QtWidgets.QPushButton(self.dockImageButton)
        self.setCharacterSetBTn.setGeometry(QtCore.QRect(10, 60, 130, 30))
        self.setCharacterSetBTn.setObjectName("setCharacterSetBTn")
        self.setCharacterSetBTn.setText(QtWidgets.QApplication.translate("MainWindow", "select Character Set", None, -1))
        self.setCharacterSetBTn.clicked.connect(self.setCharacterSetName)
        self.setCharacterSetBTn.setStyleSheet(buttonStyleB)             
        

        self.setCharacterSetLineEdit = QtWidgets.QLineEdit(self.dockImageButton)
        self.setCharacterSetLineEdit.setGeometry(QtCore.QRect(150, 60, 130, 30))
        self.setCharacterSetLineEdit.setObjectName("rootJointLineEdit")
        self.setCharacterSetLineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "Character Set Name", None, -1))
        self.setCharacterSetLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.setCharacterSetLineEdit.setStyleSheet(lineEditA)     



        self.createMeshBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createMeshBtn.setGeometry(QtCore.QRect(290, 20, 100, 30))
        self.createMeshBtn.setObjectName("createMesh")
        self.createMeshBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Mesh", None, -1))
        self.createMeshBtn.clicked.connect(self.definecreateMesh)
        self.createMeshBtn.setStyleSheet(buttonStyleB)             

        self.createClippingBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createClippingBtn.setGeometry(QtCore.QRect(400, 20, 100, 30))
        self.createClippingBtn.setObjectName("createClipping")
        self.createClippingBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Clip", None, -1))
        #self.createClippingBtn.clicked.connect(self.definecreateSlotBtn)
        self.createClippingBtn.setStyleSheet(buttonStyleB)             



        

        self.setRootBoneJointBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.setRootBoneJointBtn.setGeometry(QtCore.QRect(290, 60, 100, 30))
        self.setRootBoneJointBtn.setObjectName("setRootBoneBtn")
        self.setRootBoneJointBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Set Root", None, -1))
        self.setRootBoneJointBtn.clicked.connect(self.defineRootBone)
        self.setRootBoneJointBtn.setStyleSheet(buttonStyleB)             


        self.setRootLineEdit = QtWidgets.QLineEdit(self.dockImageButton)
        self.setRootLineEdit.setGeometry(QtCore.QRect(400, 60, 100, 30))
        self.setRootLineEdit.setObjectName("rootJointLineEdit")
        self.setRootLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.setRootLineEdit.setStyleSheet(lineEditA)             
     
        self.testABtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testABtn.setGeometry(QtCore.QRect(10, 100, 130, 30))
        self.testABtn.setObjectName("setRootBoneBtn")
        self.testABtn.setText(QtWidgets.QApplication.translate("MainWindow", "testA", None, -1))
        self.testABtn.clicked.connect(self.run)
        self.testABtn.setStyleSheet(buttonStyleB)             

        self.testBBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testBBtn.setGeometry(QtCore.QRect(150, 100, 130, 30))
        self.testBBtn.setObjectName("testb")
        self.testBBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testB", None, -1))
        self.testBBtn.clicked.connect(self.defineAllItemInRootCtrl)
        self.testBBtn.setStyleSheet(buttonStyleB)             

        self.testCBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testCBtn.setGeometry(QtCore.QRect(290, 100, 100, 30))
        self.testCBtn.setObjectName("testc")
        self.testCBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testC", None, -1))
        self.testCBtn.clicked.connect(self.defineDeformAnimation)
        self.testCBtn.setStyleSheet(buttonStyleB)             
         
        self.testDBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testDBtn.setGeometry(QtCore.QRect(400, 100, 100, 30))
        self.testDBtn.setObjectName("testDBtn")
        self.testDBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testD", None, -1))
        self.testDBtn.clicked.connect(self.testD)
        self.testDBtn.setStyleSheet(buttonStyleB)     



    def on_clicked(self):
        print "on_clicked"
        color = QtWidgets.QColorDialog.getColor()
        self.testLabel.setAutoFillBackground(True)
        print color
        if color.isValid():
            palette = self.testLabel.palette()
            palette.setColor(QtGui.QPalette.Background, color)
            self.testLabel.setPalette(palette)
    ## modify attribut
    
    
    def defineModX(self):
        min = int(float(self.modTransXminLedit.text()))
        max = int(float(self.modTransXMaxLedit.text()))

        self.defineModByAttr("translateX",min,max)

    
    def defineModY(self):
        min = int(float(self.modTransYminLedit.text()))
        max = int(float(self.modTransYMaxLedit.text()))

        self.defineModByAttr("translateY",min,max)
        
     
    def defineModZ(self):
        min = int(float(self.modTransZminLedit.text()))
        max = int(float(self.modTransZMaxLedit.text()))

        self.defineModByAttr("translateZ",min,max)
               
    def defineModRX(self):
        min = float(self.modRotateXminLedit.text())
        max = float(self.modRotateYMaxLedit.text())

        self.defineModByAttr("rotateX",minX,maxX)                        
                                
    def defineModRY(self):
        min = float(self.modRotateYminLedit.text())
        max = float(self.modRotateXMaxLedit.text())

        self.defineModByAttr("rotateY",min,max)                                       

    def defineModRZ(self):
        min = float(self.modRotateZminLedit.text())
        max = float(self.modRotateYMaxLedit.text())

        self.defineModByAttr("rotateZ",min,max)                                                

    def defineModSX(self):
        min = float(self.modScaleXminLedit.text())
        max = float(self.modScaleXMaxLedit.text())

        self.defineModByAttr("scaleX",min,max)                                                                     
                                                                                                                                
    def defineModSY(self):
        min = float(self.modScaleYminLedit.text())
        max = float(self.modScaleYMaxLedit.text())


        self.defineModByAttr("scaleY",min,max)                                                                     
                                                                                                                                                                                                                                                                
    def defineModSZ(self):
        min = float(self.modScaleZminLedit.text())
        max = float(self.modScaleZMaxLedit.text())


        self.defineModByAttr("scaleZ",min,max)                                                                     
                                                                                                                                                                                                                                                                                                                                       
    def defineModSAll(self):
        min = float(self.modScaleAllminLedit.text())
        max = float(self.modScaleAllMaxLedit.text())


        self.defineModScaleAll(min,max) 
        
    def defineModAlpha(self):
        min = float(self.modAlphaMinLedit.text())
        max = float(self.modAlphaMaxLedit.text())

        self.defineModByAttr("slot_alpha",min,max)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    def defineModByAttr(self,attr,minValue,maxValue):
        frameList = self.modFrameIndxLEdt.text().split(",")
        objList = cmds.ls(sl=True,l=True)
        for obj in objList:  
            keyframeList =  cmds.keyframe( obj,at=attr, query=True) 
            if attr in ['translateX','translateY','translateZ']:
                offsetValue =  random.randint(minValue,maxValue)
            else:
                offsetValue =  random.uniform(minValue,maxValue)
            #print "keyframeList",obj,attr,keyframeList
            
          #  print offsetValue
            if frameList[0] == "all":
                for frame in keyframeList:
                    frameValue = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]
                    #print attr,frame,frameValue
                   
                        
                    if attr == "scaleX":
                        changeValue = offsetValue * frameValue
                    elif attr == "scaleY":
                        changeValue = offsetValue * frameValue
                    elif attr == "scaleZ":
                        changeValue = offsetValue * frameValue
                        
                    elif attr == "translateX":
                        changeValue = offsetValue + frameValue                            
                    elif attr == "translateY":
                        changeValue = offsetValue + frameValue                            
                    elif attr == "translateZ":
                        changeValue = offsetValue + frameValue    
                        
                    elif attr == "rotateX":
                        changeValue = offsetValue + frameValue                                                        
                                                                                                
                    elif attr == "rotateY":
                        changeValue = offsetValue + frameValue  
                                                                              
                    elif attr == "rotateZ":
                        changeValue = offsetValue + frameValue   
                        
                    elif attr == "slot_alpha":
                        changeValue = offsetValue + frameValue                                                                                       
                                                                                                                                  
                    elif attr == "slot_red":
                        changeValue = offsetValue + frameValue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                  
                    elif attr == "slot_green":
                        changeValue = offsetValue + frameValue
                                                                                                                                                              
                    elif attr == "slot_blue":
                        changeValue = offsetValue + frameValue

                            
                    if self.modOffsetBtn.isChecked() == True:
                      #  print changeValue
                        cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=changeValue )
                    else:
                        cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=offsetValue )


                        
                        
                
            else:
                for indexNum in frameList:
                    frame = keyframeList[int(indexNum)]
                    
                    frameValue = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]
                   # print attr,frame,startFrameValue checkBox_square
                    if attr == "scaleX":
                        changeValue = offsetValue * frameValue
                    elif attr == "scaleY":
                        changeValue = offsetValue * frameValue
                    elif attr == "scaleZ":
                        changeValue = offsetValue * frameValue
                        
                    elif attr == "translateX":
                        changeValue = offsetValue + frameValue                            
                    elif attr == "translateY":
                        changeValue = offsetValue + frameValue                            
                    elif attr == "translateZ":
                        changeValue = offsetValue + frameValue    
                        
                    elif attr == "rotateX":
                        changeValue = offsetValue + frameValue                                                        
                                                                                                
                    elif attr == "rotateY":
                        changeValue = offsetValue + frameValue  
                                                                              
                    elif attr == "rotateZ":
                        changeValue = offsetValue + frameValue   
                        
                    elif attr == "slot_alpha":
                        changeValue = offsetValue + frameValue                                                                                       
                                                                                                                                  
                    elif attr == "slot_red":
                        changeValue = offsetValue + frameValue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                  
                    elif attr == "slot_green":
                        changeValue = offsetValue + frameValue
                                                                                                                                                              
                    elif attr == "slot_blue":
                        changeValue = offsetValue + frameValue

                    if self.modOffsetBtn.isChecked() == True:
                      #  print changeValue
                        cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=changeValue )
                    else:
                        cmds.setKeyframe(obj, t=[frame,frame], at=attr,v=offsetValue )


    def defineModScaleAll(self,minValue,maxValue):
        frameList = self.modFrameIndxLEdt.text().split(",")
        objList = cmds.ls(sl=True,l=True)
        for obj in objList:  
            keyframeList =  cmds.keyframe( obj,at='scaleX', query=True) 

            offsetValue =  random.uniform(minValue,maxValue)
            #print "keyframeList",obj,attr,keyframeList
            
          #  print offsetValue
            if frameList[0] == "all":
                for frame in keyframeList:
                    frameValue = cmds.keyframe(obj,at='scaleX',t=(frame,frame),q=True,eval=True)[0]
                    #print attr,frame,frameValue

                    changeValue = offsetValue * frameValue

                            
                    if self.modOffsetBtn.isChecked() == True:
                      #  print changeValue
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleX',v=changeValue )
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleY',v=changeValue )

                    else:
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleX',v=offsetValue )
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleY',v=offsetValue )


                        
                        
                
            else:
                for indexNum in frameList:
                    frame = keyframeList[int(indexNum)]
                    
                    frameValue = cmds.keyframe(obj,at='scaleX',t=(frame,frame),q=True,eval=True)[0]
                   # print attr,frame,startFrameValue checkBox_square
       
                    changeValue = offsetValue * frameValue


                    if self.modOffsetBtn.isChecked() == True:
                      #  print changeValue
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleX',v=changeValue )
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleY',v=changeValue )

                    else:
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleX',v=offsetValue )
                        cmds.setKeyframe(obj, t=[frame,frame], at='scaleY',v=offsetValue )
            
                  
                              
    def changeRelaceMode(self):   
        if self.modReplaceModBtn.isChecked() == True:
            self.modOffsetBtn.setChecked(False)
            
        else:
            self.modReplaceModBtn.setChecked(False)
            self.modOffsetBtn.setChecked(True)
            
    def changeOffsetMode(self):          
        if self.modOffsetBtn.isChecked() == True:
            self.modReplaceModBtn.setChecked(False)
        else:
            self.modOffsetBtn.setChecked(False)
            self.modReplaceModBtn.setChecked(True)  
            
    def setFrameFilletToAll(self):
        
        self.modFrameIndxLEdt.setText("all")
        
    def setFrameFilletToFirst(self):
        
        self.modFrameIndxLEdt.setText("0")
                
    def setFrameFilletToLast(self):
        
        self.modFrameIndxLEdt.setText("-1")
                
    def getObjList(self):
        
        objList = cmds.ls(sl=True)
        
        return objList  
        
        
        
        

    def scaleFrames(self):
        print "scaleFrames"
        originalIn = int(float(self.scaleTimeOriginIN.text()))
        originalOut = int(float(self.scaleTimeOriginOut.text()))
        newIn = int(float(self.scaleTimeNewIn.text()))
        newOut = int(float(self.scaleTimeNewOut.text()))
        objList = self.getObjList()
    #    print originalIn,originalOut,newIn,newOut
        if originalOut - originalIn > 0 and newOut-newIn >0:
            originalAmount = originalOut -originalIn
            newAmount = newOut-newIn
            for obj in objList:

              #  tempKeyFrameList = cmds.(obj,q=True)            
                cmds.scaleKey( obj, time=(originalIn,originalOut), newStartTime=newIn, newEndTime= newOut)


        else:
            print "not illegal frame pls check again"
            

           
        
        
        
        
        
        
        

    def loopFrames(self):
        cmds.currentTime(0,e=True)
        offsetStartFrame = int(float(self.loopTimeIn.text()))
        offsetEndFrame = int(float(self.loopTimeOut.text()))
        loopSpace = int(float(self.loopSpaceFrame.text()))
        loopTimes = int(float(self.loopTimes.text()))

        #divideNextFrame  = divideFrame +1 divideFrame

        keyFrameLength = offsetEndFrame-offsetStartFrame +1.0
        print "offsetKeyFrames"
        
        keyAbleAttList=["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ","slot_alpha","slot_red","slot_green","slot_blue"] #["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]
        objList = self.getObjList()
        
        if loopTimes == 1:
            offsetValueGet = int((offsetEndFrame - offsetStartFrame) -1)
        elif loopTimes > 1:
            for obj in objList:
                tempAllObjKeyFrames = cmds.keyframe(obj,q=True)
                allObjKeyFrames = []
                for i in tempAllObjKeyFrames:
                    if i in allObjKeyFrames:
                        pass
                    else:
                        allObjKeyFrames.append(i)
                allObjKeyFrames = sorted(allObjKeyFrames)   
                firstKeyFrame = allObjKeyFrames[0]
                lastKeyFrame = allObjKeyFrames[-1]
                pastReturnZeroFrame = lastKeyFrame +0.01
             #   print 'firstKeyFrame',firstKeyFrame,lastKeyFrame,pastReturnZeroFrame
                cmds.copyKey( obj, time=(firstKeyFrame,firstKeyFrame))  ### copy the firstkey to frameEnd to be return initial state
                cmds.pasteKey( obj, time=(pastReturnZeroFrame,pastReturnZeroFrame))
                cmds.copyKey( obj, time=(firstKeyFrame,pastReturnZeroFrame))  
                for num in range(1,loopTimes):
                    beginFrame = offsetStartFrame + (keyFrameLength + loopSpace)* num
                    cmds.pasteKey( obj, time=(beginFrame,))
                    
                newTempAllObjKeyFrames = cmds.keyframe(obj,q=True)    
                newAllObjKeyFrames = []    
                for i in newTempAllObjKeyFrames:
                    if i in newAllObjKeyFrames:
                        pass
                    else:
                        newAllObjKeyFrames.append(i) 
                offsetStartFrame = newAllObjKeyFrames[0]
                offsetEndFrame = newAllObjKeyFrames[-1] 
                offsetValueGet  = int((offsetEndFrame - offsetStartFrame) -1)  
        
        for obj in objList:
           # if self.checkBox_offsetRandom.isChecked() == False:
           #     offsetValue = int(float(self.loopOffsetRange.text()))
           # else:
              #  offsetValue = random.random(0,int(float(self.loopOffsetRange.text())))
            offsetValue = random.randint(1,offsetValueGet)

            divideFrame = offsetStartFrame + offsetValue 
            divideStepFrame = divideFrame+0.01-1
           # print "obj, offsetValue",obj,offsetValue,divideFrame,divideStepFrame

            
          #  print obj offsetValue cmds.findKeyframe("bone_0021",at ="translateZ" )
           # if 
            for attr in keyAbleAttList :
              #  print 'attr',attr

              #  print attr,offsetStartFrame,offsetEndFrame,startFrameValue,endFrameValue
                
                try:
                    keyCount =  len(cmds.keyframe(obj,at=attr,q=True)) 
                except:
                    keyCount = 0 
                    
               # print "attr",attr,"keyCount",keyCount
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
                       # print "clear key"
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
        
                       
    def alignKeys(self):
        print "alignKeys"
        objList = self.getObjList()
        alignFrame = int(float(self.alignToFrameLEdit.text()))
        print 'alignFrame',alignFrame
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
                    
            if alignFrame <= 0 :
                self.errorMsgLEdit.setText('the frame number should be large than 1')

            elif alignFrame <= keyFrameList[0] and alignFrame >= 1:  #align keyframe when align frame <= first keyframe
                for i in range(0,len(keyFrameList)):
                    originalFrame = keyFrameList[i]
                    newKeyFrame = keyFrameList[i] - (keyFrameList[0]-alignFrame)

                    try:
                        cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))
                    except:
                        pass
            elif alignFrame  >= keyFrameList[0]:
                offsetFrame =alignFrame -keyFrameList[0] #align keyframe when align frame > first keyframe
                print keyFrameList
                resveredKeyFrameList = list(reversed(keyFrameList))
                for i in range(0,len(keyFrameList)):
                    originalFrame =  resveredKeyFrameList[i]
                    
                    newKeyFrame = originalFrame +offsetFrame

                    cmds.keyframe(obj,time=(originalFrame,originalFrame),timeChange=(newKeyFrame))        
                    
                    
                    
                    
    def trimBeforeFrame(self):
        print "trimBeforeFrame"
        objList = self.getObjList()
        keepRange = int(float(self.trimBeforeFrameLEdit.text()))
        print objList,keepRange
       # cutStartFrame = float(cutFrames.split(",")[0])
        #cutEndFrame = float(cutFrames.split(",")[1]) trimAfterFrame
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
                
#cmds.cutKey( 'bone_star_A02_18', time=(0,3),option="keys" )                            
                       
    def trimAfterFrame(self):
        print "trimAfterFrame"
        objList = self.getObjList()
        keepRange = int(float(self.trimAfterFrameLEdit.text()))
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
 
    def trimBetweenFrame(self):
        print "trimBetweenFrame"
        startFrame = int(float(self.trimBetweenFrameStartLEdit.text()))
        endFrame =  int(float(self.trimBetweenFrameEndLEdit.text()))
        objList = self.getObjList()
        for obj in objList:

            tempKeyFrameList = cmds.keyframe(obj,q=True)
            lastFrame =  math.ceil(tempKeyFrameList[-1])
            firstFrame = math.floor(tempKeyFrameList[0])
            #print firstFrame,lastFrame
            cmds.cutKey( obj, time=(firstFrame,startFrame),option="keys" )
            cmds.cutKey( obj, time=(endFrame,lastFrame),option="keys" )        
                
    def slotAmountEditChange(self):                       
        inputEditValue = self.amountSliderNumLEdit.text()
        self.amountSlotSlider.setValue(int(inputEditValue))                                                                        
                        
                                                  
        ##### change slots amount
    def slotAmountSliderChange(self):
        inputSliderValue = self.amountSlotSlider.value()        
        self.amountSliderNumLEdit.setText(str(inputSliderValue))                                                   
                                                                                          
                                                                                                    
                                                                                                              
                                                                                                                        
                                                                                                                                  
                                                                                                                                                                                                                           
        ##### btn in dockWidgetImages
    
    def openSelectedFolder(self):
        print "openSelectedFolder"
        if self.selectImageFolderBtn.isChecked() == True or self.selectImageFromDiskBTN.isChecked() ==True:
            dir = self.spineItemTree.currentItem().text(1)
        else:
            self.errorMsgLEdit.setText('pls select image folder')
        currentProjWin =''   
        for cha in dir:
            if cha =="/":
                currentProjWin += '\\'
            else:    
                currentProjWin += cha 
        openCmd = "explorer "+'%s'%currentProjWin
        subprocess.call(openCmd)
    


    def setToSpineJobTree(self):
        print "setToSpineJobTree"

        self.selectImageFolderBtn.setChecked(False)
        self.selectImageFromDiskBTN.setChecked(False)
        self.selectSpineJobBtn.setChecked(True)
       # self.imageListTable.clear()
        
        self.initialSpineItemTree()
        self.defineAllSlotInSpine()

            
        
    def setImageSourceToDatabase(self):
        print "setImageSourceToDatabase"
      
        self.selectImageFolderBtn.setChecked(True)
        self.selectImageFromDiskBTN.setChecked(False)
        self.selectSpineJobBtn.setChecked(False)
       # self.imageListTable.clear()
        imageDir = "//mcd-3d/data3d/spine_imageSources/effects"
        self.getImageSourcesDir(imageDir)
        
        
    def setToDisk(self):
        print "setToDisk"
       
                        
        self.selectImageFolderBtn.setChecked(False)
        self.selectImageFromDiskBTN.setChecked(True)
        self.selectSpineJobBtn.setChecked(False)
        #self.imageListTable.clear()

        try:
            imageDir = cmds.fileDialog2(dialogStyle=1,fm=2)[0]
        except:
            self.selectImageFolderBtn.setChecked(True)
            self.selectImageFromDiskBTN.setChecked(False)
            imageDir = "//mcd-3d/data3d/spine_imageSources/effects"
            self.getImageSourcesDir(imageDir)
       # print imageDir
        self.getImageSourcesDir(imageDir)
        
        

    def getImageSourcesDir(self,imageDir):
        print "getImageSourcesDir"

        imagesRoot = imageDir
        #imagesRoot = "c:/temp/testimage"
        searchDepth = 7
        self.spineItemTree.clear()
     #   print self.findChildDir(imagesRoot)
       # print os.listdir(imagesRoot)
        #searchLoopCount = 0
        countI = 0
        exceptList =['.mayaSwatches']
        for i in self.findChildDir(imagesRoot):
            #print i        
            ## define topLevelItem Dir
           # print os.listdir(i)
            #print 'path',os.listdir(imagesRoot)
            countTopLevelItems = str(len(os.listdir(i)))
            topLevelDirName = i.split(imagesRoot)[1].split('/')[1] + '   ('+ countTopLevelItems +')'
             
            print 'topLevelDirName',topLevelDirName
            if topLevelDirName in exceptList:
                pass
            else:
              #  print countI
                topLevelItem = QtWidgets.QTreeWidgetItem(self.spineItemTree)
                self.spineItemTree.topLevelItem(countI).setText(0, QtWidgets.QApplication.translate("MainWindow",topLevelDirName.encode('utf-8'), None, -1))
                self.spineItemTree.topLevelItem(countI).setText(1, QtWidgets.QApplication.translate("MainWindow",i.encode('utf-8'), None, -1))

                topLevelItem.setForeground(0,QtGui.QBrush(QtGui.QColor(250,250, 150, 255)))
                countJ = 0
                for j in self.findChildDir(i):
                #    print j 
                    countSecLevelItems = str(len(os.listdir(j)))
                    secLevelItem = QtWidgets.QTreeWidgetItem(topLevelItem)
                    secLevelDirName = j.split(i)[1].split('/')[1] + '   ('+ countSecLevelItems +')'

                    self.spineItemTree.topLevelItem(countI).child(countJ).setText(0, QtWidgets.QApplication.translate("MainWindow",secLevelDirName.encode('utf-8'), None, -1))
                    self.spineItemTree.topLevelItem(countI).child(countJ).setText(1, QtWidgets.QApplication.translate("MainWindow",j.encode('utf-8'), None, -1))

                    secLevelItem.setForeground(0,QtGui.QBrush(QtGui.QColor(150,250, 150, 255)))

                    countK = 0
                    for k in self.findChildDir(j):
                        countThirdLevelItems = str(len(os.listdir(k)))
                        thirdLevelItem = QtWidgets.QTreeWidgetItem(secLevelItem)
                        thirdLeveItemName = k.split(j)[1].split('/')[1] + '   ('+ countThirdLevelItems +')'
                        self.spineItemTree.topLevelItem(countI).child(countJ).child(countK).setText(0, QtWidgets.QApplication.translate("MainWindow",thirdLeveItemName.encode('utf-8'), None, -1))
                        self.spineItemTree.topLevelItem(countI).child(countJ).child(countK).setText(1, QtWidgets.QApplication.translate("MainWindow",k.encode('utf-8'), None, -1))
                        thirdLevelItem.setForeground(0,QtGui.QBrush(QtGui.QColor(100,200, 255, 255)))
                        
                        countL = 0
                        for l in self.findChildDir(k):
                            countFourLevelItems = str(len(os.listdir(l)))

                            forthLevelItem = QtWidgets.QTreeWidgetItem(thirdLevelItem)
                            forthLevelItemName = l.split(k)[1].split('/')[1]+ '   ('+ countFourLevelItems +')'
                            self.spineItemTree.topLevelItem(countI).child(countJ).child(countK).child(countL).setText(0, QtWidgets.QApplication.translate("MainWindow",forthLevelItemName.encode('utf-8'), None, -1))
                            self.spineItemTree.topLevelItem(countI).child(countJ).child(countK).child(countL).setText(1, QtWidgets.QApplication.translate("MainWindow",l.encode('utf-8'), None, -1))
                            forthLevelItem.setForeground(0,QtGui.QBrush(QtGui.QColor(150,150, 200, 255)))
                            
                            
                            countL =  countL +1
                        countK = countK + 1
                    countJ = countJ +1                
                countI = countI +1
                    


    def findChildDir(self,parentDir):
        print "findChildDir"
        childDirList = []
        childFileNameList = os.listdir(parentDir)
        for i in childFileNameList:
            fileName = parentDir +'/' +i
            ##print fileName
            if os.path.isdir(fileName) == True:
                childDirList.append(fileName)
                
        return childDirList
    
    
    def defineSpineWorkSpace(self):
        print "defineSpineWorkSpace"
        basicFilter = "*.json"
        spineWorkSpace = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=1,fm=2)[0]
        self.spineWorkSpaceLEdit.setText(spineWorkSpace)
        print spineWorkSpace
        
        spineImagesFolder = spineWorkSpace +'/images'
        exportFolder = spineWorkSpace +'/export'
        try :
            os.mkdir(spineImagesFolder)
        except:
            pass
        try:
            os.mkdir(exportFolder)
        except:
            pass
        
        self.spineImagesSpaceLEdit.setText(spineImagesFolder)
        self.spineExportSpaceLEdit.setText(exportFolder)
        
        
        
        
    
    
    def defineExportFileName(self):
        print "defineExportFileName"
        
        basicFilter = "*.json"
        exportFileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2)[0]
        self.selectExportFileBTnLEdit.setText(exportFileName)
        print exportFileName
        
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    def initialSpineItemTree(self):
        print "defineSpineImagesTable"
        allCharacterSetList = []
        allMeshSlotList = []
        allSkinNameList = []
        allDeformerList = []
        self.spineItemTree.clear()
        
        if len(cmds.ls("spine_RootSkeleton")) == 0:
            self.errorMsgLEdit.setText('spine_Root is not exist,pls define it')
        else:
            if cmds.getAttr('spine_RootSkeleton.spine_tag') == "spine_RootSkeleton":
                newSpineRootItem = QtWidgets.QTreeWidgetItem(self.spineItemTree)
                self.spineItemTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "spine_RootSkeleton", None, -1))
                
                allTransformInRoot = cmds.listRelatives("spine_RootSkeleton",c=True,p=False,type="transform")
                newSpineRootItem.setExpanded(True)

                for i in range(0,len(allTransformInRoot)):
                    characterSet = allTransformInRoot[i]
                    allIKIncharacterSet = cmds.listRelatives(characterSet,c=True,p=False,type="ikHandle",ad=True) ### get IK in character set
                    #print 'allIKIncharacterSet',allIKIncharacterSet
                    if cmds.getAttr('%s.spine_tag'%characterSet) == "spine_characterSet":
                        allCharacterSetList.append(characterSet)
                        
                        #### define Character Set in Tree
                        newCharSetItem = QtWidgets.QTreeWidgetItem(newSpineRootItem)
                        charSetName = str(characterSet)
                        self.spineItemTree.topLevelItem(0).child(i).setText(0, QtWidgets.QApplication.translate("MainWindow",charSetName, None, -1))
                        newCharSetItem.setForeground(0,QtGui.QBrush(QtGui.QColor(255,133, 133, 255)))

                        allTransformInCharSet = cmds.listRelatives(characterSet,c=True,p=False,type="transform")
                      #  print 'allTransformInCharSet',allTransformInCharSet
                        itemInCharSetCount = 0
                        newCharSetItem.setExpanded(True)
                        try:
                            allMeshInCharacterSetList = []
                            for j in allTransformInCharSet:
                               # print 'jjjjj',j
                        
                                if cmds.getAttr('%s.spine_tag'%j) == "spine_ctrl":
                                    newCtrlItem = QtWidgets.QTreeWidgetItem(newCharSetItem)
                                    ctrlName = str(j)
                                    self.spineItemTree.topLevelItem(0).child(i).child(itemInCharSetCount).setText(0, QtWidgets.QApplication.translate("MainWindow",ctrlName, None, -1))
                                    itemInCharSetCount = itemInCharSetCount +1
                                    newCtrlItem.setForeground(0,QtGui.QBrush(QtGui.QColor(255,255, 100, 255)))
                                elif cmds.getAttr('%s.spine_tag'%j) == "spine_slot":
                                    newSlotItem = QtWidgets.QTreeWidgetItem(newCharSetItem)
                                    slotName = str(j)
                                    self.spineItemTree.topLevelItem(0).child(i).child(itemInCharSetCount).setText(0, QtWidgets.QApplication.translate("MainWindow",slotName, None, -1))

                                    newSlotItem.setForeground(0,QtGui.QBrush(QtGui.QColor(200,255, 200, 255)))

                                    newSlotItem.setExpanded(True)
                                    meshInSlotItemCount = 0
                                    for k in cmds.listRelatives(j,c=True,p=False):
                                        try:
                                            if cmds.nodeType(k) =='mesh' and cmds.getAttr('%s.spine_skinType'%k) =='mesh':
                                                newMeshItem = QtWidgets.QTreeWidgetItem(newSlotItem)
                                                meshName = str(k)
                                                self.spineItemTree.topLevelItem(0).child(i).child(itemInCharSetCount).child(meshInSlotItemCount).setText(0, QtWidgets.QApplication.translate("MainWindow",meshName, None, -1))
                                                newMeshItem.setForeground(0,QtGui.QBrush(QtGui.QColor(150,150, 255, 255)))
                                                
                                                attachmentName = str(cmds.getAttr('%s.spine_attachmentName'%k))
                                                newAttachmentItem = QtWidgets.QTreeWidgetItem(newMeshItem)
                                                self.spineItemTree.topLevelItem(0).child(i).child(itemInCharSetCount).child(meshInSlotItemCount).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow",attachmentName, None, -1))
                                                newAttachmentItem.setForeground(0,QtGui.QBrush(QtGui.QColor(150,200, 255, 255)))

                                                
                                                allMeshSlotList.append(j)
                                                allSkinNameList.append(k)
                                                allMeshInCharacterSetList.append(k)
                                                newMeshItem.setExpanded(True)
                                                meshInSlotItemCount = meshInSlotItemCount+1
                                        except:
                                            pass
                                            
                                    itemInCharSetCount = itemInCharSetCount +1



                                        #print 'kkkk',k,cmds.getAttr('%s.spine_skinType'%str(k))
                                       # if cmds.nodeType(k) =='mesh' and cmds.getAttr('%s.spine_skinType'%k) =='mesh':
                                           # allMeshSlotList.append(j)
                                           # allSkinNameList.append(k)
                               # print 'jjjjjjj',j
                                        #allMeshSlotList.append(i)
                                
                        except:
                            pass
                
                
                
                        #### define deformerin tree
                        allDeformerInCharacterSetList = []
                        for mesh in allMeshInCharacterSetList:
                          #  print 'mesh',mesh
                            

                            allDeformersList = cmds.listHistory(mesh)
                            for d in allDeformersList:
                               # print 'dddddd',d,cmds.nodeType(d)
                                dt = cmds.nodeType(d)
                                if dt == "joint":
                                    allDeformerInCharacterSetList.append(d)
                                elif dt == "clusterHandle":
                                    clusterHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(clusterHandle[0])
                                elif dt == "softModHandle":
                                    softModHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(softModHandle[0])
                                elif dt == "deformBend":
                                    deformBendHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(deformBendHandle[0])                                   
                                elif dt == "deformFlare":
                                    deformFlareHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(deformFlareHandle[0])                                    
                                elif dt == "deformSine":
                                    deformSineHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(deformSineHandle[0])                                    
                                elif dt == "deformSquash":
                                    deformSquashHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(deformSquashHandle[0])                                    
                                elif dt == "deformTwist":
                                    deformTwistHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(deformTwistHandle[0])                                    
                                elif dt == "deformWave":
                                    deformWaveHandle = cmds.listRelatives(d,p=True)
                                    allDeformerInCharacterSetList.append(deformWaveHandle[0])         
                                    
                                                                                        
                           # print 'allDeformerInCharacterSetList',allDeformerInCharacterSetList
                        
                        try:
                            if len(allDeformerInCharacterSetList) > 0:
                                childCountInCharacterSetA =  self.spineItemTree.topLevelItem(0).child(i).childCount()
                                newDeformerGrpItem = QtWidgets.QTreeWidgetItem(newCharSetItem)
                                self.spineItemTree.topLevelItem(0).child(i).child(childCountInCharacterSetA).setText(0, QtWidgets.QApplication.translate("MainWindow",'Deformer', None, -1))
                                newDeformerGrpItem.setForeground(0,QtGui.QBrush(QtGui.QColor(250,250, 100, 255)))
                                deformerCount = 0
                                for d in allDeformerInCharacterSetList:
                                #    print "ddddddddddd",d,cmds.nodeType(d)
                                    newDeformerItem = QtWidgets.QTreeWidgetItem(newDeformerGrpItem)
                                    deformerName  = str(d)
                                    self.spineItemTree.topLevelItem(0).child(i).child(childCountInCharacterSetA).child(deformerCount).setText(0, QtWidgets.QApplication.translate("MainWindow",deformerName, None, -1))
                                    newDeformerItem.setForeground(0,QtGui.QBrush(QtGui.QColor(250,250, 200, 255)))

                                    deformerCount = deformerCount + 1
                            
                            ### define allIK
                          #  print 'allIKIncharacterSet',allIKIncharacterSet,type(allIKIncharacterSet)
                        except:
                            pass
                        
                        print 'allIKIncharacterSet',allIKIncharacterSet,type(allIKIncharacterSet)
                        try:
                            if len(allIKIncharacterSet) > 0:
                                childCountInCharacterSetB =  self.spineItemTree.topLevelItem(0).child(i).childCount()
                                newIKGrpItem = QtWidgets.QTreeWidgetItem(newCharSetItem)
                                self.spineItemTree.topLevelItem(0).child(i).child(childCountInCharacterSetB).setText(0, QtWidgets.QApplication.translate("MainWindow",'IK', None, -1))
                                newIKGrpItem.setForeground(0,QtGui.QBrush(QtGui.QColor(250,250, 100, 255)))
                                ikCount = 0
                                newIKGrpItem.setExpanded(True)
                                for ik in allIKIncharacterSet:
                                  #  print ik
                                    newIKItem = QtWidgets.QTreeWidgetItem(newIKGrpItem)
                                    ikName  = str(ik)
                                    self.spineItemTree.topLevelItem(0).child(i).child(childCountInCharacterSetB).child(ikCount).setText(0, QtWidgets.QApplication.translate("MainWindow",ikName, None, -1))
                                    newIKItem.setForeground(0,QtGui.QBrush(QtGui.QColor(250,250, 200, 255)))

                                    ikCount = ikCount + 1
                        except:
                            pass
                           #   newIKItem.setForeground(0,QtGui.QBrush(QtGui.QColor(255,133, 133, 255)))
                
                            
                ## define image in image space tree
                newImageRootItem = QtWidgets.QTreeWidgetItem(self.spineItemTree)
                self.spineItemTree.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "images", None, -1))
                newImageRootItem.setForeground(0,QtGui.QBrush(QtGui.QColor(100,250, 200, 255)))
                #allTransformInRoot = cmds.listRelatives("spine_RootSkeleton",c=True,p=False,type="transform")
                newImageRootItem.setExpanded(True)   
                
                imageFolder = self.spineImagesSpaceLEdit.text()
                print "imageFolder" ,imageFolder
                if len(imageFolder) == 0:
                    self.errorMsgLEdit.setText('no spine image folder')
                else:
                    allFilesInSpineImageFolder = os.listdir(imageFolder)
                   # print 'allFilesInSpineImageFolder',allFilesInSpineImageFolder
                    imageCount = 0
                    for file in allFilesInSpineImageFolder:
                        fullFileName = (self.spineWorkSpaceLEdit.text()).encode('utf-8')+'/images/'+file
                       # print fullFileName
                        
                        if os.path.isdir(fullFileName) == True:
                            pass
                        else:
                           # print file.split('.')[-1]
                            if file.split('.')[-1] in self.imagesFilter:
                             #   print 'fullFileName',fullFileName
                                newImageFileItem = QtWidgets.QTreeWidgetItem(newImageRootItem)
                                self.spineItemTree.topLevelItem(1).child(imageCount).setText(0, QtWidgets.QApplication.translate("MainWindow", file.encode('utf-8'), None, -1))
                                self.spineItemTree.topLevelItem(1).child(imageCount).setText(1, QtWidgets.QApplication.translate("MainWindow", file.encode('utf-8'), None, -1))
                              #  self.spineItemTree.itemClicked.connect(self.clickSpineImages)
                                #clickSpineImages
                                imageCount = imageCount +1
                    self.defineSpineImagesTable(imageFolder)
                   # print 'defineSpineImagesTable'
                    #self.getImageSourcesDir(self,imageDir):                
                                                                               
                                            
            else:
                self.errorMsgLEdit.setText('spine_RootSkeleton spine_tag error')
                
       # self.spineItemTree.expandAll()

    
       # print 'allCharacterSetList',allCharacterSetList
       # print 'allMeshSlotList',allMeshSlotList
        #print 'allSkinNameList',allSkinNameList
        
    def defineAllSlotInSpine(self):
        print "defineAllSlotInSpine" 
        
        existedCharacterSetsInSpineRoot  = self.spineItemTree.topLevelItem(0).childCount()
        #print existedCharacterSetsInSpineRoot
        slotsTopGrpItem = QtWidgets.QTreeWidgetItem(self.spineItemTree.topLevelItem(0)) 
        self.spineItemTree.topLevelItem(0).child(existedCharacterSetsInSpineRoot).setText(0, QtWidgets.QApplication.translate("MainWindow","slots/bones", None, -1))
        slotsTopGrpItem.setForeground(0,QtGui.QBrush(QtGui.QColor(100,255, 100, 255)))
        slotsTopGrpItem.setExpanded(True)   
        allJoints = cmds.listRelatives('spine_RootSkeleton',c=True,f=True,ad=True)
        allSpineBoneList = []
        for i in allJoints:
            try:
                if cmds.getAttr('%s.spine_tag'%i) == 'spine_bone' or cmds.getAttr('%s.spine_tag'%i) == 'spine_slot':
                    allSpineBoneList.append(i)
                   # try:
                   #     if if cmds.getAttr('%s.spine_tag'%i) == 'spine_bone'
            except:
                pass
                
        childCountInThirdLV = self.spineItemTree.topLevelItem(0).child(existedCharacterSetsInSpineRoot).childCount()
        thridLVItems = self.defineslotTreeLevel(slotsTopGrpItem,allSpineBoneList,2)
        print thridLVItems
        for i in thridLVItems:

            allItemListHave3rdLevel =  filter(lambda x: len(x.split('|')) >3 ,allSpineBoneList)
            addItemList3rd = filter(lambda x: x.split('|')[2] ==  i.text(0) ,allItemListHave3rdLevel)
            
            fourthLVItems = self.defineslotTreeLevel(i,addItemList3rd,3)
            
            for j in fourthLVItems:
                allItemListHave4thLevel =  filter(lambda x: len(x.split('|')) >4 ,allSpineBoneList)
                addItemList4th = filter(lambda x: x.split('|')[3] ==  j.text(0) ,allItemListHave4thLevel)
                fiveLVItems = self.defineslotTreeLevel(j,addItemList4th,4)
                
                for k in fiveLVItems:
                    allItemListHave5thLevel =  filter(lambda x: len(x.split('|')) >5 ,allSpineBoneList)
                    addItemList5th = filter(lambda x: x.split('|')[4] ==  k.text(0) ,allItemListHave5thLevel)
                    sixLVItems = self.defineslotTreeLevel(k,addItemList5th,5)
                    
                    
                    for l in sixLVItems:
                        allItemListHave6thLevel =  filter(lambda x: len(x.split('|')) >6 ,allSpineBoneList)
                        addItemList6th = filter(lambda x: x.split('|')[5] ==  l.text(0) ,allItemListHave6thLevel)
                        sevenLVItems = self.defineslotTreeLevel(l,addItemList6th,6)
                        
                        for m in sevenLVItems:
                            allItemListHave7thLevel =  filter(lambda x: len(x.split('|')) >7 ,allSpineBoneList)
                            addItemList7th = filter(lambda x: x.split('|')[6] ==  m.text(0) ,allItemListHave7thLevel)
                            eightLVItems = self.defineslotTreeLevel(m,addItemList7th,7)
                            
                            for n in eightLVItems:
                                allItemListHave8thLevel =  filter(lambda x: len(x.split('|')) >8 ,allSpineBoneList)
                                addItemList8th = filter(lambda x: x.split('|')[7] ==  n.text(0) ,allItemListHave8thLevel)
                                nineLVItems = self.defineslotTreeLevel(n,addItemList8th,8)
                                    
                                for o in nineLVItems:
                                    allItemListHave9thLevel =  filter(lambda x: len(x.split('|')) >9 ,allSpineBoneList)
                                    addItemList9th = filter(lambda x: x.split('|')[8] ==  o.text(0) ,allItemListHave9thLevel)
                                    tenLVItems = self.defineslotTreeLevel(o,addItemList9th,9)
                                            
                            
                            
                                                      
                        

    def defineslotTreeLevel(self,parentItem,itemAddList,depthLevel):
        
        
       # print 'childCount',childCount,itemAddList
        itemExisted = []
        #### check exist item in parentItem
        existItemInParent = parentItem.childCount()
        for i in range(0,existItemInParent):
            if parentItem.child(i).text(0) in itemExisted:
                pass
            else:
                itemExisted.append(parentItem.child(i).text(0))
                
        addItemList = []
        for i in itemAddList:
            try:
                if i.split('|')[depthLevel] in addItemList:
                    pass
                else:
                    addItemList.append(str(i.split('|')[depthLevel]))
            except:
                pass
          
        realAddItemList = []
        for i in addItemList:
            if i in itemExisted:
                pass
            else:
                realAddItemList.append(i)
                
        childItem = []
        for i in range(0,len(realAddItemList)):
            newItem = QtWidgets.QTreeWidgetItem() 
            itemName = addItemList[i]
           # print 'itemName',itemName
            newItem.setText(0, QtWidgets.QApplication.translate("MainWindow",itemName, None, -1))
            parentItem.addChild(newItem)
            childItem.append(newItem)    
            try:
                if cmds.getAttr('%s.spine_tag'%itemName) == 'spine_bone':
                    newItem.setForeground(0,QtGui.QBrush(QtGui.QColor(100,200,100)))
                elif cmds.getAttr('%s.spine_tag'%itemName) == 'spine_slot':
                    newItem.setForeground(0,QtGui.QBrush(QtGui.QColor(100,200,200)))

            except:
                pass
            #newItem.setForeground(0,QtGui.QBrush(QtGui.QColor(int(itemColor))))

            newItem.setExpanded(True)   

        return childItem

    def defineSpineImagesTable(self,imageDir):    
        print "defineSpineImagesTable"
        currentFolder = imageDir#.encode('utf-8')
       # print 'currentFolder',currentFolder
        try:
            files = os.listdir(currentFolder)
            images = filter(lambda x: x.split('.')[-1] in self.imagesFilter, files)

           # print 'images',images
            #self.createImageTable(images,50,currentFolder)
           # print self.imageListTable
            self.imageListTable.setRowCount(0)
            self.imageListTable.setColumnCount(0)
           # self.createImageTable(images,50,currentFolder)
            
           # self.createImageInfoTable()
            imagesCount = len(images)
           # print 'imagesCount',imagesCount
            columnCount = 5
            columnWidth = 50
            rowCount = int(math.ceil(float(len(images))/float(columnCount)))
            rowHeight = columnWidth
           # print 'imagesCount',imagesCount,rowCount

            self.imageListTable.setGeometry(QtCore.QRect(5, 60,(columnCount*columnWidth+30), 525+30))

            self.imageListTable.setObjectName("tableWidget")
            self.imageListTable.setColumnCount(columnCount)
            self.imageListTable.setRowCount(rowCount)
            self.imageListTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.imageListTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.imageListTable.horizontalHeader().setVisible(False)
            self.imageListTable.verticalHeader().setVisible(False)
            #  self.imageListTable.setColumnWidth(0, 60)
           #   self.imageListTable.setColumnWidth(1, 60)
            for i in range(0,columnCount):
                self.imageListTable.setColumnWidth(i, columnWidth)
                   
            for i in range(0,rowCount):
                self.imageListTable.setRowHeight(i, columnWidth)

                   
            for i in range (0,imagesCount):

                item = QtWidgets.QTableWidgetItem()
                itemName = images[i]
               # print 'itemName',itemName
                imageUrl =currentFolder +'/'+ itemName.encode('utf-8')
                #print 'imageUrl',imageUrl
                text = itemName.decode('utf-8').encode('utf-8')#str(itemName)
                iconFile =QtGui.QIcon(imageUrl)
                #iconFile.pixmap(QSize(22, 22))
                row = math.floor(float(i)/float(columnCount))
                column = i%columnCount
              #  print imageUrl
                self.imageListTable.setIconSize(QtCore.QSize(columnWidth,columnWidth))
    #self.icon.pixmap(QSize(22, 22)
                self.imageListTable.setItem(row,column,item)

                self.imageListTable.item(row, column).setIcon(iconFile)
                self.imageListTable.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",text, None,-1))
                #self.imageListTable.item(row, column).setData(QtCore.Qt.EditRole, )

                                                     
            self.imageListTable.itemClicked.connect(lambda x:self.imageInfo(currentFolder))
            
        except:
            pass
            
    
    def clickSpineImages(self):
        print "aaaa"
    
    
    
    def defineSpineRootSkeleton(self):
        print "defineSpineRootSkeleton"
        spineRootSkelName = "spine_RootSkeleton"
        allTransforms = cmds.ls(type="transform",dag=2)
        if spineRootSkelName in allTransforms:
            self.errorMsgLEdit.setText('spine_RootSkeleton is already Existed') 
        else: 
            spineRootSkeleton = cmds.createNode('transform',n="spine_RootSkeleton")
            cmds.addAttr(spineRootSkeleton, ln='spine_rootSkeleton', numberOfChildren=2, attributeType='compound' )
            cmds.addAttr(spineRootSkeleton, ln='spine_tag', sn='stag' , dt="string", parent='spine_rootSkeleton' ,k=True )
            cmds.addAttr(spineRootSkeleton, ln='skel_Name', sn='skelName' , dt="string", parent='spine_rootSkeleton' ,k=True )
           
            cmds.setAttr('%s.spine_tag'%spineRootSkeleton,'spine_RootSkeleton',type='string')
            cmds.setAttr('%s.skel_Name'%spineRootSkeleton,'spine_RootSkeleton',type='string')
           
            
            newSlotItem = QtWidgets.QTreeWidgetItem(self.spineItemTree)
            self.spineItemTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "spine_RootSkeleton", None, -1))
                                
            
        self.spineRootLEdit.setText("spine_RootSkeleton")
           # cmds.select(nullGrp)
           # cmds.rename(nullGrp,characterSetName)
           # realGrpName = cmds.ls(sl=True)[0]
        #print allTransforms



    def testD(self):
        print "testD"
        print cmds.ls("spine_RootSkeletona")

        #print (self.spineItemTree.topLevelItemCount()),self.spineItemTree.topLevelItem(0)


    def doAnalyzeCharacterSet(self):
        print "doAnalyzeCharacterSet"
        #QTreeWidget::QTreeWidgetItem
        treeItemA = "\
                     QTreeWidget:item {\
                     background-color:#333333;\
                     color:#777777;\
                     text-align:center;\
                     }\
                     QTreeWidgetItem {\
                     background-color:#333333;\
                     color:#FF7777;\
                     text-align:center;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-radius:10px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-radius:10px;\
                     border-style:solid;\
                     border-width:3px;\
                     border-color:#5E749C;\
                     }\
                     "
        treeItemB = "\
                     QTreeWidget:item:text {\
                     background-color:#333333;\
                     color:#FF7777;\
                     text-align:center;\
                     }\
                     "     
        characterSet = self.setCharacterSetLineEdit.text()
        if len(characterSet) == 0:
            self.errorMsgLEdit.setText('pls select One character set')
            
        else:
            if cmds.getAttr('%s.spine_tag'%characterSet) == 'spine_characterSet':
                #allTransform = cmds.listRelatives(c=True,typ='transform')
                allMeshSlotList = []
                allSkinNameList = []
                allDeformerList = []
                
                
                allTransformsList =  cmds.listRelatives(characterSet,c=True,p=False)
                print "%s is spine character set"%characterSet,allTransformsList

                slotCount = 0
                for i in allTransformsList:
                    meshCount = 0

                    for j in cmds.listRelatives(i,c=True,p=False):
                        
                        try:
                            if cmds.nodeType(j) =='mesh' and cmds.getAttr('%s.spine_skinType'%j) =='mesh':
                               # print 'jjjjjjj',j
                                allMeshSlotList.append(i)
                                slotName = str(i)
                                
                                ### add slotName to tree
                                newSlotItem = QtWidgets.QTreeWidgetItem(self.spineItemTree)
                                self.spineItemTree.topLevelItem(slotCount).setText(0, QtWidgets.QApplication.translate("MainWindow", slotName, None, -1))
                                
                                
                                ### add meshName to tree
                                meshName = str(j)
                                newMeshItem = QtWidgets.QTreeWidgetItem(newSlotItem)
                                self.spineItemTree.topLevelItem(slotCount).child(meshCount).setText(0, QtWidgets.QApplication.translate("MainWindow",meshName, None, -1))
                                newMeshItem.setForeground(0,QtGui.QBrush(QtGui.QColor(255,255, 100, 255)))
                               # self.spineItemTree.topLevelItem(slotCount).child(meshCount).setText(0).setStyleSheet(treeItemB)
                                  
                                ### add attachmentName to tree
                                attachmentName = str(cmds.getAttr('%s.spine_attachmentName'%meshName))
                                newAttachmentItem = QtWidgets.QTreeWidgetItem(newMeshItem) 
                                self.spineItemTree.topLevelItem(slotCount).child(meshCount).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow",attachmentName, None, -1))
                                newAttachmentItem.setForeground(0,QtGui.QBrush(QtGui.QColor(100,255, 255, 255)))
                                
                                
                                
                                slotCount = slotCount +1
                                meshCount = meshCount +1
                                allSkinNameList.append(j)
                        except:
                            pass
                print allMeshSlotList
                print allSkinNameList
       # newSlotItem = QtWidgets.QTreeWidgetItem(self.spineItemTree)
       # self.spineItemTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a", None, -1))

        #self.spineItemTree
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
       # item_1 = QtWidgets.QTreeWidgetItem(item_0)
       # item_2 = QtWidgets.QTreeWidgetItem(item_1)
       # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
       # item_1 = QtWidgets.QTreeWidgetItem(item_0)
      # self.treeWidget.setSortingEnabled(False)
      #  self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a", None, -1))
      #  self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a1", None, -1))
      #  self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a1_2", None, -1))
       # self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "b", None, -1))
       # self.treeWidget.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "b1", None, -1))
       # newItem = QtGui.QTreeWidgetItem(self.spineItemTree)
       # self.spineItemTree.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "a", None, -1))

    def setCharacterSetName(self):
        print "setCharacterSetName"
        currentSel = cmds.ls(sl=True,type = 'transform')
        if len(currentSel) > 1:
            self.errorMsgLEdit.setText('more than one Character Set selected')
        elif len(currentSel) == 1:
            set = currentSel[0]
            try:
                if cmds.getAttr('%s.spine_tag'%set) == "spine_characterSet":
                     self.setCharacterSetLineEdit.setText(cmds.getAttr('%s.set_name'%set))
                else:
                     self.errorMsgLEdit.setText('%s is not character set'%set)   
            except:
                self.errorMsgLEdit.setText('pls select the character set that be exported')
                self.setCharacterSetLineEdit.setText('Character Set Name')
        print currentSel
        
        
        
        
    
    def createCharacterGrp(self):
        print "createCharacterGrp"
        errMsg = "create Empty Character Grp"
        allTransform = cmds.ls(type='transform')
        characterSetName = self.characterNameLEdit.text()
        print 'allTransform',allTransform
        if len(characterSetName) == 0:
            self.errorMsgLEdit.setText('pls type in Character Set Name')
        elif characterSetName in allTransform:
            self.errorMsgLEdit.setText('%s existed'%characterSetName)
        else:
            
            nullGrp = cmds.createNode('transform')
            cmds.select(nullGrp)
            cmds.rename(nullGrp,characterSetName)
            realGrpName = cmds.ls(sl=True)[0]
            
            print 'characterSet',realGrpName
            cmds.addAttr(realGrpName, ln='spineCharacterSet', numberOfChildren=2, attributeType='compound' )
            cmds.addAttr(realGrpName, ln='spine_tag', sn='stag' , dt="string", parent='spineCharacterSet' ,k=True )
            cmds.addAttr(realGrpName, ln='set_name', sn='setname' , dt="string", parent='spineCharacterSet' ,k=True )
            
            cmds.setAttr('%s.set_name'%realGrpName,realGrpName,type='string')
           
            cmds.setAttr('%s.spine_tag'%realGrpName,'spine_characterSet',type='string')
            
            cmds.setAttr('%s.tx'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.ty'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.tz'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.sx'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.sy'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.sz'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.rx'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.ry'%realGrpName,l=True,k=False)
            cmds.setAttr('%s.rz'%realGrpName,l=True,k=False)
            cmds.parent(realGrpName,'spine_RootSkeleton')
            self.characterNameLEdit.setText('')
            self.errorMsgLEdit.setText('%s created '%characterSetName)
        #print errMsg,characterSetName
        self.initialSpineItemTree()
        
        
        
        
        
          
    def createRootCtrl(self):
        print "createRootCtrl"
        errMsg = "create Root Ctrl"
        ctrlScale = float(self.rootCtrlScaleEdit.text())
        points = [(0,2*ctrlScale,0),(6*ctrlScale,2*ctrlScale,0),(6*ctrlScale,3*ctrlScale,0),(9*ctrlScale,0,0),(6*ctrlScale,-3*ctrlScale,0),(6*ctrlScale,-2*ctrlScale,0),(0,-2*ctrlScale,0),(-6*ctrlScale,-2*ctrlScale,0),(-6*ctrlScale,-3*ctrlScale,0),(-9*ctrlScale,0,0),(-6*ctrlScale,3*ctrlScale,0),(-6*ctrlScale,2*ctrlScale,0),(0,2*ctrlScale,0)]
        allTransform =  cmds.ls(type="transform")
        currentSet = cmds.ls(sl=True,type='transform')
        rootName = self.rootNameEdit.text()
        if len(currentSet) == 0:
            self.errorMsgLEdit.setText('pls select Character Set')
        elif len(currentSet) > 1:
            self.errorMsgLEdit.setText('more than one character set be selected')
        else:
            try:
                if cmds.getAttr("%s.spine_tag"%currentSet[0]) == 'spine_characterSet':
                    
                    if len(rootName) == 0:
                        self.errorMsgLEdit.setText('pls type in root control Name')
                    else:
                        if rootName in allTransform:
                            self.errorMsgLEdit.setText('%s is existed'%rootName)
                        else:
                            
                    
                           # self.errorMsgLEdit.setText('%s is selected'%currentSet[0])
                            
                           # print rootName 
                            
                            curve = cmds.curve(d=1,p=points,n = rootName )     
                              
                            cmds.addAttr(curve, ln='spineRootCtrl', numberOfChildren=4, attributeType='compound' )
                            cmds.addAttr(curve, ln='spine_tag', sn='stag' , dt="string", parent='spineRootCtrl'  )
                            cmds.addAttr(curve, ln='timeStart', sn='timeStart' , at="float", dv=0.0,parent='spineRootCtrl' ,k=True )
                            cmds.addAttr(curve, ln='timeEnd', sn='timeEnd' , at="float", dv=120.0,parent='spineRootCtrl' ,k=True )
                            
  
                            
                            
                            cmds.addAttr(curve, ln='spine_parentCharacterSet', sn='rootCtrl' , dt="string", parent='spineRootCtrl'  )
                              
                            cmds.setAttr('%s.spine_tag'%curve,'spine_ctrl',type='string')
                            cmds.setAttr('%s.spine_parentCharacterSet'%curve,currentSet[0],type='string') 
                          #  cmds.rename(curve,'rootCtrl')
                        
                            self.errorMsgLEdit.setText('Root %s created'%rootName)
                    
                else:
                    self.errorMsgLEdit.setText('%s is not spine Character Set'%currentSet[0])
            except:
                self.errorMsgLEdit.setText('%s is not character set'%currentSet[0])
               # self.errorMsgLEdit.setText('%s is not spine Character Set'%currentSet[0])
                
                

       # characterSet = 
        '''      
        
        
        '''
          
   
               
    ### find all keyframe in characterSet
    def findAllKeyframes(self,characterSetGrp):
        print "findAllKeyframes"
        #characterSetGrp = 'saberSet'  ###input
        allObjects = cmds.ls(characterSetGrp,fl=True,dag=True,type='mesh')
        meshList = []
        allKeyFrameDict ={}
        for i in allObjects:
            try:
                if cmds.getAttr('%s.spine_skinType'%i) =='mesh':
                    meshList.append(i)
                else:
                    pass
            except:
                pass
                
        for i in meshList:
            allKeyframesList = []
            allDeformersList = cmds.listHistory(i)
            
            for deformer in allDeformersList:
                allKeyframes = cmds.keyframe( deformer, query=True)
                if allKeyframes == None:
                    pass
                else:
                    for f in allKeyframes:
                        if f in allKeyframesList:
                            pass
                        else:
                            allKeyframesList.append(f)
            allKeyFrameDict.update({i:allKeyframesList})
                     

        return allKeyFrameDict

    def defineVertexsValueDeltaTime(self,allKeyFrameListByDeformers):
        print "defineVertexsValueDeltaTime"
        errMsg = "get vertexValue Error"
        #print allKeyFrameListByDeformers
        frameStart = 0.0
        frameEnd = 120.0
        skinName = "default"
        meshDeformDict = {skinName:{}}
        
        meshList = allKeyFrameListByDeformers.keys()
        

       # print 'meshList',meshList
        for mesh in meshList:
            slotName = cmds.listRelatives(mesh,p=True)[0]
            attachmentName = cmds.getAttr('%s.spine_attachmentName'%slotName)
            print 'attachmentName',attachmentName

            meshDeformDict[skinName].update({slotName:{attachmentName:[]}})
            
            allvertexs = cmds.polyListComponentConversion(mesh,tv=True) ## get all vertexID
            vertexList = cmds.ls(allvertexs,fl=True)  ## get all vertexID
            
            keyFrameList = allKeyFrameListByDeformers[mesh]
            keyFrameList.append(frameStart)
            keyFrameList.append(frameEnd)
            keyFrameList = sorted(keyFrameList)
            vertexPositionPreFrameList= []

            for f in keyFrameList:
                vertexPositionCurrentFrameList = []
                deltaVertexPositionPreFrameList=[]
               # vertexPositionX_preFrame = 0.0
               # vertexPositionY_preFrame = 0.0
                cmds.currentTime(f,e=True)
                for vertex in vertexList:
                    vertexPosionX_CurrentFrame = cmds.pointPosition(vertex)[0]
                    vertexPosionY_CurrentFrame = cmds.pointPosition(vertex)[1]
                   # deltaPosionX = vertexPosionX_CurrentFrame-vertexPositionX_preFrame
                   # deltaPosionY = vertexPosionY_CurrentFrame-vertexPositionY_preFrame
                    vertexPositionCurrentFrameList.append(vertexPosionX_CurrentFrame)
                    vertexPositionCurrentFrameList.append(vertexPosionY_CurrentFrame)
                   # vertexPositionX_preFrame = cmds.pointPosition(vertex)[0]
                   # vertexPositionY_preFrame = cmds.pointPosition(vertex)[1]
                if f == 0.0:
                    for i in range(0,len(vertexPositionCurrentFrameList)):
                        deltaPosition = vertexPositionCurrentFrameList[i]
                        deltaVertexPositionPreFrameList.append(deltaPosition)
                        
                else:    
                        
                        
                    for i in range(0,len(vertexPositionCurrentFrameList)):
                        deltaPosition = vertexPositionCurrentFrameList[i] - vertexPositionPreFrameList[i]
                        deltaVertexPositionPreFrameList.append(deltaPosition)
                   # print deltaPosionX,deltaPosionY
                vertexPositionPreFrameList = vertexPositionCurrentFrameList
                print 'vertexPositionPreFrameList',vertexPositionPreFrameList
                meshDeformDict[skinName][slotName][attachmentName].append({"time":f/30.0,"vertices":deltaVertexPositionPreFrameList})


        return meshDeformDict
      #  allvertexs = cmds.polyListComponentConversion(meshName,tv=True)
        #vertexList = []
        '''
        cmds.select(allvertexs)
        vertexList = cmds.ls(sl=True,fl=True)
        cmds.select(cl=True)
        ox = cmds.getAttr("%s.translateX"%joinName)
        oy = cmds.getAttr("%s.translateY"%joinName)
        print ox,oy

       #  print vertexList
        vertexPositionForSpine= []
        for i in vertexList:
          #   print cmds.pointPosition(i)
            vertexPositionForSpine.append(cmds.pointPosition(i)[0]-ox)
            vertexPositionForSpine.append(cmds.pointPosition(i)[1]-oy)
             
        '''
        
        
                         
    #### 輸出     
    def defineDeformAnimation(self,characterSetGrp):
        print "defineDeformAnimation"
        
        #meshList = cmds.ls(sl=True)
        #characterSetGrp = 'saberSet'
        allKeyFrameListByDeformers = self.findAllKeyframes(characterSetGrp) ## 根據控制器，變形器，骨架，取得所有的keyFrame 
        
        meshDeformDict = self.defineVertexsValueDeltaTime(allKeyFrameListByDeformers) ## 取得每個keyframe的vertex 數值
        return meshDeformDict
        # print allKeyFrameListByDeformers
        '''
        deformDict = {}
            #getTime
            #getVertics

        allvertexs = cmds.polyListComponentConversion(meshName,tv=True)
        #vertexList = []
        cmds.select(allvertexs)
        vertexList = cmds.ls(sl=True,fl=True)
        cmds.select(cl=True)
        ox = 0##cmds.getAttr("%s.translateX"%joinName)
        oy = 0##cmds.getAttr("%s.translateY"%joinName)
        print ox,oy

       #  print vertexList
        vertexPositionForSpine= []
        for i in vertexList:
          #   print cmds.pointPosition(i)
            vertexPositionForSpine.append(cmds.pointPosition(i)[0]-ox)
            vertexPositionForSpine.append(cmds.pointPosition(i)[1]-oy)
             
        return vertexPositionForSpine
        '''
    def exortTOSpineJson(self): #regionSlot
        print "exortTOSpineJson"
        
        errMsg = "define all items in root ctrl"
        rootCtrlName = self.exportSpineRootLabelLEdit.text()
        characterSetGrp =[]
        boneList = [{ "name":rootCtrlName},]
        allMeshItem = []
        meshSlotList = []
        allBoneList = []
        #skinDict = {"default":{}}
        allObjInRootCtrl = cmds.listRelatives(rootCtrlName,c=True)
        print 'rootCtrlName',rootCtrlName
        for i in allObjInRootCtrl:
            if cmds.getAttr('%s.spine_tag'%i) == "spine_characterSet":
                characterSetGrp.append(i)

        allJointInRootCtrl = cmds.listRelatives(rootCtrlName,ad=True,type="joint")
        for i in allJointInRootCtrl:
            try:
                if cmds.getAttr('%s.spine_tag'%i) == "spine_bone":
                    allBoneList.append(i) 
            except:
                pass
        ## get boneList
        boneList = self.getAllBoneList(allBoneList)  
        ## get regionSlotList 
        regionSlotList = self.getAllRegionSlotList(allBoneList) 
        ## get regionSkinDict 
        skinDict = self.getAllRegionSkinList(regionSlotList)

        print 'skinDict',skinDict
        
    def getAllBoneList(self,allBoneList):

        boneList = []
        for bone in allBoneList:
          #  print bone
            #boneShotName =  i.split("|")[-1]
            boneParent = cmds.listRelatives(bone,p=True)
            if boneParent == None:
                pass
            else:
               boneParent = boneParent[0]
                
            x = cmds.getAttr("%s.translateX"%bone)
            if x == 0:        
                inputX= 0
            else:
                inputX= '{:.3f}'.format(x)
            y = cmds.getAttr("%s.translateY"%bone)
            if y == 0:        
                inputY = 0
            else:
                inputY = '{:.3f}'.format(y)
            r = cmds.getAttr("%s.rotateZ"%bone)
            
            if r == 0:        
                inputR = 0
            else:
                inputR = '{:.2f}'.format(r)           
            
            
            scaleX = cmds.getAttr("%s.scaleX"%bone)
            
            if scaleX == 0 or scaleX == 1 :        
                inputSX = scaleX
            else:
                inputSX = '{:.2f}'.format(scaleX)            
            
            
            scaleY = cmds.getAttr("%s.scaleY"%bone)
            if scaleY == 0 or scaleY == 1:        
                inputSY = scaleY
            else:
                inputSY = '{:.2f}'.format(scaleY)  
                
                                
            inheritScale = cmds.getAttr("%s.bone_inheritScale"%bone)
            inheritRation = cmds.getAttr("%s.bone_inheritRotation"%bone)
            print inheritScale,inheritRation
            boneDict = {"name":bone,
                        "parent":boneParent,
                        "rotation":inputR,
                        "x": inputX,
                        "y":inputY,
                        "scaleX":inputSX,
                        "scaleY":inputSY
                        }
            if inheritScale == False:
                boneDict.update({"inheritScale":"false"})
            if inheritRation == False:
                boneDict.update({"inheritRotation":"false"})
            boneList.append(boneDict)
            
        return boneList
        
    def getAllRegionSlotList(self,allBoneList):
        slotList = []
        
        for i in allBoneList:
              
                
            itemList = cmds.listRelatives(i,c=True)
            
            
            
            for j in itemList:
               # print j , cmds.nodeType(j)
                if cmds.getAttr('%s.spine_tag'%j) == 'spine_slot':
                    boneName = cmds.getAttr('%s.slot_bone'%j)#i["name"]
                    blendModeGet = int(cmds.getAttr("%s.slot_blend"%j))
                    if blendModeGet == 0:
                        blendMode = "normal"
                    elif blendModeGet == 1:
                        blendMode = "additive"
                    elif blendModeGet == 2:
                        blendMode = "multiply"
                    elif blendModeGet == 3:
                        blendMode = "screen"            
                    slotName = cmds.getAttr('%s.slot_name'%j)
                    
                    parent = cmds.getAttr('%s.slot_bone'%j)
                    fade = float(cmds.getAttr('%s.slot_fade'%parent))
                    color = cmds.getAttr('%s.slot_color'%j)[0]
                    alpha = float(cmds.getAttr('%s.slot_alpha'%j)) *fade
                    dark = cmds.getAttr('%s.slot_dark'%j)[0]
                    attachment = cmds.getAttr('%s.slot_attachment'%j)
                    alphaHex = "%02x"%int((alpha/1)*255)
                    colorHex = "%02x"%int((color[0]/1)*255) + "%02x"%int((color[1]/1)*255) +"%02x"%int((color[2]/1)*255)
                    darkHex = "%02x"%int((dark[0]/1)*255) + "%02x"%int((dark[1]/1)*255) +"%02x"%int((dark[2]/1)*255)
                    exportColorHex = str(colorHex + alphaHex)
                    
                    slotDict =  {"name":slotName,
                                 "bone":parent,
                                 "color":exportColorHex,
                                 "attachment":attachment,
                                 "blend":blendMode}
                    print 'darkHex',darkHex,type(darkHex)
                    if darkHex == "000000":
                        pass
                    else:
                        slotDict.update({"dark":darkHex})
                    slotList.append(slotDict)  #additive

                       
        return slotList    
 

    def getAllRegionSkinList(self,regionSlotList):
        print "getAllRegionSkinList"
        print 'regionSlotList',regionSlotList
        skinList= {"default":{}}
        
       # print "slotList",slotList
       # print "slotListLength",len(slotList)
            
        for i in regionSlotList:
            slotName = i["name"]
            attachment = cmds.getAttr('%s.slot_attachment'%slotName)
            width = int(cmds.getAttr( "%s.slot_width"%slotName))
            height = int(cmds.getAttr( "%s.slot_height"%slotName))
            x = int(cmds.getAttr( "%s.translateX"%slotName))
            y = int(cmds.getAttr( "%s.translateY"%slotName))
            r = float(cmds.getAttr( "%s.rotateZ"%slotName))

            
            regionSlotSkinDict = {attachment:{"width": width,"height": height, "x":x,"y":y }}
           
            if r == 0.0:
                pass
            else:
                regionSlotSkinDict[attachment].update({"rotation":'{:.2f}'.format(r)})
             
            skinList["default"].update({slotName:regionSlotSkinDict})                                                                                                              
        return skinList
                

    def defineRegionSlotAnimation(self,regionSlotList):
        print "defineRegionSlotAnimation"
        actionName = "testAction"
        animationList = {}
        actionAnimation={actionName:{"slots":{},
                                     "bones":{}}}     
                   
        soltsAnimationDict= {}     
        for slot in regionSlotList:  
            slotName = slot["name"]
            boneName = cmds.getAttr('%s.slot_bone'%slotName)
            attachment = cmds.getAttr('%s.slot_attachment'%slotName)
            tempSlotDict = { slotName:{"color":[]}}
            soltsAnimationDict.update(tempSlotDict)

           # attachment = slot["attachment"]     
             
            keyFrameList = []
            alphaGainkeyFrameList = cmds.keyframe(boneName, query=True)
            
            for i in alphaGainkeyFrameList:
                if i in keyFrameList:
                    pass
                else:
                    keyFrameList.append(i)
            keyFrameList = sorted(keyFrameList)

                            
                                    
                                                            
    def defineAllItemInRootCtrl(self):
        print "defineAllItemInRootCtrl"
        '''
        "animations": {
           "name": {
              "bones": { ... },
              "slots": { ... },
              "ik": { ... },
              "deform": { ... },
              "events": { ... },
              "draworder": { ... },
           },
           ...
        }
        
        "deform": {
           "skinName": {
              "slotName": {
                 "meshName": [
                    {
                       "time": 0,
                       "curve": [ 0.25, 0, 0.75, 1 ]
                    },
                    {
                       "time": 1.5,
                       "offset": 12,
                       "vertices": [ -0.75588, -3.68987, -1.01898, -2.97404, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       -1.01898, -2.97404, -0.75588, -3.68987, 0, 0, -0.75588, -3.68987, -0.75588, -3.68987,
                       -1.01898, -2.97404, -1.01898, -2.97404, -1.01898, -2.97404, -0.75588, -3.68987 ],
                       "curve": [ 0.25, 0, 0.75, 1 ]
                    },
                    ...
                 ],
                 ...
              },
              ...
           },
           ...
        }
        
        '''
        errMsg = "define all items in root ctrl"
        rootCtrlName = "rootCtrl"
        boneList = [{ "name":rootCtrlName},]
        allMeshItem = []
        meshSlotList = []
        skinDict = {"default":{}}

               
        characterSetGrp = "saberSet"


        allTransformsList =  cmds.listRelatives(characterSetGrp,c=True,p=False)
        allMeshSlotList = []
        allSkinNameList = []
        for i in allTransformsList:
            for j in cmds.listRelatives(i,c=True,p=False):
                try:
                    if cmds.nodeType(j) =='mesh' and cmds.getAttr('%s.spine_skinType'%j) =='mesh':
                        allMeshSlotList.append(i)
                        allSkinNameList.append(j)
                except:
                    pass
                
        
        

        #animationDict={"default":{"bones":{},"slots":{},"deform":{"default":{deformerDict}}}}

              # print i,cmds.nodeType(i)
          
          #self.defineExportData(boneList,skinDict)
        print 'allMeshSlotList',allMeshSlotList
        for slot in allMeshSlotList: ## define all mesh's slot
        #   print cmds.ls(i)
            try:
                self.defineSlot(slot,rootCtrlName) 
            except:
                pass
          
        for i in allSkinNameList:
            skinData = json.loads(cmds.getAttr('%s.spine_skinData'%i))
            # skinDict.update(skinData)
            skinDict["default"].update(skinData)
        #  exportFile = "C:/Users/alpha/Documents/GitHub/spineToolAdv/test_01.json" 


          #print allSlotItem
        slotList = self.getAllMeshSlots(allMeshSlotList)
        
        
        
        #animaitonSlotDict = 
        slotAnimationDict = self.defineSlotAnimation(allMeshSlotList)
        
        
        deformerDict = self.defineDeformAnimation(characterSetGrp)
        print deformerDict
        '''
        animationDict = {"default": {
                                  "bones": {},
                                  "slots": {},
                                  "ik": {},
                                  "deform": {},
                                  "events": {},
                                  "draworder": {}
                                }}
                                
        '''
        animationDict={"default":{"bones":{},
                                    "slots":slotAnimationDict,
                                    "deform":deformerDict}}
        
        print 'skinDict',skinDict
        print 'slotList',slotList
        print 'animationDict',animationDict
  
        self.defineExportData(boneList,skinDict,slotList,animationDict)

         # print slotList
          
          

    def defineSlotAnimation(self,slotList):
        print "defineSlotAnimation"
        
        slotAnimationDict = {}
        
        for slot in slotList:
            attachmentName = cmds.getAttr('%s.spine_attachmentName'%slot)
            slotAnimationDict.update({slot:{"attachment": [{ "time": 0, "name": attachmentName }]}})
            
            
        return slotAnimationDict
        
        
    def defineRootBone(self):
        print "defineRootBone"
        rootBone = cmds.ls(sl=True,typ='joint')
        if len(rootBone) == 1:
            rootBoneName = rootBone[0]
            self.setRootLineEdit.setText(rootBoneName)
            #print rootBone
        else:
            errMsg = 'get root bone'
            print errMsg
      
    def definecreateMesh(self):
        print "definecreateMesh"
        if len(cmds.ls(sl=True)) >1:
            pass
        else:
            currentMesh = cmds.ls(sl=True,dag=2,typ='mesh')[0]
            currentTransformName = cmds.ls(sl=True)[0]
            bbox = cmds.polyEvaluate(currentMesh,b=True)
            pivotX = bbox[0][0]+(bbox[0][1]-bbox[0][0])/2
            pivotY = bbox[1][0]+(bbox[1][1]-bbox[1][0])/2
            boneName = 'bone_'+'{:04d}'.format(0)
            cmds.select(cl=True)
            bone = cmds.joint(p=(pivotX,pivotY,0),n=boneName)

            print pivotX,pivotY
            cmds.addAttr(bone, ln='spineBone', numberOfChildren=17, attributeType='compound' )
            cmds.addAttr(bone, ln='spine_tag', sn='stag' , dt="string", parent='spineBone'  )

            cmds.addAttr(bone, ln='bone_name', sn='name' , dt="string", parent='spineBone'  )
            cmds.addAttr(bone, ln='bone_parent', sn='parent' , dt="string", parent='spineBone'  )
            cmds.addAttr(bone, ln='bone_slot', sn='slot' , dt="string", parent='spineBone'  )
            cmds.addAttr(bone, ln='bone_length', sn='length' , at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_transform', sn='transform' , at="enum",en="normal:onlyTranslation:noRotationOrReflection:noScale:noScaleOrReflection", parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_x', sn='x' , at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_y', sn='y' , at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_rotation', sn='rotation' , at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_scaleX',  at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_scaleY',  at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_shearX', sn='shearX' , at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_shearY', sn='shearY' , at="float", dv=0,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_inheritScale', sn='inheritScale' , at="bool", dv=1,parent='spineBone' ,k=True )
            cmds.addAttr(bone, ln='bone_inheritRotation', sn='inheritRotation' , at="bool", dv=1,parent='spineBone' ,k=True )
            cmds.addAttr(bone, longName='bone_color', usedAsColor=True, attributeType='float3',parent='spineBone' ,k=True )
            cmds.addAttr(bone, longName='bone_red', attributeType='float', parent='bone_color',k=True )
            cmds.addAttr(bone, longName='bone_green', attributeType='float', parent='bone_color',k=True )
            cmds.addAttr(bone, longName='bone_blue', attributeType='float', parent='bone_color',k=True )
            cmds.addAttr(bone, ln='skin_type', sn='skinType' , dt="string", parent='spineBone'  )


            ## add Spine Tag
            cmds.setAttr('%s.spine_tag'%bone,'spine_bone',type='string')
            cmds.setAttr('%s.bone_name'%bone,bone,type='string')
            cmds.setAttr('%s.bone_slot'%bone,currentTransformName,type='string')                        
            cmds.setAttr('%s.skin_type'%bone,'mesh',type='string')
             
            borderEdges = self.getMeshData(currentMesh)

            dataForSpine = self.getUVData(currentMesh,boneName,borderEdges)


            #attachment = i["attachment"]

            #slotSkinData = { slotName:{"attachment":slotSkinData}}
            # #print 'getSlotSkinData',getSlotSkinData
            # print 'slotSkinData',slotSkinData
            # skinList["default"].update(slotSkinData)

            print dataForSpine 

     
    def getAllMeshSlots(self,meshSlotList):
        print "getAllMeshSlots"
        slotList = []
        for i in meshSlotList:
            slotName = cmds.getAttr('%s.slot_name'%i)
           # slotName = cmds.listRelatives(slotMeshName,p=True)
            boneName = cmds.getAttr('%s.slot_bone'%i)
            attachment = cmds.getAttr('%s.slot_attachment'%i)
            slotBlendIndex = cmds.getAttr('%s.slot_blend'%i)
            if slotBlendIndex == 0:
                slotBlend = 'normal'
            elif slotBlendIndex ==1 :
                slotBlend = 'additive'
            elif slotBlendIndex ==2 :
                slotBlend = 'multiply'
            elif slotBlendIndex ==3 :
                slotBlend = 'screen'
            print 'slotBlend',slotBlend

            slotList.append({"name":slotName,
                                "bone":boneName,
                                "color":"ffffffff",
                                "attachment":attachment,
                                "blend":slotBlend})  #additive
        return slotList
  
    def getSelectSlotBone(self):
        print "getSelectSlotBone"
        allSelectorBone = cmds.ls(sl=True,type='joint')
        self.currentSelectBone = []
        for i in allSelectorBone:
            if cmds.getAttr('%s.spine_tag'%i) == "spine_bone":
                self.currentSelectBone.append(i)
        self.showAllSelectedObjLedit.setText(str(self.currentSelectBone))
        #cmds.
    
    def getSelectAnyTransform(self):
        
        print "getSelectAnyTransform"
        allSelectorTransform = cmds.ls(sl=True,type='transform')
        self.currentSelectBone = allSelectorTransform
        self.showAllSelectedObjLedit.setText(str(self.currentSelectBone))    
                    
    def renameSelectedBone(self):
        print "renameSelectedBone"
        newName = self.newNameSelectedLEdit.text()
       # print newName,self.currentSelectBone
        fileCount = len(self.currentSelectBone)
        try:
            for i in range(0,fileCount):
               # print #'{:04d}'.format(i)
                newBoneName = str(newName+'_'+'{:04d}'.format(i))
                newSlotName = str(newName+'_S_'+'{:04d}'.format(i))
                newShapeName = str(newName+'_S_Shape_'+'{:04d}'.format(i))
                bone = self.currentSelectBone[i]
                slot = cmds.listRelatives(bone,c=True,type ='transform')[0]
                shape = cmds.listRelatives(slot,c=True,type ='mesh')[0]
               # print bone,slot,shape,newBoneName,newSlotName,newShapeName
                cmds.setAttr('%s.bone_name'%bone,newBoneName,type='string')
                cmds.setAttr('%s.bone_slot'%bone,newSlotName,type='string')
                cmds.rename('%s'%bone,'%s'%newBoneName)
                cmds.rename('%s'%slot,'%s'%newSlotName)
                cmds.rename('%s'%shape,'%s'%newShapeName)
        except:
            pass
        self.getSelectSlotBone()
           # for j in self.currentSelectBone:
               # print i
        #cmds.listRelatives('star_A02_5',c=True,type = 'mesh')
        
        

        
    
    def optionalSelect(self):
            # print 'optionalSelect'     #1,2,3,4,5,6,7,8,9,0
        #self.currentOptionSelectState = [0,0,0,0,0,0,0,0,0,0]
        currentOptionSelectState = []
        if self.fillet_odd_btn.isChecked() == True:
            currentOptionSelectState.append("1")
            currentOptionSelectState.append("3")
            currentOptionSelectState.append("5")
            currentOptionSelectState.append("7")
            currentOptionSelectState.append("9")

        if self.fillet_even_btn.isChecked() == True: 
            currentOptionSelectState.append("2")
            currentOptionSelectState.append("4")
            currentOptionSelectState.append("6")
            currentOptionSelectState.append("8")
            currentOptionSelectState.append("0")
            
        if self.fillet_n1_btn.isChecked() == True: 
            currentOptionSelectState.append("1")
            
        if self.fillet_n2_btn.isChecked() == True: 
            currentOptionSelectState.append("2")
            
        if self.fillet_n3_btn.isChecked() == True: 
            currentOptionSelectState.append("3")
            
        if self.fillet_n4_btn.isChecked() == True: 
            currentOptionSelectState.append("4")
            
        if self.fillet_n5_btn.isChecked() == True: 
            currentOptionSelectState.append("5")
            
        if self.fillet_n6_btn.isChecked() == True: 
            currentOptionSelectState.append("6")
            
        if self.fillet_n7_btn.isChecked() == True: 
            currentOptionSelectState.append("7")
            
        if self.fillet_n8_btn.isChecked() == True: 
            currentOptionSelectState.append("8")
            
        if self.fillet_n9_btn.isChecked() == True: 
            currentOptionSelectState.append("9")
            
        if self.fillet_n0_btn.isChecked() == True: 
            currentOptionSelectState.append("0")

       # print self.fillet_odd_btn.isChecked()
       # print self.fillet_even_btn.isChecked()
        currentOptionSelectState = sorted(currentOptionSelectState)
       # print currentOptionSelectState
        filletSelect = []
        for i in currentOptionSelectState:
            if i in filletSelect:
                pass
            else:
                filletSelect.append(i)
        #print filletSelect
        newSelect = []
        for i in self.currentSelectBone:
            #print i[-1]
            if str(i[-1]) in filletSelect:
              #  print i
                newSelect.append(i)
        #print newSelect
        cmds.select(cl=True)
        cmds.select(newSelect)
       
                           
    def getAllSlots(self,boneList):
        print "getAllSlots"
        slotList = []
        for i in boneList:
            boneName = i["name"]
            # print i
            # print boneName
         
            itemList = cmds.listRelatives(boneName,c=True)
            print "itemList",boneName,itemList
            try:
                for j in itemList:
                # print j , cmds.nodeType(j)
                    if cmds.nodeType(j) == "transform" :
                        parentBone = cmds.listRelatives(j,p=True)[0]
                        getObj =  cmds.ls(j,dag=1)[1]
                        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
                        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
                        currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
                        fileInSlot = currentFile.split("/")[-1].split(".png")[0]
                        #  print "fileInSlot",fileInSlot
                        #print j , cmds.listRelatives(j,p=True)[0]
                        #  print "%s.blendMode" % fileNode[0]
                        try:
                            blendMode = cmds.getAttr("%s.blendMode" % fileNode[0])
                                  
                            #    print blendMode
                        except:
                            blendMode = "normal"
                            slotList.append({"name":j,
                                               "bone":parentBone,
                                               "color":"ffffffff",
                                               "attachment":fileInSlot,
                                               "blend":blendMode})  #additive
            except:
                pass
        return slotList
         




    def getMeshData(self,meshName):
        print "getMeshData"
        alledges = cmds.polyListComponentConversion(meshName,te=True)
        cmds.select(alledges)
        allEdgesList = cmds.ls(sl=True,fl=True)

        borderEdge = []
        for i in allEdgesList:
            toFace = cmds.select(cmds.polyListComponentConversion(i,tf=True))
            listFace = cmds.ls(sl=True,fl=True)
           #  print listFace
            if len(listFace )> 1:
                pass
            else:
                borderEdge.append(i)
        cmds.select(cl=True)

        # len(borderEdge)

        # cmds.select(borderEdge)

        return borderEdge



    def getBoneList(self):
        print "getBoneList"
        allJoints = cmds.ls(typ='joint')
        boneList = []
        for i in allJoints:
               
            try:
                if cmds.getAttr('%s.spine_tag'%i) == 'spine_bone':
                    boneList.append(i)
            except:
                pass

        return boneList

    

    def getSkinsList(self,slotList):
        print "getSkinsList"
        skinList= {"default":{}}
        for i in slotList:
            slotName = i["name"]
            joinName = i["bone"]
            attachment = i["attachment"]
            #print "slotName",slotName
            type = cmds.getAttr("%s.meshType"%slotName)
            if type == "mesh" :
                boneList = getMeshData(slotName)
                getSlotSkinData = getUVData(slotName,joinName,boneList)
                # getSlotSkinData.update({})
                slotSkinData = { slotName:{attachment:getSlotSkinData}}
                #print 'getSlotSkinData',getSlotSkinData
                # print 'slotSkinData',slotSkinData
                skinList["default"].update(slotSkinData)
        return skinList
  
        '''
        'skins':{
          'default':{
               slotName/skinName:{
                    attachmentName:slotSkinData
               }
          }
        }

        '''


    def getSkinData(self): 
        print "getSkinData"
        cmds.currentTime(0,e=True)
        meshName = cmds.ls(sl=True,dag=2,typ='mesh')[0]
        try:
            cmds.deleteAttr('%s.spine_skinData'%meshName)
            cmds.deleteAttr('%s.spine_boneName'%meshName)
            cmds.deleteAttr('%s.spine_attachmentName'%meshName)
            cmds.deleteAttr('%s.spine_skinName'%meshName)
            cmds.deleteAttr('%s.spine_slotName'%meshName)
            cmds.deleteAttr('%s.spine_skinType'%meshName)
            cmds.deleteAttr('%s.spine_tag'%meshName)
            cmds.deleteAttr('%s.spineSlot'%meshName)
        except:
            pass

        try:  
            cmds.addAttr(meshName, ln='spineSlot', numberOfChildren=7, attributeType='compound' )
            cmds.addAttr(meshName, ln='spine_tag', sn='stag' , dt="string", parent='spineSlot')
            cmds.addAttr(meshName, ln='spine_skinType', sn='skinType' , dt="string", parent='spineSlot')

            cmds.addAttr(meshName, ln='spine_slotName', sn='slotName' , dt="string", parent='spineSlot')
            cmds.addAttr(meshName, ln='spine_skinName', sn='skunName' , dt="string", parent='spineSlot')
            cmds.addAttr(meshName, ln='spine_attachmentName', sn='attachName' , dt="string", parent='spineSlot')
            cmds.addAttr(meshName, ln='spine_boneName', sn='boneName' , dt="string", parent='spineSlot')
            cmds.addAttr(meshName, ln='spine_skinData', sn='skinData' , dt="string", parent='spineSlot')

        except:
            pass
     

        #cmds.addAttr(bone, ln='bone_name', sn='name' , dt="string", parent='spineBone'  )
        # cmds.addAttr(bone, ln='bone_parent', sn='parent' , dt="string", parent='spineBone'  )

          

        errMsg ="unDefine"
        borderEdges = self.getMeshData(meshName)
        #dataForSpine = self.getUVData(currentMesh,boneName,borderEdges) joinName


        shadingGrps = cmds.listConnections(meshName ,type='shadingEngine')

        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
        # print fileNode

        attachmentName = cmds.getAttr("%s.fileTextureName" %fileNode).split('/')[-1].split('.')[0]

        #print attachmentName



        imageWidth = self.getImageMetaData(fileNode)[1]
        imageHeight = self.getImageMetaData(fileNode)[2]
        #print imageWidth,imageHeight, getImageMetaData(fileNode)
        # scaleRatio = imageHeight/imageWidth
        # print "scaleRatio",scaleRatio.imageWidth,imageHeight
        uvCount = cmds.polyEvaluate(meshName,uv=True)
        uvCoordDict ={}
        for i in range(0,uvCount):
            uvCoord = cmds.polyEditUV("%s.map[%s]"%(meshName,i),q=True)
        
            uvCoordDict.update({i:uvCoord})
        triangleVertexDict = {} 
        faceCount = cmds.polyEvaluate(meshName,f=True)
        for i in range(0,faceCount):
            toVertex = cmds.polyListComponentConversion("%s.f[%s]"%(meshName,i),tv=True,)
            cmds.select(toVertex)
            faceRefVertex = cmds.ls(sl=True,fl=True)
            triangleVertexDict.update({i:faceRefVertex})
        cmds.select(cl=True)

        edgeCount = cmds.polyEvaluate(meshName,e=True)
      
        border = cmds.polyListComponentConversion(cmds.ls(sl=True,fl=True),uvs=True)

        cmds.select(cl=True)
         
        uvCoordListForSpine = []
        for i in uvCoordDict.keys():
          #   print i
            uvCoordListForSpine.append(uvCoordDict[i][0])
            uvCoordListForSpine.append((1-uvCoordDict[i][1]))
        # print "uvCoordListForSpine",uvCoordListForSpine

        trianglesListForSpine = []
        for i in triangleVertexDict.keys():
            trianglesListForSpine.append(int(triangleVertexDict[i][0].split("[")[1].split("]")[0]))
            trianglesListForSpine.append(int(triangleVertexDict[i][1].split("[")[1].split("]")[0]))
            trianglesListForSpine.append(int(triangleVertexDict[i][2].split("[")[1].split("]")[0]))
             
        # print "trianglesListForSpine",trianglesListForSpine

        allvertexs = cmds.polyListComponentConversion(meshName,tv=True)
        #vertexList = []
        cmds.select(allvertexs)
        vertexList = cmds.ls(sl=True,fl=True)
        cmds.select(cl=True)
        ox = 0##cmds.getAttr("%s.translateX"%joinName)
        oy = 0##cmds.getAttr("%s.translateY"%joinName)
        print ox,oy

       #  print vertexList
        vertexPositionForSpine= []
        for i in vertexList:
          #   print cmds.pointPosition(i)
            vertexPositionForSpine.append(cmds.pointPosition(i)[0]-ox)
            vertexPositionForSpine.append(cmds.pointPosition(i)[1]-oy)
             
        # print "vertexPositionForSpin",vertexPositionForSpine

        # borderEdgesString = cmds.getAttr("%s.borderList"%meshName)
        # borderEdges = borderEdgesString.split(",")
        borderEdgesCount = len(borderEdges)
         
        edgesVertexDict = {}
        for i in range(0,borderEdgesCount):
            toVertex = cmds.polyListComponentConversion(borderEdges[i],tv=True,)
            cmds.select(toVertex)
            edgeRefVertex = cmds.ls(sl=True,fl=True)
            edgesVertexDict.update({i:edgeRefVertex})

        edgesVertexForSpineList = []
        for i in edgesVertexDict.keys():
            v1 = edgesVertexDict[i][0].split("[")[-1].split("]")[0]
            v2 = edgesVertexDict[i][1].split("[")[-1].split("]")[0]

            edgesVertexForSpineList.append(int(v1)*2)
            edgesVertexForSpineList.append(int(v2)*2)
         #print "edgesVertexForSpineList",edgesVertexForSpineList
        width = imageWidth#cmds.getAttr("%s.scaleX"%meshName)
        height = imageHeight#cmds.getAttr#("%s.scaleZ"%meshName)

        dataForSpine = {"type":"mesh",
                         "width":width,
                         "height":height,
                         "uvs":uvCoordListForSpine,"triangles":trianglesListForSpine,
                         "vertices":vertexPositionForSpine,"hull":borderEdgesCount,
                         "edges":edgesVertexForSpineList}
          
        #return dataForSpine
          
          
               
        
          
          
        slotName = cmds.listRelatives(meshName,p=True)[0]
        print 'slotName',slotName,meshName
        errMsg ="Define Data"
        print dataForSpine
        skinData = json.dumps({slotName:{attachmentName:dataForSpine}})

        
        
        cmds.setAttr('%s.spine_tag'%meshName,'spine_skin',type='string')
        cmds.setAttr('%s.spine_skinType'%meshName,'mesh',type='string')

        cmds.setAttr('%s.spine_slotName'%meshName,slotName,type='string')
        cmds.setAttr('%s.spine_skinName'%meshName,slotName,type='string')  
        #cmds.setAttr('%s.spine_boneName'%meshName,currentTransformName,type='string')             
                  
        cmds.setAttr('%s.spine_attachmentName'%meshName,attachmentName,type='string')
        cmds.setAttr('%s.spine_skinData'%meshName,skinData,type='string')  

        return skinData

          
          
          



    def getUVData(self,meshName,joinName,borderEdges):
        
        #getObj =  cmds.ls(meshName,dag=1)[1]
        print "getUVData"
         
        shadingGrps = cmds.listConnections(meshName ,type='shadingEngine')
          
       # print shadingGrps
         
          
 
        #cmds.polyEditUV("pPlane8.map[3]",q=True)
        #shadingGrps = cmds.listConnections(meshName,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
        print fileNode
        imageWidth = self.getImageMetaData(fileNode)[1]
        imageHeight = self.getImageMetaData(fileNode)[2]
        #print imageWidth,imageHeight, getImageMetaData(fileNode)
        # scaleRatio = imageHeight/imageWidth
        # print "scaleRatio",scaleRatio.imageWidth,imageHeight
        uvCount = cmds.polyEvaluate(meshName,uv=True)
        uvCoordDict ={}
        for i in range(0,uvCount):
            uvCoord = cmds.polyEditUV("%s.map[%s]"%(meshName,i),q=True)
        
            uvCoordDict.update({i:uvCoord})
        triangleVertexDict = {} 
        faceCount = cmds.polyEvaluate(meshName,f=True)
        for i in range(0,faceCount):
            toVertex = cmds.polyListComponentConversion("%s.f[%s]"%(meshName,i),tv=True,)
            cmds.select(toVertex)
            faceRefVertex = cmds.ls(sl=True,fl=True)
            triangleVertexDict.update({i:faceRefVertex})
        cmds.select(cl=True)

        edgeCount = cmds.polyEvaluate(meshName,e=True)
      
        border = cmds.polyListComponentConversion(cmds.ls(sl=True,fl=True),uvs=True)

        cmds.select(cl=True)
         
        uvCoordListForSpine = []
        for i in uvCoordDict.keys():
          #   print i
            uvCoordListForSpine.append(uvCoordDict[i][0])
            uvCoordListForSpine.append((1-uvCoordDict[i][1]))
        # print "uvCoordListForSpine",uvCoordListForSpine

        trianglesListForSpine = []
        for i in triangleVertexDict.keys():
               trianglesListForSpine.append(int(triangleVertexDict[i][0].split("[")[1].split("]")[0]))
               trianglesListForSpine.append(int(triangleVertexDict[i][1].split("[")[1].split("]")[0]))
               trianglesListForSpine.append(int(triangleVertexDict[i][2].split("[")[1].split("]")[0]))
             
        # print "trianglesListForSpine",trianglesListForSpine

        allvertexs = cmds.polyListComponentConversion(meshName,tv=True)
        #vertexList = []
        cmds.select(allvertexs)
        vertexList = cmds.ls(sl=True,fl=True)
        cmds.select(cl=True)
        ox = cmds.getAttr("%s.translateX"%joinName)
        oy = cmds.getAttr("%s.translateY"%joinName)
        print ox,oy

       #  print vertexList
        vertexPositionForSpine= []
        for i in vertexList:
          #   print cmds.pointPosition(i)
            vertexPositionForSpine.append(cmds.pointPosition(i)[0]-ox)
            vertexPositionForSpine.append(cmds.pointPosition(i)[1]-oy)
             
        # print "vertexPositionForSpin",vertexPositionForSpine

        # borderEdgesString = cmds.getAttr("%s.borderList"%meshName)
        # borderEdges = borderEdgesString.split(",")
        borderEdgesCount = len(borderEdges)
         
        edgesVertexDict = {}
        for i in range(0,borderEdgesCount):
            toVertex = cmds.polyListComponentConversion(borderEdges[i],tv=True,)
            cmds.select(toVertex)
            edgeRefVertex = cmds.ls(sl=True,fl=True)
            edgesVertexDict.update({i:edgeRefVertex})

        edgesVertexForSpineList = []
        for i in edgesVertexDict.keys():
            v1 = edgesVertexDict[i][0].split("[")[-1].split("]")[0]
            v2 = edgesVertexDict[i][1].split("[")[-1].split("]")[0]
     
            edgesVertexForSpineList.append(int(v1)*2)
            edgesVertexForSpineList.append(int(v2)*2)
         #print "edgesVertexForSpineList",edgesVertexForSpineList
        width = imageWidth#cmds.getAttr("%s.scaleX"%meshName)
        height = imageHeight#cmds.getAttr#("%s.scaleZ"%meshName)

        dataForSpine = {"type":"mesh",
                         "width":width,
                         "height":height,
                         "uvs":uvCoordListForSpine,"triangles":trianglesListForSpine,
                         "vertices":vertexPositionForSpine,"hull":borderEdgesCount,
                         "edges":edgesVertexForSpineList}
          
        return dataForSpine
          


    def getImageMetaData(self,fileNode):
        print "getImageMetaData" 
        currentFile = cmds.getAttr("%s.fileTextureName" % fileNode)
        fileInSlot = currentFile.split("/")[-1].split(".png")[0]
        image = ice.Load(currentFile)
        imageMetaData = image.GetMetaData()
        imageSize = imageMetaData['Original Size']
        imageWidth = int(imageMetaData['Original Size'].split(" ")[0].split("(")[1])
        imageHeight = int(imageMetaData['Original Size'].split(" ")[1].split(")")[0])

        return currentFile,imageWidth,imageHeight




                                                                           

    def jointSizeValueChange(self):
        print "jointSizeValueChange"
        currentValue = self.horizontalSlider.value() 
        # print currentValue

        self.jointSizeValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", '%s'%currentValue, None, -1))

        cmds.jointDisplayScale(currentValue)



     
     
    def defineCreateBGBtn(self):
        print "defineCreateBGBtn"
        bgWidth = int(self.createBG_comboBox.currentText().split('x')[0])
        bgHeight = int(self.createBG_comboBox.currentText().split('x')[1])
        print (bgWidth,bgHeight)
        slotPlane = cmds.polyPlane(n='BG_plane',sx=1,sy=1)[0]
        cmds.setAttr('%s.rotateX'%slotPlane,90)
        cmds.setAttr('%s.scaleX'%slotPlane,bgWidth)
        cmds.setAttr('%s.scaleZ'%slotPlane,bgHeight)

    def createCleanBone(self):
        print "createCleanBone"
        parentBoneList = cmds.ls(sl=True,type = 'transform')
        if len(parentBoneList) == 0:
            self.errorMsgLEdit.setText('pls select parent bone')
        elif len(parentBoneList) > 1:
            self.errorMsgLEdit.setText('more than one bone selected')
        elif len(parentBoneList) == 1:
            parentBone = str(parentBoneList[0])
            if len(self.createBoneNameLEdit.text()) ==0:
                self.errorMsgLEdit.setText('name the bone')
            else:
                boneName =  self.createBoneNameLEdit.text()
                allBoneList = cmds.ls(type='joint')
                print 'allBoneList',boneName,allBoneList
                if boneName in allBoneList:
                    self.errorMsgLEdit.setText('got the same joint name')
                    boneName = boneName +'_'+'{:04d}'.format(0)
                    
                else:
                    
                    print 'parentBone',parentBone
                bone = str(self.createBone(boneName))
                cmds.setAttr('%s.bone_name'%bone,boneName,type='string')

                cmds.setAttr('%s.bone_parent'%bone,parentBone,type='string')
      
                cmds.parent(bone,parentBone)
                cmds.select(parentBone)
                
     
    def createBone(self,boneName):
        print "createBone" #createBoneBtn
       # parentBone = cmds.ls(sl=True,type = 'transform')
        
                     # if cmds.getAttr('%s.spine_tag'%parentBone[0]) == "spine_RootSkeleton" or cmds.getAttr('%s.spine_tag'%parentBone[0]) == "spine_bone":

        
        #boneNum = 1
        #boneName = 'bone_'+'{:04d}'.format(0)
        boneAttr = {'bone_name':"string ",
                    "bone_length":"float",
                    "bone_transform":"enum",
                    "bone_x":"float",
                    "bone_y":"float",
                    "bone_rotation":"float",
                    "bone_scaleX":"float",
                    "bone_scaleY":"float",
                    "bone_shearX":"float",
                    "bone_shearY":"float",
                    "bone_inheritScale":"bool",
                    "bone_inheritRotation":"bool",
                    "bone_color":"float3"
                    }
        cmds.select(cl=True)
          
        bone = cmds.joint(p=(0,0,0),n=boneName)
          #print (bone)
          #attrCount = len(boneAttr.keys())
        cmds.addAttr(bone, ln='spineBone', numberOfChildren=23, attributeType='compound' )
        cmds.addAttr(bone, ln='spine_tag', sn='stag' , dt="string", parent='spineBone'  ) #1
        
        cmds.addAttr(bone, ln='bone_name', sn='name' , dt="string", parent='spineBone'  )
        cmds.addAttr(bone, ln='bone_parent', sn='parent' , dt="string", parent='spineBone'  )
        cmds.addAttr(bone, ln='bone_slot', sn='slot' , dt="string", parent='spineBone'  )
        cmds.addAttr(bone, ln='bone_length', sn='length' , at="float", dv=0,parent='spineBone' ,k=False ) #5
        cmds.addAttr(bone, ln='bone_transform', sn='transform' , at="enum",en="normal:onlyTranslation:noRotationOrReflection:noScale:noScaleOrReflection", parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_x', sn='x' , at="float", dv=0,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_y', sn='y' , at="float", dv=0,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_rotation', sn='rotation' , at="float", dv=0,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_scaleX',  at="float", dv=0,parent='spineBone' ,k=False )#10
        cmds.addAttr(bone, ln='bone_scaleY',  at="float", dv=0,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_shearX', sn='shearX' , at="float", dv=0,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_shearY', sn='shearY' , at="float", dv=0,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_inheritScale', sn='inheritScale' , at="bool", dv=1,parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='bone_inheritRotation', sn='inheritRotation' , at="bool", dv=1,parent='spineBone' ,k=False )
        
        cmds.addAttr(bone, ln='slot_width', sn='s_w', parent='spineBone',k=False   )#16
        cmds.addAttr(bone, ln='slot_height', sn='s_h', parent='spineBone',k=False   )
            
        cmds.addAttr(bone, ln='slot_color', usedAsColor=True, attributeType='float3',parent='spineBone' ,k=True )
        cmds.addAttr(bone, ln='slot_red', attributeType='float',dv=1.0, parent='slot_color',k=True )
        cmds.addAttr(bone, ln='slot_green', attributeType='float',dv=1.0, parent='slot_color',k=True )
        cmds.addAttr(bone, ln='slot_blue', attributeType='float',dv=1.0, parent='slot_color',k=True )
        
        cmds.addAttr(bone, ln='slot_alpha', attributeType='float',dv=1.0, parent='spineBone',k=True )
        cmds.addAttr(bone, ln='slot_fade', attributeType='float',dv=1.0, parent='spineBone',k=True )

        cmds.addAttr(bone, ln='slot_dark', usedAsColor=True, attributeType='float3',parent='spineBone' ,k=False )
        cmds.addAttr(bone, ln='slot_darkRed', attributeType='float', parent='slot_dark',k=False )
        cmds.addAttr(bone, ln='slot_darkGreen', attributeType='float', parent='slot_dark',k=False )
        cmds.addAttr(bone, ln='slot_darkBlue', attributeType='float', parent='slot_dark',k=False )                
        cmds.addAttr(bone, ln='slot_attachment', sn='s_att' , dt="string", parent='spineBone',k=False  )
        cmds.addAttr(bone, ln='slot_blend', sn='s_blend' , at="enum",en="normal:additive:multiply:screen", parent='spineBone' ,k=True )
        

        ## add Spine Tag
        cmds.setAttr('%s.spine_tag'%bone,'spine_bone',type='string')
        cmds.setAttr('%s.bone_name'%bone,bone,type='string')
        return bone
        
        
    def createSlot(self):
        print "createSlotBtn" 
        
        newBoneCreatedList = []
        slotAmount = int(self.amountSliderNumLEdit.text())

        selectedImageCount = 0
        try:
            selectedImageCount = len(self.imageListTable.selectedItems())
        except:
            pass
        currentImage = ''
        try:
            currentImage = self.imageListTable.currentItem().text()
        except:
            pass
        if len(currentImage) == 0 :
            self.errorMsgLEdit.setText('pls select one image from Table')
        else:
            
            slotName = currentImage.split('.')[0] #+ '{:04}'.format(0)
            
        print 'selectedImageCount',selectedImageCount,currentImage,slotName

        
        if selectedImageCount ==0:
            self.errorMsgLEdit.setText('no selected image')
        else:
            parentBone = cmds.ls(sl=True,type = 'transform')
            if len(parentBone) == 0:
                self.errorMsgLEdit.setText('no parent Bone selected')
            elif len(parentBone) >1:
                self.errorMsgLEdit.setText('more than one bone selected')
                
            elif len(parentBone) == 1:
                try:
                    for c in range(0,slotAmount):
                        if cmds.getAttr('%s.spine_tag'%parentBone[0]) == "spine_RootSkeleton" or cmds.getAttr('%s.spine_tag'%parentBone[0]) == "spine_bone":
                            self.errorMsgLEdit.setText(currentImage)
                           # imageSize = self.imageInfoTable.item(10,1).text()[1:-1].split(' ')
                            fileName = self.imageInfoTable.item(0,1).text()

                            imageW = int(self.imageInfoTable.item(3,1).text())
                            imageH = int(self.imageInfoTable.item(4,1).text())
                            slotPlane = str(cmds.polyPlane(n='%s_#'%slotName,sx=1,sy=1)[0])
                            cmds.setAttr('%s.rotateX'%slotPlane,90)
                            cmds.setAttr('%s.scaleX'%slotPlane,imageW)
                            cmds.setAttr('%s.scaleZ'%slotPlane,imageH)
                            

                            self.assignSurfaceShader(slotName,slotPlane,fileName)
                            

                            boneName = "bone_%s"%slotPlane # + '{:04d}'.format(0)

                            self.createBone(boneName)

                            cmds.setAttr('%s.bone_parent'%boneName,parentBone[0],type='string')
                            cmds.setAttr('%s.bone_slot'%boneName,slotPlane,type='string')
                            cmds.setAttr('%s.slot_width'%boneName,imageW)
                            cmds.setAttr('%s.slot_height'%boneName,imageH)
                           # attachmentFile = cmds.getAttr('%s.slot_attachment'%slotPlane)
                           # print 'attachmentFile',attachmentFile 
                           # cmds.setAttr('%s.slot_attachment'%bone,attachmentFile,type='string')

                          #  print 
          
                            #cmds.rename(bone,newBoneName)
                            self.defineSlot(slotPlane,boneName)
                            attachmentFile = str(cmds.getAttr('%s.slot_attachment'%slotPlane))
                            print 'attachmentFile',attachmentFile 
                            cmds.setAttr('%s.slot_attachment'%boneName,attachmentFile,type='string')
                            cmds.parent(slotPlane,boneName)
                            cmds.parent(boneName,parentBone[0])
                            newBoneCreatedList.append(boneName)
                            cmds.setAttr('%s.slot_width'%slotPlane,imageW)
                            cmds.setAttr('%s.slot_height'%slotPlane,imageH)
                            
                           # cmds.parent(bone,)
                            cmds.select(parentBone[0])
                        else:
                            self.errorMsgLEdit.setText('selected Bone is uncorrect A')
                except:
                    self.errorMsgLEdit.setText('selected Bone is uncorrect B')
        self.currentSelectBone = newBoneCreatedList
    
        self.showAllSelectedObjLedit.setText(str(self.currentSelectBone))           
                    
        if self.enableDynaSlotCheck.isChecked() == True:            
            self.defineDynamicKeys(newBoneCreatedList)
        else:
            pass
        
    def defineDynamicKeys(self,boneList):
        print 'defineDynamicKeys'
        print boneList
        
        if self.radioButton_createRad.isChecked() ==True:
            print "Radiation shape"
                
            self.setToRadiation(boneList)
                
                
        elif self.radioButton_createSquare.isChecked() == True:
            self.setSquare(boneList)
            
            
            
       
        elif self.radioButton_createSector.isChecked() == True:
            print "Sector shape"
            self.setSector(boneList)
            
            
        elif self.radioButton_createDirection.isChecked() == True:
            self.setDirection(boneList)
            
        elif self.radioButton_createFollowCurve.isChecked() == True:
            self.setAlongCurve(boneList)

    
    def getDagPath(self,node=None):
        sel = om.MSelectionList()
        sel.add(node)
        curveFn = om.MDagPath()
        sel.getDagPath(0, curveFn)
        return curveFn        
                

    def setAlongCurve(self,boneList):
      #  print "setAlongCurve"
       # self.statusbar.clearMessage()
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        frameTotal = endFrame - startFrame
        keys =  int(self.lineEdit_keys.text())
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

            for jointIndex in range(0,len(boneList)):
                joint = boneList[jointIndex]
                
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
                  
                                                
                                                    
                                                                                                    
        
    def setToRadiation(self,boneList):
        
        radius = int(self.lineEdit_RadiusA.text())
        amount = len(boneList)
       # jointAmount = int(self.lineEdit_shapeStartFrame.text())
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        print startFrame,endFrame,amount
        
        if self.checkBox_offsetRandom.isChecked() == True:
            for i in range(0,amount):
               
                rad =  random.uniform(0,math.pi*2) 
                x = radius * math.cos(rad)
                y = radius * math.sin(rad)

                joint = boneList[i]
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
                joint = boneList[i]
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
                
                
                  
    def getCurve(self):
        
        allObj = cmds.ls(sl=True,dag=2)
        self.allSelectCurveList = []
        for i in allObj:
            if cmds.nodeType(i) == "nurbsCurve":
                self.allSelectCurveList.append(i)
              
        if len(self.allSelectCurveList) == 0:
            self.errorMsgLEdit.setText("select at least one curve")
        
            
      #  print len(allSelectCurveList),allSelectCurveList
        #return allSelectCurveList
        
        self.lineEdit_selectCurve.setText("%s"%self.allSelectCurveList)
        #self.allSelectCurveList 
        

        
    def setDirection(self,boneList):
        print "set to direction"
        originX = int(self.lineEdit_DirectionX.text())
        originY = int(self.lineEdit_DirectionY.text())
        directionDegree = float(self.lineEdit_directionDegree.text())
        directionSpread = float(self.lineEdit_directionSpread.text())
        radius = int(self.lineEdit_RadiusA.text())

        
        amount = len(boneList)
       # jointAmount = int(self.lineEdit_shapeStartFrame.text())
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())


        
        for i in range(0,amount):
            rad = (directionDegree *math.pi)/180 + (random.uniform(-directionSpread,directionSpread)*math.pi)/180
            x = originX + int(radius * math.cos(rad))
            y = originY + int(radius * math.sin(rad))

            joint = boneList[i]
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
              
                                       
        
        
    def setSector(self,boneList):
        print "sector shape"
        
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        amount = len(boneList)
        sectorStartAngle = int(self.lineEdit_AngleA_start.text())
        sectorEndAngle = int(self.lineEdit_AngleA_end.text())
        angleMax = sectorEndAngle - sectorStartAngle
        angleStep = int(angleMax/amount)
        if self.checkBox_squareFillIn.isChecked() == True:
            for i in range(0,amount):
                joint = boneList[i]

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
                joint = boneList[i]

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
                  
                    
                    

                      
                                                          
        
    def setSquare(self,boneList):
        print "square shape"
        startFrame = float(self.lineEdit_shapeStartFrame.text())
        endFrame = float(self.lineEdit_shapeEndFrame.text())
        width = int(self.lineEdit_widthSquare.text())
        height = int(self.lineEdit_HeightA.text())
        amount = len(boneList)
        if self.checkBox_squareFillIn.isChecked() == True:
            for i in range(0,amount):
                joint = boneList[i]
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

                joint = boneList[i]
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
                  
                
                        
        
        
      
    def defineSelectObj(self):
        print "defineSelectObj"  
        currentTarget = cmds.ls(sl=True,typ='transform')[0]
     
        self.defineSlot(currentTarget)
        self.defineSkin(currentTarget)
          
          
          
          
          
          
          
          
    def defineSlot(self,slot,boneName):
      
        print "defineSlot",slot,boneName

        try:
            cmds.addAttr(slot, ln='spineSlot', numberOfChildren=11, attributeType='compound' )
            cmds.addAttr(slot, ln='spine_tag', sn='stag' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_name', sn='s_name' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_bone', sn='s_bone' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_width', sn='s_w', parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_height', sn='s_h', parent='spineSlot'  )
            
            cmds.addAttr(slot, ln='slot_color', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
            cmds.addAttr(slot, ln='slot_red', attributeType='float',dv=1.0, parent='slot_color',k=True )
            cmds.addAttr(slot, ln='slot_green', attributeType='float',dv=1.0, parent='slot_color',k=True )
            cmds.addAttr(slot, ln='slot_blue', attributeType='float',dv=1.0, parent='slot_color',k=True )
            cmds.addAttr(slot, ln='slot_alpha', attributeType='float',dv=1.0, parent='spineSlot',k=True )

            cmds.addAttr(slot, ln='slot_dark', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
            cmds.addAttr(slot, ln='slot_darkRed', attributeType='float', parent='slot_dark',k=True )
            cmds.addAttr(slot, ln='slot_darkGreen', attributeType='float', parent='slot_dark',k=True )
            cmds.addAttr(slot, ln='slot_darkBlue', attributeType='float', parent='slot_dark',k=True )                
            cmds.addAttr(slot, ln='slot_attachment', sn='s_att' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_frequence', sn='s_freq' , at="bool", dv=0,parent='spineSlot' ,k=True )
        
            cmds.addAttr(slot, ln='slot_blend', sn='s_blend' , at="enum",en="normal:additive:multiply:screen", parent='spineSlot' ,k=True )

        

               
               
        except:
            pass
        slotList = cmds.listRelatives( slot, c=True,ad=True,s=True)
        if len(slotList) > 1:
            self.errMsgLabel.setText('more than one shape in slot transform')
        else:
            slotName =  slot#cmds.listRelatives(slotList[0],p=True)[0]
        cmds.setAttr('%s.spine_tag'%slot,'spine_slot',type='string')
        cmds.setAttr('%s.slot_name'%slot,slot,type='string')
        cmds.setAttr('%s.slot_bone'%slot,boneName,type='string')
        getObj =  cmds.ls(slot,dag=1)[1]
          #print 'getObj',getObj
        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        if cmds.nodeType(shaders) == 'lambert':
            fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
        elif cmds.nodeType(shaders) == 'surfaceShader':

            fileNode = cmds.listConnections('%s.outColor' % (shaders[0]), type='file')
        currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
         # print 'currentFile',currentFile
        fileInSlot = currentFile.split("/")[-1][0:-4]
          #print 'fileInSlot',fileInSlot
        cmds.setAttr('%s.slot_attachment'%slot,fileInSlot,type='string')
        
                                          
    def defineSkin(self,slot):
        print "defineSkin"
        '''
        'skin':{
           'skinName':{
                'slotName':{
                     'attachmentName':{'x':0.0,'y':0.0,'width':0,'height':0},
                },
           'skinName':{
                'slotName':{
                     'type':'mesh',
                     'uvs':[],
                     'triangles':[],
                     'vertices':[],
                     'hull':[],
                     'edges':[],
                     'x':0,
                     'y':0,
                     'rotation':0
                     'width':50,
                     'height':50,
                } 
           },
                
           }                                                                  
        }        
        '''
          
        cmds.addAttr(slot, ln='spineSkin', numberOfChildren=1, attributeType='compound' )
        cmds.addAttr(slot, ln='skin_type', sn='s_type' , at="enum",en="region:mesh:linkedmesh:boundingbox:path:point:clipping", parent='spineSkin' ,k=True )


     
             
                   
    def assignSurfaceShader(self,imageName,object,fileName):  #imageName  as slot name
        print "assignSurfaceShader"
       # slotShaderName =  imageName + '_surfaceShader'
        
        imageName = imageName.split('/')[-1]
       # print ('fileName',fileName,imageName)
        imageExtName = fileName.split('.')[-1]
        cmds.select(cl=True)
        slotShaderName =  imageName + '_shader'

        slotFileName = imageName + '_imageFile'
        print 'fileName##########################',fileName,imageExtName#,slotShaderName
        slotSG = imageName + '_SG'
        if len(cmds.ls(slotShaderName)) == 0:
            print ('slotShaderName is not exist')
          #  shader = cmds.shadingNode("surfaceShader",asShader=True,n=slotShaderName)
            shader = cmds.shadingNode("lambert",asShader=True,n=slotShaderName)
            print 'shader',shader
            cmds.select(shader)
            shaderName = cmds.ls(sl=True)[0]
            # shader=cmds.rename(shader,slotShaderName)
            print 'shaderName',shaderName,shader
            file_node=cmds.shadingNode("file",asTexture=True,n=slotFileName)
            shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n=slotSG)
            cmds.connectAttr('%s.color' %shader ,'%s.surfaceShader' %shading_group)
            cmds.connectAttr('%s.outColor' %file_node, '%s.color' %shader)
            print 'fileName',fileName
            
           # if imageExtName == 'jpg':
             #   pass
         #   elif imageExtName == 'png':
            cmds.connectAttr('%s.outTransparency' %file_node, '%s.transparency' %shader)
            cmds.setAttr('%s.fileTextureName'%slotFileName,fileName,type='string')
            try:
                cmds.setAttr('%s.fileTextureName'%slotFileName,fileName,type='string')
                print 'assigned image file'
            except:
                pass
            cmds.select(object)
            cmds.hyperShade( assign=slotShaderName )
            cmds.select(cl=True)

             #  print ('create shrfaceShader named %s'%slotShaderName)

        elif len(cmds.ls(slotShaderName)) == 1:
               
            print ('%s is exist'%slotShaderName)
            cmds.select(object)
            cmds.hyperShade( assign=slotShaderName )
            cmds.select(cl=True)

        
   
    def defineImageTableFromSel(self):
        print 'defineImageTableFromSel'
        try:
            currentFolder = (self.spineItemTree.currentItem().text(1))
        except:
            pass
        #print os.path.isfile(currentFolder),currentFolder
        if self.selectSpineJobBtn.isChecked() ==True:
       # if len(self.spineImagesSpaceLEdit.text()) > 0:
            spineImageFolder = (self.spineImagesSpaceLEdit.text())#.encode('utf-8')
            fileName = spineImageFolder +'/' + currentFolder#.encode('utf-8')
            print 'fileName',fileName,os.path.isfile(fileName)
            if os.path.isfile(fileName) == True:### get file from spine images
                
                print 'fileName',fileName 
                
                try:
                    image = ice.Load(fileName)
                    imageMetaData = image.GetMetaData()
                    self.defineImageTableData(imageMetaData)
                    self.imagePreviewLabel.setPixmap(QtGui.QPixmap(fileName))
                except:
                    pass

                
                
        else:
        
           # print 'currentFolder',currentFolder
            try:
                files = os.listdir(currentFolder)
                imagesAllow = ['png','jpg','PNG','JPG']
                images = filter(lambda x: x.split('.')[-1] in imagesAllow, files)

             #   print 'images',images
                #self.createImageTable(images,50,currentFolder)
               # print self.imageListTable
                self.imageListTable.setRowCount(0)
                self.imageListTable.setColumnCount(0)
               # self.createImageTable(images,50,currentFolder)
                
               # self.createImageInfoTable()
                imagesCount = len(images)
                columnCount = 5
                columnWidth = 50
                rowCount = int(math.ceil(float(len(images))/float(columnCount)))
                rowHeight = columnWidth
               # print 'imagesCount',imagesCount,rowCount

                self.imageListTable.setGeometry(QtCore.QRect(5, 60,(columnCount*columnWidth+30), 525+30))

                self.imageListTable.setObjectName("tableWidget")
                self.imageListTable.setColumnCount(columnCount)
                self.imageListTable.setRowCount(rowCount)
                self.imageListTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
                self.imageListTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
                self.imageListTable.horizontalHeader().setVisible(False)
                self.imageListTable.verticalHeader().setVisible(False)
                #  self.imageListTable.setColumnWidth(0, 60)
               #   self.imageListTable.setColumnWidth(1, 60)
                for i in range(0,columnCount):
                    self.imageListTable.setColumnWidth(i, columnWidth)
                       
                for i in range(0,rowCount):
                    self.imageListTable.setRowHeight(i, columnWidth)

                       
                for i in range (0,imagesCount):

                    item = QtWidgets.QTableWidgetItem()
                    itemName = images[i]
                   # print 'itemName',itemName
                    imageUrl =currentFolder +'/'+ itemName
                    #print 'imageUrl',imageUrl
                    text = itemName.decode('utf-8').encode('utf-8')#str(itemName)
                    iconFile =QtGui.QIcon(imageUrl)
                    #iconFile.pixmap(QSize(22, 22))
                    row = math.floor(float(i)/float(columnCount))
                    column = i%columnCount
                    print imageUrl
                    self.imageListTable.setIconSize(QtCore.QSize(columnWidth,columnWidth))
        #self.icon.pixmap(QSize(22, 22)
                    self.imageListTable.setItem(row,column,item)

                    self.imageListTable.item(row, column).setIcon(iconFile)
                    self.imageListTable.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",text, None,-1))
                    #self.imageListTable.item(row, column).setData(QtCore.Qt.EditRole, )

                                                         
                self.imageListTable.itemClicked.connect(lambda x:self.imageInfo(currentFolder))
            
            except:
                pass
                
                                                                                                   
        #self.imageListTable.itemClicked.connect(self.imageInfo)
        
    def defineImageInfoDock(self):
        print "defineImageInfoDock"
        #folderDir = "C:/Users/alpha/Documents/GitHub/mayaTool/pipelineTool/UI"
        #.currentIndex()
        
        images = self.getImagesInFolder()
        print 'images',images
        imagesDir  = 'C:/Temp/images'#"//mcd-3d/data3d/spine_imageSources/"
       # self.createImageTable(images,50,imagesDir)
       # self.createImageInfoTable()
        #print self.spineItemTree
        #self.createImagePreviewTable()





    def createCamview(self):
        print "createCamview"
        # We have our Qt Layout where we want to insert, say, a Maya viewport
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockSpineItemTree)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # We set a qt object name for this layout.

        # We set the given layout as parent to carry on creating Maya UI using Maya.cmds and create the paneLayout under it.
        cmds.setParent('verticalLayout')
        paneLayoutName = cmds.paneLayout()
          
        # Create the model panel. I use # to generate a new panel with no conflicting name
        modelPanelName = cmds.modelPanel("embeddedModelPanel#", cam='persp')
          
        # Find a pointer to the paneLayout that we just created using Maya API
        ptr = mui.MQtUtil.findControl(paneLayoutName)
          
        # Wrap the pointer into a python QObject. Note that with PyQt QObject is needed. In Shiboken we use QWidget.
        paneLayoutQt = shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

        # Now that we have a QtWidget, we add it to our Qt layout
        qtLayout.addWidget(paneLayoutQt)

       
    def getImagesInFolder(self):
        print "getImagesInFolder"
        
        files = os.listdir("c:/temp/images")
        imagesAllow = ['png','jpg','PNG','JPG']
        imageFiles = filter(lambda x: x.split('.')[-1] in imagesAllow, files)
        return imageFiles          


          
      
          
          
          
     
    def defineImageTableData(self,imageMetaData):
        print "defineImageTableData"
       # imageKey = imageMetaData.keys()
       # print imageKey
        fileName = str(imageMetaData['File Name'])
        shortName = str(fileName.split('/')[-1])
        fileSize = str(imageMetaData['File Size'] +' bytes')
        #imageWH = imageMetaData['Original Size']
        imageW = str(imageMetaData['Original Size'].split(' ')[0].split('(')[1])
        imageH = str(imageMetaData['Original Size'].split(' ')[1].split(')')[0])
        bitSample =str(imageMetaData['Original Bits Per Sample'])
        print fileName,shortName,fileSize,imageW,imageH
        self.imageInfoTable.setItem(0,0,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow",'file name', None,-1))
        self.imageInfoTable.setItem(0,1,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow",fileName, None,-1))

        self.imageInfoTable.setItem(1,0,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow",'shor name', None,-1))     

        self.imageInfoTable.setItem(1,1,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(1, 1).setText(QtWidgets.QApplication.translate("MainWindow",shortName, None,-1))   
                
        self.imageInfoTable.setItem(2,0,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(2, 0).setText(QtWidgets.QApplication.translate("MainWindow",'file size', None,-1))     
                   
        self.imageInfoTable.setItem(2,1,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(2, 1).setText(QtWidgets.QApplication.translate("MainWindow",fileSize, None,-1))  
                       
        self.imageInfoTable.setItem(3,0,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(3, 0).setText(QtWidgets.QApplication.translate("MainWindow",'image width', None,-1))       
                          
        self.imageInfoTable.setItem(3,1,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(3, 1).setText(QtWidgets.QApplication.translate("MainWindow",imageW, None,-1))                         

              
        self.imageInfoTable.setItem(4,0,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(4, 0).setText(QtWidgets.QApplication.translate("MainWindow",'image height', None,-1))        
              
        self.imageInfoTable.setItem(4,1,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(4, 1).setText(QtWidgets.QApplication.translate("MainWindow",imageH, None,-1))        
                
        self.imageInfoTable.setItem(5,0,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(5, 0).setText(QtWidgets.QApplication.translate("MainWindow",'bit pre sample', None,-1))    
        
        self.imageInfoTable.setItem(5,1,QtWidgets.QTableWidgetItem())
        self.imageInfoTable.item(5, 1).setText(QtWidgets.QApplication.translate("MainWindow",bitSample, None,-1))            
        '''                
        for i in range(0,len(imageKey)):
            item = QtWidgets.QTableWidgetItem()
            self.imageInfoTable.setItem(i,0,item)
            itemName = imageKey[i]
            ## self.imageInfoTable.item(row, column).setIcon(iconFile)
            self.imageInfoTable.item(i, 0).setText(QtWidgets.QApplication.translate("MainWindow",'%s'%itemName, None,-1))

            item = QtWidgets.QTableWidgetItem()
            self.imageInfoTable.setItem(i,1,item)
            itemName = imageKey[i]
            itemValue = imageMetaData[itemName]
            ## self.imageInfoTable.item(row, column).setIcon(iconFile)
          
            self.imageInfoTable.item(i, 1).setText(QtWidgets.QApplication.translate("MainWindow",'%s'%itemValue, None,-1))

        '''
          ## define preview image table item
         
          
          
          
    def createImagePlane(self):
        print self.currentImageFullName
          

          

    def imageInfo(self,imagesDir):
        print 'imageInfo2'
        #print 'imageName',self.imageListTable.currentItem().icon()#.iconName()
        #imageUrl = self.imageListTable.currentItem().text()
        imageUrl = imagesDir + '/' + str(self.imageListTable.currentItem().text())
        self.currentImageFullName  = imageUrl
        self.imageSourceLEdit.setText(str(self.imageListTable.currentItem().text()))
       # imageUrl = self.folderDir + '/' + self.imageListTable.currentItem().text()

       # print 'imageUrl',imageUrl
        
       
        try:
            image = ice.Load(imageUrl)
            imageMetaData = image.GetMetaData()
            self.defineImageTableData(imageMetaData)
            self.imagePreviewLabel.setPixmap(QtGui.QPixmap(imageUrl))
        except:
            pass




    def run(self):
        print ("export json")
        setRoot = self.setRootLineEdit.text()
        boneList = self.defineBone(setRoot)
        skinDict = self.getSkinData()
        self.defineExportData(boneList,skinDict)
          #print (boneList)

    def defineBone(self,root):
          ###all z axis should aim up
        boneList=[]
        allNode =  self.getItemDepth(root)
        print ('allNode',allNode)
        for i in allNode:
            print "i",i,type(i),cmds.nodeType(i)
               
            if cmds.nodeType(i) == "joint":
                    #  print i
                    
                x = float("%.3f"%(cmds.getAttr("%s.translateX"%i)))
                y = float("%.3f"%(cmds.getAttr("%s.translateY"%i)))
                rz = float("%.3f"%(cmds.getAttr("%s.rotateZ"%i)))
                sx = float("%.3f"%(cmds.getAttr("%s.scaleX"%i)))
                sy = float("%.3f"%(cmds.getAttr("%s.scaleY"%i)))
                ox = float("%.3f"%(cmds.getAttr("%s.jointOrientX"%i)))
                #  if abs(ox) == 180:
                #    cmds.setAttr('%s.rotateAxisX'%i,180)
                oy = float("%.3f"%(cmds.getAttr("%s.jointOrientY"%i)))
                oz = float("%.3f"%(cmds.getAttr("%s.jointOrientZ"%i)))
                #  if oz <0 :
                #    cmds.setAttr('%s.rotateAxisX'%i,180)
                r  = oz+rz+oy
                child = cmds.listRelatives(i,c=True)
                   #   print "child",child
                if child == None:
                    length = 0
                else:
                    length = float("%.3f"%cmds.getAttr("%s.translateX"%child[0]))
                         # print "length",length
                          
                      #length = cmds.getAttr("%s.translateX"%child)
                   #   print length,type(length)
                if cmds.listRelatives(i,p=True) == None:
                          
                    boneInfo = {"name":i,"rotation":r,"x":x,"y":y,"length":length,"color":"ffffffff"}
                    #      print "It's root"
                else:
                    parentBone = cmds.listRelatives(i,p=True)[0]
                #      print "bone,(joint):",i, "parent:",parentBone
                    boneInfo = {"name":i,"parent":parentBone,"rotation":r,"x":x,"y":y,"length":length,"color":"ffffffff","transform":"normal"}

             
                    boneList.append(boneInfo)
                    
        return boneList
               
                 
    def getItemDepth(self,baseRoot):
        allNode =  cmds.ls(baseRoot,dag=2,l=True,typ ="joint")
        checkMaxDepth = []
        for i in allNode: #check joint depth
            # print "allNode",i
            if len(i.split("|")) in checkMaxDepth:
                pass
            else:
                checkMaxDepth.append(len(i.split("|")))
        depth =  sorted(checkMaxDepth)[-1]
        print "depth",depth
          # return depth

        jointListByLevel = []
        for i in range(0,depth):
            for j in allNode:
                # print "j",j,j.split("|")[-1],len(j.split("|"))
                 #print "i",i
                if len(j.split("|")) == (i+1):
                    if j.split("|")[-1] in jointListByLevel:
                        # print "aaaa"
                        pass
                    else:
                        # print "bbbb"
                        jointListByLevel.append(j.split("|")[-1])
        print "jointListByLevel",jointListByLevel
        return jointListByLevel            
                     
      


    def defineExportData(self,boneList,skinDict,slotList,animationDict):
          
        exportFile = "C:/Users/alpha/Documents/GitHub/spineToolAdv/test_02.json"
        exportData = {'skeleton':{},
                         'bones':boneList,
                         'slots':slotList,
                         'skins':skinDict,
                         'events':{},
                         'animations':animationDict        
        }
          
          
          
        writeData = json.dumps(exportData, sort_keys=True , indent =4) 
          #writeData = json.dumps(exportJson) 
        with open(exportFile, 'w') as the_file:
            the_file.write(writeData)
          



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

