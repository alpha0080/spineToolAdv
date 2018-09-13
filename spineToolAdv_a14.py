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
        self.fontScale = 1  
          #initial data
       # self.folderDir = '//mcd-3d/data3d/spine_imageSources'  #'C:/Temp/testImage'
        self.imagesFilter = ['jpg','JPG','png','PNG']
          
        print ('2',self)
        self.createDock()
         # self.createImageTable()
        #  self.getImagesInFolder()

        self.defineImageInfoDock()
        self.defineImageButtonDock()
        self.initialWorkSpace()

       # self.definePreviewImageDock()
        self.initialSpineItemTree()
        #defineDockCamview
        self.createImageInfoTable()
           
           
           
    def initialWorkSpace(self):
        print "initialWorkSpace"
        #basicFilter = "*.json"
        #spineWorkSpace = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=1,fm=2)[0]
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
          #  self.imageListTable.clear()
           
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
        self.workSpaceInfoDock.setMinimumWidth(600)
        self.workSpaceInfoDock.setMinimumHeight(200)
        #self.workSpaceInfoDock.setMaximumHeight(200)
        
        
        
        self.dockWidgetImagesInfo = QtWidgets.QDockWidget(self)
        self.dockWidgetImagesInfo.setObjectName("dockWidget")
        self.dockWidgetImagesInfo.setMinimumWidth(600)
        self.dockWidgetImagesInfo.setMinimumHeight(400)
        #  self.dockWidgetImagesInfo.setMaximumHeight(330)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidgetImagesInfo)

        self.dockImageButton = QtWidgets.QDockWidget(self)
        self.dockImageButton.setObjectName("dockImageButton")
        self.dockImageButton.setMinimumWidth(300)
        self.dockImageButton.setMinimumHeight(300)


        self.dockSpineMeshProgress = QtWidgets.QDockWidget(self)
        self.dockSpineMeshProgress.setObjectName("dockMeshProgress")
        self.dockSpineMeshProgress.setMinimumWidth(400)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockSpineMeshProgress)


        self.dockExport = QtWidgets.QDockWidget(self)
        self.dockExport.setObjectName("dockExport")
        self.dockExport.setMinimumWidth(400)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockExport)

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
        self.splitDockWidget( self.dockSpineMeshProgress, self.dockExport, QtCore.Qt.Vertical)



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
                         height: 30px;\
                         background-color:#333333;\
                         border-top-right-radius: 8px;\
                         border-bottom-right-radius: 8px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#333333;\
                         text-align:left;\
                         }\
                         "    
        lineEditRightBMiddle = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#333333;\
                         border-style:solid;\
                         border-right-width:1px;\
                         border-color:#555555;\
                         text-align:left;\
                         }\
                         "                            

        lineEditRightB = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#333333;\
                         border-top-right-radius: 8px;\
                         border-bottom-right-radius: 8px;\
                         border-style:solid;\
                         border-width:0px;\
                         border-color:#333333;\
                         text-align:left;\
                         }\
                         "    
                                                                                                                                           
                                                                                                                         
                                        
        lineEditA = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#333333;\
                         border-radius :6px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:left;\
                         }\
                         "    
                         
        errMsgA = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#888888;\
                         color:#222222;\
                         border-radius :6px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#888888;\
                         text-align:left;\
                         }\
                         "                             
                         
                         
                         
        lineEditB = "\
                         QLineEdit {\
                         height: 30px;\
                         background-color:#333333;\
                         border-radius :6px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "     
                         
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
                         font-size:12px;\
                         background-color:#505050;\
                         border-radius :8px;\
                         border-style:solid;\
                         border-width:1px;\
                         border-color:#666666;\
                         text-align:center;\
                         }\
                         "                                                            
            
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
        self.selectSpineWorkSpaceBtn = QtWidgets.QPushButton(self.workSpaceInfoDock)
        self.selectSpineWorkSpaceBtn.setGeometry(QtCore.QRect(10, 20, 110,30))
        self.selectSpineWorkSpaceBtn.setObjectName("selectSpineWorkSpaceBtn")
        self.selectSpineWorkSpaceBtn.setText(QtWidgets.QApplication.translate("MainWindow", "work space", None, -1))
        self.selectSpineWorkSpaceBtn.clicked.connect(self.defineSpineWorkSpace)
        self.selectSpineWorkSpaceBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.spineWorkSpaceLEdit = QtWidgets.QLineEdit(self.workSpaceInfoDock)
        self.spineWorkSpaceLEdit.setGeometry(QtCore.QRect(120, 20, 450, 30))
        self.spineWorkSpaceLEdit.setObjectName("spineWorkSpaceLEdit")
        self.spineWorkSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineWorkSpaceLEdit.setText('')
        self.spineWorkSpaceLEdit.setStyleSheet(lineEditRightB)     
        
        
        self.selectImageDitBtn = QtWidgets.QPushButton(self.workSpaceInfoDock)
        self.selectImageDitBtn.setGeometry(QtCore.QRect(10, 60, 110,30))
        self.selectImageDitBtn.setObjectName("selectImageDitBtn")
        self.selectImageDitBtn.setText(QtWidgets.QApplication.translate("MainWindow", "images Folder", None, -1))
       # self.selectImageDitBtn.clicked.connect(self.defineSpineWorkSpace)
        self.selectImageDitBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.spineImagesSpaceLEdit = QtWidgets.QLineEdit(self.workSpaceInfoDock)
        self.spineImagesSpaceLEdit.setGeometry(QtCore.QRect(120, 60, 450, 30))
        self.spineImagesSpaceLEdit.setObjectName("spineImagesSpaceLEdit")
        self.spineImagesSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineImagesSpaceLEdit.setText('')
        self.spineImagesSpaceLEdit.setStyleSheet(lineEditRightB)     
        
        self.selectExportFolderBtn = QtWidgets.QPushButton(self.workSpaceInfoDock)
        self.selectExportFolderBtn.setGeometry(QtCore.QRect(10, 100, 110,30))
        self.selectExportFolderBtn.setObjectName("selectExportFolderBtn")
        self.selectExportFolderBtn.setText(QtWidgets.QApplication.translate("MainWindow", "export Folder", None, -1))
       # self.selectExportFolderBtn.clicked.connect(self.defineSpineWorkSpace)
        self.selectExportFolderBtn.setStyleSheet(buttonStyleLeftB)     

 
        self.spineExportSpaceLEdit = QtWidgets.QLineEdit(self.workSpaceInfoDock)
        self.spineExportSpaceLEdit.setGeometry(QtCore.QRect(120, 100, 450, 30))
        self.spineExportSpaceLEdit.setObjectName("spineExportSpaceLEdit")
        self.spineExportSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.spineExportSpaceLEdit.setText('')
        self.spineExportSpaceLEdit.setStyleSheet(lineEditRightB)  




        self.createMeshBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createMeshBtn.setGeometry(QtCore.QRect(170, 170, 150, 50))
        self.createMeshBtn.setObjectName("createMesh")
        self.createMeshBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Mesh", None, -1))
        self.createMeshBtn.clicked.connect(self.definecreateMesh)

        self.createClippingBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createClippingBtn.setGeometry(QtCore.QRect(340, 170, 150, 50))
        self.createClippingBtn.setObjectName("createClipping")
        self.createClippingBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Clip", None, -1))
        #self.createClippingBtn.clicked.connect(self.definecreateSlotBtn)





        self.createBoneBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createBoneBtn.setGeometry(QtCore.QRect(170, 240, 150, 50))
        self.createBoneBtn.setObjectName("createBone")
        self.createBoneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Bone", None, -1))
        self.createBoneBtn.clicked.connect(self.createBone)


        self.createBGBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createBGBtn.setGeometry(QtCore.QRect(0, 310, 150, 50))
        self.createBGBtn.setObjectName("createBone")
        self.createBGBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Define BG", None, -1))
        self.createBGBtn.clicked.connect(self.defineCreateBGBtn)


        self.createBG_comboBox = QtWidgets.QComboBox(self.dockImageButton)
        self.createBG_comboBox.setGeometry(QtCore.QRect(160, 310, 300, 50))
        self.createBG_comboBox.setObjectName("comboBox")
        itemNameList = ["100x100","200x200","250x250","300x300","400x400",
                         "512x512","600x600","800x800","1000x1000","1024x1024",
                         "1200x1200","1500x1500","1600x1600","1920x1080","1920x1920","2000x2000","2048x2048"]
        for i in range(0,len(itemNameList)):
            self.createBG_comboBox.addItem("")
            self.createBG_comboBox.setItemText(i, QtWidgets.QApplication.translate("MainWindow", itemNameList[i], None, -1))

        self.createBG_comboBox.setCurrentIndex(13)
          
          
        self.jointSizeLabel = QtWidgets.QLabel(self.dockImageButton)
        self.jointSizeLabel.setGeometry(QtCore.QRect(5, 380, 500, 50))
        self.jointSizeLabel.setObjectName("jointSizeLabel")
        self.jointSizeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "joint size", None, -1))

        self.jointSizeValueLabel = QtWidgets.QLabel(self.dockImageButton)
        self.jointSizeValueLabel.setGeometry(QtCore.QRect(100, 380, 500, 50))
        self.jointSizeValueLabel.setObjectName("jointSizeLabel")
        self.jointSizeValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", "10", None, -1))

        self.horizontalSlider = QtWidgets.QSlider(self.dockImageButton)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 380, 300, 50))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.jointSizeValueChange)

        self.setRootBoneJointBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.setRootBoneJointBtn.setGeometry(QtCore.QRect(0, 450, 150, 50))
        self.setRootBoneJointBtn.setObjectName("setRootBoneBtn")
        self.setRootBoneJointBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Set Root", None, -1))
        self.setRootBoneJointBtn.clicked.connect(self.defineRootBone)


        self.setRootLineEdit = QtWidgets.QLineEdit(self.dockImageButton)
        self.setRootLineEdit.setGeometry(QtCore.QRect(170, 450, 300, 50))
        self.setRootLineEdit.setObjectName("rootJointLineEdit")
        self.setRootLineEdit.setAlignment(QtCore.Qt.AlignCenter)

        ##
        self.testABtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testABtn.setGeometry(QtCore.QRect(0, 520, 150, 50))
        self.testABtn.setObjectName("setRootBoneBtn")
        self.testABtn.setText(QtWidgets.QApplication.translate("MainWindow", "testA", None, -1))
        self.testABtn.clicked.connect(self.run)

        self.testBBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testBBtn.setGeometry(QtCore.QRect(170, 520, 150, 50))
        self.testBBtn.setObjectName("testb")
        self.testBBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testB", None, -1))
        self.testBBtn.clicked.connect(self.defineAllItemInRootCtrl)

        self.testCBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testCBtn.setGeometry(QtCore.QRect(340, 520, 150, 50))
        self.testCBtn.setObjectName("testc")
        self.testCBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testC", None, -1))
        self.testCBtn.clicked.connect(self.defineDeformAnimation)



        self.createMeshBtn.setStyleSheet(buttonStyle)             
        self.createClippingBtn.setStyleSheet(buttonStyle)             


        self.createBoneBtn.setStyleSheet(buttonStyle)
        self.createBGBtn.setStyleSheet(buttonStyle)
        self.setRootBoneJointBtn.setStyleSheet(buttonStyle)             
        self.setRootLineEdit.setStyleSheet(buttonStyle)             
        self.testABtn.setStyleSheet(buttonStyle)             
        self.testBBtn.setStyleSheet(buttonStyle)             
        self.testCBtn.setStyleSheet(buttonStyle)             

        self.createBG_comboBox.setStyleSheet(buttonStyle)


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
        self.defineSpineCharacterGrpBox.setGeometry(QtCore.QRect(10, 120, 370, 350))
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
        self.characterNameLEdit.setGeometry(QtCore.QRect(160, 60, 180, 30))
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
        self.rootCtrlScaleEdit.setGeometry(QtCore.QRect(300,100, 40, 30))
        self.rootCtrlScaleEdit.setObjectName("rootCtrlScaleEdit")
        self.rootCtrlScaleEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rootCtrlScaleEdit.setText('10.0')
        self.rootCtrlScaleEdit.setStyleSheet(lineEditRightB)           
        



        self.defineMeshBtn = QtWidgets.QPushButton(self.defineSpineCharacterGrpBox)
        self.defineMeshBtn.setGeometry(QtCore.QRect(30, 150, 150, 30))
        self.defineMeshBtn.setObjectName("defineMesh")
        self.defineMeshBtn.setText(QtWidgets.QApplication.translate("MainWindow", "define Mesh", None, -1))
        self.defineMeshBtn.clicked.connect(self.getSkinData)
        self.defineMeshBtn.setStyleSheet(buttonStyleB)     
        
        ###### defineSpineSlotBoneGrpBox
        self.defineSpineSlotBoneGrpBox = QtWidgets.QGroupBox(self.dockWidgetImagesInfo )
        self.defineSpineSlotBoneGrpBox.setGeometry(QtCore.QRect(10, 10, 370, 350))
        self.defineSpineSlotBoneGrpBox.setObjectName("defineSpineCharacterGrpBox")
        self.defineSpineSlotBoneGrpBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
        self.defineSpineSlotBoneGrpBox.setStyleSheet(QGroupBoxA)     
        self.defineSpineSlotBoneGrpBox.setVisible(True)
     
        

        self.createSlotBtn = QtWidgets.QPushButton(self.defineSpineSlotBoneGrpBox)
        self.createSlotBtn.setGeometry(QtCore.QRect(10, 10, 150, 30))
        self.createSlotBtn.setObjectName("createSlot")
        self.createSlotBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Slot", None, -1))
        self.createSlotBtn.clicked.connect(self.createSlot)              
        self.createSlotBtn.setStyleSheet(buttonStyleB)   
        
        self.testDBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.testDBtn.setGeometry(QtCore.QRect(10, 300, 100, 30))
        self.testDBtn.setObjectName("testDBtn")
        self.testDBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testD", None, -1))
        self.testDBtn.clicked.connect(self.testD)
        self.testDBtn.setStyleSheet(buttonStyleB)             
        
        
        
        
        
        self.exportLabel = QtWidgets.QLabel(self.dockExport)
        self.exportLabel.setGeometry(QtCore.QRect(10, 0, 300, 50))
        self.exportLabel.setObjectName("exportLabel")
        self.exportLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Export", None, -1))
        self.exportLabel.setStyleSheet(buttonStyleB)   
             
        
        

        self.setCharacterSetBTn = QtWidgets.QPushButton(self.dockImageButton)
        self.setCharacterSetBTn.setGeometry(QtCore.QRect(10, 450, 150, 30))
        self.setCharacterSetBTn.setObjectName("setCharacterSetBTn")
        self.setCharacterSetBTn.setText(QtWidgets.QApplication.translate("MainWindow", "select Character Set", None, -1))
        self.setCharacterSetBTn.clicked.connect(self.setCharacterSetName)
        self.setCharacterSetBTn.setStyleSheet(buttonStyleB)     
        

        self.exportSpineJsonBtn = QtWidgets.QPushButton(self.dockSpineMeshProgress)
        self.exportSpineJsonBtn.setGeometry(QtCore.QRect(10, 750, 150, 30))
        self.exportSpineJsonBtn.setObjectName("exportSpineJson")
        self.exportSpineJsonBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Export Spine Json", None, -1))
        self.exportSpineJsonBtn.clicked.connect(self.defineAllItemInRootCtrl)
        self.exportSpineJsonBtn.setStyleSheet(buttonStyleB)     

       
        self.analyzeCharacterSet = QtWidgets.QPushButton(self.dockSpineMeshProgress)
        self.analyzeCharacterSet.setGeometry(QtCore.QRect(10, 500, 150, 30))
        self.analyzeCharacterSet.setObjectName("analyzeCharacterSet")
        self.analyzeCharacterSet.setText(QtWidgets.QApplication.translate("MainWindow", "analyze Character Set", None, -1))
        self.analyzeCharacterSet.clicked.connect(self.doAnalyzeCharacterSet)
        self.analyzeCharacterSet.setStyleSheet(buttonStyleB)     
        
        
        
        
        

        self.setCharacterSetLineEdit = QtWidgets.QLineEdit(self.dockImageButton)
        self.setCharacterSetLineEdit.setGeometry(QtCore.QRect(170, 450, 200, 30))
        self.setCharacterSetLineEdit.setObjectName("rootJointLineEdit")
        self.setCharacterSetLineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "Character Set Name", None, -1))
        self.setCharacterSetLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.setCharacterSetLineEdit.setStyleSheet(lineEditA)     

        self.startFrameLabel = QtWidgets.QLabel(self.dockExport)
        self.startFrameLabel.setGeometry(QtCore.QRect(10, 50, 70, 30))
        self.startFrameLabel.setObjectName("startFrameLabel")
        self.startFrameLabel.setText(QtWidgets.QApplication.translate("MainWindow", " Start Frame", None, -1))
        self.startFrameLabel.setStyleSheet(labelA)  


        self.timeStartLEdit = QtWidgets.QLineEdit(self.dockExport)
        self.timeStartLEdit.setGeometry(QtCore.QRect(80, 50, 60, 30))
        self.timeStartLEdit.setObjectName("timeStartLEdit")
        self.timeStartLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0.0", None, -1))
        self.timeStartLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeStartLEdit.setStyleSheet(lineEditCMiddle)     

        self.endFrameLabel = QtWidgets.QLabel(self.dockExport)
        self.endFrameLabel.setGeometry(QtCore.QRect(140, 50, 70, 30))
        self.endFrameLabel.setObjectName("endFrameLabel")
        self.endFrameLabel.setText(QtWidgets.QApplication.translate("MainWindow", "  End Frame", None, -1))
        self.endFrameLabel.setStyleSheet(labelAMiddle)  


        self.timeEndLEdit = QtWidgets.QLineEdit(self.dockExport)
        self.timeEndLEdit.setGeometry(QtCore.QRect(210, 50, 60, 30))
        self.timeEndLEdit.setObjectName("timeEndLEdit")
        self.timeEndLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "120.0", None, -1))
        self.timeEndLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEndLEdit.setStyleSheet(lineEditCMiddle)   
        
        self.fpsLabel = QtWidgets.QLabel(self.dockExport)
        self.fpsLabel.setGeometry(QtCore.QRect(270, 50, 50, 30))
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsLabel.setText(QtWidgets.QApplication.translate("MainWindow", "  FPS", None, -1))
        self.fpsLabel.setStyleSheet(labelAMiddle)  
          
        self.fpsLEdit = QtWidgets.QLineEdit(self.dockExport)
        self.fpsLEdit.setGeometry(QtCore.QRect(320, 50, 50, 30))
        self.fpsLEdit.setObjectName("fpsLEdit")
        self.fpsLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "30.0", None, -1))
        self.fpsLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fpsLEdit.setStyleSheet(lineEditC)               
  
        self.exportSpineRootLabel = QtWidgets.QLabel(self.dockExport)
        self.exportSpineRootLabel.setGeometry(QtCore.QRect(10, 100, 110, 30))
        self.exportSpineRootLabel.setObjectName("exportSpineRootLabel")
        self.exportSpineRootLabel.setText(QtWidgets.QApplication.translate("MainWindow", " export Spine Root", None, -1))
        self.exportSpineRootLabel.setStyleSheet(labelA)  
               
        self.exportSpineRootLabelLEdit = QtWidgets.QLineEdit(self.dockExport)
        self.exportSpineRootLabelLEdit.setGeometry(QtCore.QRect(120, 100, 250, 30))
        self.exportSpineRootLabelLEdit.setObjectName("exportSpineRootLabelLEdit")
        self.exportSpineRootLabelLEdit.setText(QtWidgets.QApplication.translate("MainWindow", "spine_RootSkeleton", None, -1))
        self.exportSpineRootLabelLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.exportSpineRootLabelLEdit.setStyleSheet(lineEditC)                                    
 
                                                          
        
        self.selectExportFileBTn = QtWidgets.QPushButton(self.dockExport)
        self.selectExportFileBTn.setGeometry(QtCore.QRect(10, 150, 110,30))
        self.selectExportFileBTn.setObjectName("selectExportFileBTn")
        self.selectExportFileBTn.setText(QtWidgets.QApplication.translate("MainWindow", "file name", None, -1))
        self.selectExportFileBTn.clicked.connect(self.defineExportFileName)
        self.selectExportFileBTn.setStyleSheet(buttonStyleLeftB)     

 
        self.selectExportFileBTnLEdit = QtWidgets.QLineEdit(self.dockExport)
        self.selectExportFileBTnLEdit.setGeometry(QtCore.QRect(120, 150, 250, 30))
        self.selectExportFileBTnLEdit.setObjectName("rootJointLineEdit")
        self.selectExportFileBTnLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.selectExportFileBTnLEdit.setText('')
        self.selectExportFileBTnLEdit.setStyleSheet(lineEditRightB)     
          
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


     
    def createBone(self):
        print "createBone" #createBoneBtn
        #boneNum = 1
        boneName = 'bone_'+'{:04d}'.format(0)
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
        cmds.addAttr(bone, ln='spineBone', numberOfChildren=16, attributeType='compound' )
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


        ## add Spine Tag
        cmds.setAttr('%s.spine_tag'%bone,'spine_bone',type='string')
        cmds.setAttr('%s.bone_name'%bone,bone,type='string')
        return bone
        
        
    def createSlot(self):
        print "createSlotBtn" 
        #errMsg = "create Slot fail"
        #self.initialSpineItemTree()
        #print errMsg
        
        selectedImageCount = len(self.imageListTable.selectedItems())
        currentImage = self.imageListTable.currentItem().text()
        slotName = currentImage.split('.')[0]
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
                    if cmds.getAttr('%s.spine_tag'%parentBone[0]) == "spine_RootSkeleton" or cmds.getAttr('%s.spine_tag'%parentBone[0]) == "spine_bone":
                        self.errorMsgLEdit.setText(currentImage)
                        imageSize = self.imageInfoTable.item(10,1).text()[1:-1].split(' ')
                        fileName = self.imageInfoTable.item(2,1).text()

                        imageW = int(imageSize[0])
                        imageH = int(imageSize[1])
                        slotPlane = cmds.polyPlane(n='%s_#'%slotName,sx=1,sy=1)[0]
                        cmds.setAttr('%s.rotateX'%slotPlane,90)
                        cmds.setAttr('%s.scaleX'%slotPlane,imageW)
                        cmds.setAttr('%s.scaleZ'%slotPlane,imageH)
                        self.assignSurfaceShader(slotName,slotPlane,fileName)
                        
                        ###create bone for slot
                        bone = self.createBone()
                        print 'bone',bone
                        print 'slotPlane',slotPlane
                        newBoneName = ("bone_%s"%slotPlane)
                        cmds.setAttr('%s.bone_name'%(str(bone)),'hjhgjhg')
                        cmds.rename(bone,newBoneName)
                        self.defineSlot(slotPlane,newBoneName)
                        #cmds.parent(slotPlane,bone)
                       # cmds.parent(bone,)
                        
                    else:
                        self.errorMsgLEdit.setText('selected Bone is uncorrect')
                except:
                    self.errorMsgLEdit.setText('selected Bone is uncorrect')
                       
      
    def defineSelectObj(self):
        print "defineSelectObj"  
        currentTarget = cmds.ls(sl=True,typ='transform')[0]
     
        self.defineSlot(currentTarget)
        self.defineSkin(currentTarget)
          
          
          
          
          
          
          
          
    def defineSlot(self,slot,boneName):
      
        print "defineSlot",slot,boneName

        try:
            cmds.addAttr(slot, ln='spineSlot', numberOfChildren=8, attributeType='compound' )
            cmds.addAttr(slot, ln='spine_tag', sn='stag' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_name', sn='s_name' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slot, ln='slot_bone', sn='s_bone' , dt="string", parent='spineSlot'  )
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

        cmds.select(cl=True)
        slotShaderName =  imageName + '_shader'

        slotFileName = imageName + '_imageFile'
       # print 'slotFileName',slotFileName,slotShaderName
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
        imageKey = imageMetaData.keys()
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


          ## define preview image table item
         
          
          
          
          
          

          

    def imageInfo(self,imagesDir):
        print 'imageInfo'
        #print 'imageName',self.imageListTable.currentItem().icon()#.iconName()
        #imageUrl = self.imageListTable.currentItem().text()
        imageUrl = imagesDir + '/' + str(self.imageListTable.currentItem().text())
        
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

