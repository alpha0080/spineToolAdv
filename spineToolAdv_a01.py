# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/UI/dock_01.ui'
#
# Created: Thu Jul 19 21:51:31 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as mui
import shiboken2

import os,math
import sys
try:
     sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.7/lib/python2.7/Lib/site-packages")
     import ice
except:
     pass
     

class Ui_MainWindow(object):
     def setupUi(self, MainWindow):
          MainWindow.setObjectName("MainWindow")
          MainWindow.resize(1200, 950)
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
          print ('2',self)
          self.createDock()
         # self.createImageTable()
        #  self.getImagesInFolder()
          self.defineImageInfoDock()
          self.createPreviewImageDockButton()
     
     
     
     
     def defineImageInfoDock(self):
          folderDir = "C:/Users/alpha/Documents/GitHub/mayaTool/pipelineTool/UI"

          images = self.getImagesInFolder(folderDir)
          self.createImageTable(images,folderDir,50)
          self.createImageInfoTable()
          self.createImagePreviewTable()

     def createDock(self):
          
          self.dockWidgetImages = QtWidgets.QDockWidget(self)
          self.dockWidgetImages.setObjectName("dockWidget")
          self.dockWidgetImages.setMinimumWidth(300)
          self.dockWidgetImages.setMinimumHeight(600)

          self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidgetImages)
          
          self.previewImageDock = QtWidgets.QDockWidget(self)
          self.previewImageDock.setObjectName("previewImageDock")
          self.previewImageDock.setMinimumWidth(300)
          self.previewImageDock.setMinimumHeight(350)

          self.dockWidgetImagesInfo = QtWidgets.QDockWidget(self)
          self.dockWidgetImagesInfo.setObjectName("dockWidget")
          self.dockWidgetImagesInfo.setMinimumWidth(600)
          self.dockWidgetImagesInfo.setMinimumHeight(400)
        #  self.dockWidgetImagesInfo.setMaximumHeight(330)
          
          self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidgetImagesInfo)
          
          self.dockImageButton = QtWidgets.QDockWidget(self)
          self.dockImageButton.setObjectName("dockImageButton")
          self.dockImageButton.setMinimumWidth(300)
          self.dockImageButton.setMinimumHeight(600)


          self.dockCamview = QtWidgets.QDockWidget(self)
          self.dockCamview.setObjectName("dockCamview")
          self.dockCamview.setMinimumWidth(600)
          self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockCamview)
         # self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.previewImageDock)
         # self.dockWidgetContents = QtWidgets.QWidget()
          #self.dockWidgetContents.setObjectName("dockWidgetContents") 
         # self.dockWidgetImages.setGeometry(QtCore.QRect(0, 0, 400, 600))

          #self.dockWidget2 = QtWidgets.QDockWidget(self)
          #self.dockWidget2.setObjectName("dockWidget")
         # self.dockWidgetContents = QtWidgets.QWidget()
          #self.dockWidgetContents.setObjectName("dockWidgetContents") 
         # self.dockWidget2.setMinimumWidth(300)

        #  self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget2)
          self.splitDockWidget( self.dockWidgetImages, self.dockWidgetImagesInfo, QtCore.Qt.Horizontal)
          self.splitDockWidget( self.dockWidgetImagesInfo, self.dockCamview, QtCore.Qt.Horizontal)

          self.splitDockWidget( self.dockWidgetImages, self.previewImageDock, QtCore.Qt.Vertical)
          self.splitDockWidget( self.dockWidgetImagesInfo, self.dockImageButton, QtCore.Qt.Vertical)


     def createCamview(self):
         # We have our Qt Layout where we want to insert, say, a Maya viewport
          self.verticalLayout = QtWidgets.QVBoxLayout(self.dockCamview)
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

       
     def getImagesInFolder(self,folderDir):
          "define image folder"
          files = os.listdir(folderDir)
          imagesAllow = ['png','jpg','PNG','JPG']
          imageFiles = filter(lambda x: x.split('.')[-1] in imagesAllow, files)
          return imageFiles          
          
     def createImageInfoTable(self):
          print('create image info table')
          self.imageInfoTable = QtWidgets.QTableWidget(self.dockWidgetImagesInfo)
          self.imageInfoTable.setGeometry(QtCore.QRect(10, 50,550,330))
          columnCount = 2
          rowCount = 11
          rowHeight =30
          self.imageInfoTable.setObjectName("imageInfoTable")
          self.imageInfoTable.setColumnCount(columnCount)
          self.imageInfoTable.setRowCount(rowCount)
          self.imageInfoTable.setColumnWidth(0, 200)
          self.imageInfoTable.setColumnWidth(1, 350)
          self.imageInfoTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
          self.imageInfoTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

          self.imageInfoTable.horizontalHeader().setVisible(False)
          self.imageInfoTable.verticalHeader().setVisible(False)
          for i in range(0,rowCount):
               self.imageInfoTable.setRowHeight(i, rowHeight)

     def createPreviewImageDockButton(self):
          self.createSlotButton = QtWidgets.QPushButton(self.dockImageButton)
          self.createSlotButton.setGeometry(QtCore.QRect(50, 50, 150, 46))
          self.createSlotButton.setObjectName("pushButton")
          self.createSlotButton.setText(QtWidgets.QApplication.translate("MainWindow", "create Slot", None, -1))



     def createImagePreviewTable(self):
          self.imagePreviewTable = QtWidgets.QTableWidget(self.previewImageDock)
          self.imagePreviewTable.setGeometry(QtCore.QRect(10, 50,280,280))
          self.imagePreviewTable.setObjectName("imagePreviewTable")
          self.imagePreviewTable.setColumnCount(1)
          self.imagePreviewTable.setRowCount(1)
          self.imagePreviewTable.setColumnWidth(0, 280)
          self.imagePreviewTable.setRowHeight(0, 280)
          self.imagePreviewTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
          self.imagePreviewTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

          self.imagePreviewTable.horizontalHeader().setVisible(False)
          self.imagePreviewTable.verticalHeader().setVisible(False) 
          #self.imagePreviewTable.setStyleSheet(";\
         #                                    background-color:rgb(0,0,0);\
          #                                   ");
          self.imagePreviewTable.setStyleSheet("\
                                                  QTableWidget {\
                                                      background-color: rgb(0,0,0);\
                                                  }\
                                                  QTableWidget::item {\
                                                     background-color: rgb(0,0,0);\
                                                     padding:5px;\
                                                    }\
                                                  QTableWidget::icon {\
                                                     background-color: rgb(0,0,0);\
                                                     width:260px;\
                                                     heigth:260px;\
                                                    }\
                                                  QTableWidget::item:selected {\
                                                      background-color: rgb(0,0,0);\
                                                  }\
                                                  QTableWidget::item:hover {\
                                                      background-color: rgb(0,0,0);\
                                                  }\
                                                  "
                                                  )


          
      
          
          
          
     
     def defineImageTableData(self,imageMetaData):
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

          self.imageInfoTable.setStyleSheet(";\
                                             font-size:16px;\
                                             ");
                                             
          ## define preview image table item
         
          
          
          
          
          
     def createImageTable(self,images,folderDir,iconWidth):
          self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetImages)
          imagesCount = len(images)
          columnCount = 5
          columnWidth = iconWidth
          rowCount = int(math.ceil(float(len(images))/float(columnCount)))
          rowHeight = columnWidth
          
          self.tableWidget.setGeometry(QtCore.QRect(10, 50,(columnCount*columnWidth+30), 500+30))

          self.tableWidget.setObjectName("tableWidget")
          self.tableWidget.setColumnCount(columnCount)
          self.tableWidget.setRowCount(rowCount)
          self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
          self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
          self.tableWidget.horizontalHeader().setVisible(False)
          self.tableWidget.verticalHeader().setVisible(False)
        #  self.tableWidget.setColumnWidth(0, 60)
       #   self.tableWidget.setColumnWidth(1, 60)
          for i in range(0,columnCount):
               self.tableWidget.setColumnWidth(i, columnWidth)
               
          for i in range(0,rowCount):
               self.tableWidget.setRowHeight(i, columnWidth)

               
          for i in range (0,imagesCount):

               item = QtWidgets.QTableWidgetItem()
               itemName = images[i]
               imageUrl = folderDir +'/'+ itemName
               iconFile =QtGui.QIcon(imageUrl)
               row = math.floor(float(i)/float(columnCount))
               column = i%columnCount
            #   print images[i]
               self.tableWidget.setIconSize(QtCore.QSize(columnWidth,columnWidth))

               self.tableWidget.setItem(row,column,item)
               
               self.tableWidget.item(row, column).setIcon(iconFile)
               self.tableWidget.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",'%s'%itemName, None,-1))

          self.tableWidget.setStyleSheet(" border: 3px solid #5E749C;\
                                             color:white;\
                                             text-align: top;\
                                             padding: 4px;\
                                             border-radius: 7px;\
                                             position: absolute;\
                                             border-bottom-left-radius: 7px;\
                                             width: 15px");
                                             

                                                                                               
          self.tableWidget.itemClicked.connect(self.imageInfo)

          
          
          

     def imageInfo(self):
         # print 'asss'
          
         # print self.tableWidget.currentItem().text()
          
          folderDir = "C:/Users/alpha/Documents/GitHub/mayaTool/pipelineTool/UI"
          imageUrl = folderDir + '/' + self.tableWidget.currentItem().text()
          #print imageUrl
          
          image = ice.Load(imageUrl)
          imageMetaData = image.GetMetaData()
         # print imageMetaData.keys(),len(imageMetaData.keys())

          self.defineImageTableData(imageMetaData)

          item = QtWidgets.QTableWidgetItem()
          self.imagePreviewTable.setItem(0,0,item)
          iconFile =QtGui.QIcon(imageUrl)
          self.imagePreviewTable.setIconSize(QtCore.QSize(270,270))
          self.imagePreviewTable.item(0, 0).setIcon(iconFile)







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

