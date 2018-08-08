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
          
          #initial data
          self.folderDir = 'C:/Temp/testImage'
          
          
          print ('2',self)
          self.createDock()
         # self.createImageTable()
        #  self.getImagesInFolder()
          self.defineImageInfoDock()
          self.defineImageButtonDock()
          self.definePreviewImageDock()
          self.defineDockCamview()
     
     
     
     def defineImageButtonDock(self):
          
          buttonStyle = "\
                         QLineEdit {\
                         htight:50px;\
                         background-color:#333333;\
                         border-radius :5px;\
                         border-style:solid;\
                         border-width:3px;\
                         border-color:#5E749C;\
                         text-align:center;\
                         }\
                         QComboBox {\
                         htight:50px;\
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
        
         
                         
                   
                                                                   
          self.errMsgLabel = QtWidgets.QLabel(self.dockImageButton)
          self.errMsgLabel.setGeometry(QtCore.QRect(0, 50, 500, 50))
          self.errMsgLabel.setObjectName("errMsgLabel")
          self.errMsgLabel.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
          
          
          self.createSlotBtn = QtWidgets.QPushButton(self.dockImageButton)
          self.createSlotBtn.setGeometry(QtCore.QRect(0, 100, 150, 50))
          self.createSlotBtn.setObjectName("createSlot")
          self.createSlotBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Slot", None, -1))
          self.createSlotBtn.clicked.connect(self.definecreateSlotBtn)
     
     
         
          self.createBoneBtn = QtWidgets.QPushButton(self.dockImageButton)
          self.createBoneBtn.setGeometry(QtCore.QRect(200, 100, 150, 50))
          self.createBoneBtn.setObjectName("createBone")
          self.createBoneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Bone", None, -1))
          self.createBoneBtn.clicked.connect(self.defineCreateBoneBtn)
     
     
          self.createBGBtn = QtWidgets.QPushButton(self.dockImageButton)
          self.createBGBtn.setGeometry(QtCore.QRect(0, 170, 150, 50))
          self.createBGBtn.setObjectName("createBone")
          self.createBGBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Define BG", None, -1))
          self.createBGBtn.clicked.connect(self.defineCreateBGBtn)
          

          self.createBG_comboBox = QtWidgets.QComboBox(self.dockImageButton)
          self.createBG_comboBox.setGeometry(QtCore.QRect(160, 170, 300, 50))
          self.createBG_comboBox.setObjectName("comboBox")
          itemNameList = ["100x100","200x200","250x250","300x300","400x400",
                         "512x512","600x600","800x800","1000x1000","1024x1024",
                         "1200x1200","1500x1500","1600x1600","1920x1080","1920x1920","2000x2000","2048x2048"]
          for i in range(0,len(itemNameList)):
               self.createBG_comboBox.addItem("")
               self.createBG_comboBox.setItemText(i, QtWidgets.QApplication.translate("MainWindow", itemNameList[i], None, -1))

          self.createBG_comboBox.setCurrentIndex(13)
          
          
          self.jointSizeLabel = QtWidgets.QLabel(self.dockImageButton)
          self.jointSizeLabel.setGeometry(QtCore.QRect(5, 250, 500, 50))
          self.jointSizeLabel.setObjectName("jointSizeLabel")
          self.jointSizeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "joint size", None, -1))
          
          self.jointSizeValueLabel = QtWidgets.QLabel(self.dockImageButton)
          self.jointSizeValueLabel.setGeometry(QtCore.QRect(100, 250, 500, 50))
          self.jointSizeValueLabel.setObjectName("jointSizeLabel")
          self.jointSizeValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", "10", None, -1))
          
          self.horizontalSlider = QtWidgets.QSlider(self.dockImageButton)
          self.horizontalSlider.setGeometry(QtCore.QRect(150, 250, 300, 50))
          self.horizontalSlider.setMinimum(1)
          self.horizontalSlider.setMaximum(100)
          self.horizontalSlider.setProperty("value", 10)
          self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
          self.horizontalSlider.setObjectName("horizontalSlider")
          self.horizontalSlider.valueChanged.connect(self.jointSizeValueChange)
         
          self.setRootBoneJointBtn = QtWidgets.QPushButton(self.dockImageButton)
          self.setRootBoneJointBtn.setGeometry(QtCore.QRect(0, 320, 150, 50))
          self.setRootBoneJointBtn.setObjectName("setRootBoneBtn")
          self.setRootBoneJointBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Set Root", None, -1))
          self.setRootBoneJointBtn.clicked.connect(self.defineRootBone)
            
          
          self.setRootLineEdit = QtWidgets.QLineEdit(self.dockImageButton)
          self.setRootLineEdit.setGeometry(QtCore.QRect(170, 320, 300, 50))
          self.setRootLineEdit.setObjectName("rootJointLineEdit")
          self.setRootLineEdit.setAlignment(QtCore.Qt.AlignCenter)

          ##
          self.testBtn = QtWidgets.QPushButton(self.dockImageButton)
          self.testBtn.setGeometry(QtCore.QRect(0, 420, 150, 50))
          self.testBtn.setObjectName("setRootBoneBtn")
          self.testBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testA", None, -1))
          self.testBtn.clicked.connect(self.run)


                  
          self.createSlotBtn.setStyleSheet(buttonStyle)             
          self.createBoneBtn.setStyleSheet(buttonStyle)
          self.createBGBtn.setStyleSheet(buttonStyle)
          self.setRootBoneJointBtn.setStyleSheet(buttonStyle)             
          self.setRootLineEdit.setStyleSheet(buttonStyle)             
          self.testBtn.setStyleSheet(buttonStyle)             

          self.createBG_comboBox.setStyleSheet(buttonStyle)
          
     def defineRootBone(self):
          rootBone = cmds.ls(sl=True,typ='joint')
          if len(rootBone) == 1:
               rootBoneName = rootBone[0]
               self.setRootLineEdit.setText(rootBoneName)
               #print rootBone
          else:
               errMsg = 'get root bone'
               print errMsg
          

     def jointSizeValueChange(self):
         
          currentValue = self.horizontalSlider.value() 
         # print currentValue

          self.jointSizeValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", '%s'%currentValue, None, -1))
          
          cmds.jointDisplayScale(currentValue)


     def defineDockCamview(self):
          print ('define DockCameView')
     
          self.spineItemTree = QtWidgets.QTreeWidget(self.dockCamview)
          self.spineItemTree.setGeometry(QtCore.QRect(0, 50, 300, 800))
          self.spineItemTree.setDragEnabled(True)
          self.spineItemTree.setDragDropOverwriteMode(True)
          self.spineItemTree.header().setVisible(False)

          self.spineItemTree.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
          self.spineItemTree.setObjectName("spineItemTree")

     
     
     
     def defineCreateBGBtn(self):
          bgWidth = int(self.createBG_comboBox.currentText().split('x')[0])
          bgHeight = int(self.createBG_comboBox.currentText().split('x')[1])
          print (bgWidth,bgHeight)
          slotPlane = cmds.polyPlane(n='BG_plane',sx=1,sy=1)[0]
          cmds.setAttr('%s.rotateX'%slotPlane,90)
          cmds.setAttr('%s.scaleX'%slotPlane,bgWidth)
          cmds.setAttr('%s.scaleZ'%slotPlane,bgHeight)


     
     def defineCreateBoneBtn(self):
          print ('define bone')
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

     def definecreateSlotBtn(self):
          errMsg = "create Slot fail"
          selectedImageCount = len(self.imageListTable.selectedItems())
          currentImage = self.imageListTable.currentItem().text()
          slotName = currentImage.split('.')[0]
          print (currentImage)
          if selectedImageCount ==0:
              self.errMsgLabel.setText('no selected image')
          else:
               self.errMsgLabel.setText(currentImage)
               imageSize = self.imageInfoTable.item(0,1).text()[1:-1].split(' ')
               fileName = self.imageInfoTable.item(2,1).text()

               imageW = int(imageSize[0])
               imageH = int(imageSize[1])
               slotPlane = cmds.polyPlane(n='%s_#'%slotName,sx=1,sy=1)[0]
               cmds.setAttr('%s.rotateX'%slotPlane,90)
               cmds.setAttr('%s.scaleX'%slotPlane,imageW)
               cmds.setAttr('%s.scaleZ'%slotPlane,imageH)
               
               self.assignSurfaceShader(slotName,slotPlane,fileName)
               print slotPlane
               
       
     
     def defineSlot(self):
          '''
          slotAttr = {'name':'string',
                       'bone':'string',
                       'color':'rgba',
                       'dark':'rgba',
                       'attachment':'strng',
                       'blend':'enum'
                         }
          '''
          
          cmds.addAttr(slot, ln='spineSlot', numberOfChildren=16, attributeType='compound' )
          cmds.addAttr(slot, ln='spine_tag', sn='stag' , dt="string", parent='spineSlot'  )
          cmds.addAttr(slot, ln='slot_name', sn='s_name' , dt="string", parent='spineSlot'  )
          cmds.addAttr(slot, ln='slot_bone', sn='s_bone' , dt="string", parent='spineSlot'  )
          cmds.addAttr(slot, ln='slot_color', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
          cmds.addAttr(slot, ln='slot_red', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_green', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_blue', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_color', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
          cmds.addAttr(slot, ln='slot_red', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_green', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_blue', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_alpha', attributeType='float', parent='slot_color',k=True )
          cmds.addAttr(slot, ln='slot_dark', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
          cmds.addAttr(slot, ln='slot_darkRed', attributeType='float', parent='slot_dark',k=True )
          cmds.addAttr(slot, ln='slot_darkGreen', attributeType='float', parent='slot_dark',k=True )
          cmds.addAttr(slot, ln='slot_darkBlue', attributeType='float', parent='slot_dark',k=True )                
          cmds.addAttr(slot, ln='slot_attachment', sn='s_att' , dt="string", parent='spineSlot'  )
          cmds.addAttr(bone, ln='slot_blend', sn='s_blend' , at="enum",en="normal:additive:multiply:screen", parent='spineSlot' ,k=True )
                       
                                          
     def defineSkin(self):
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
     
     
             
                   
     def assignSurfaceShader(self,imageName,object,fileName):  #imageName  as slot name
          print ('fileName',fileName)
          slotShaderName =  imageName + '_surfaceShader'
          slotFileName = imageName + '_imageFile'
          slotSG = imageName + '_SG'
          if len(cmds.ls(slotShaderName)) == 0:
               print ('slotShaderName is not exist')
               shader=cmds.shadingNode("surfaceShader",asShader=True,n=slotShaderName)
              # shader=cmds.rename(shader,slotShaderName)
               file_node=cmds.shadingNode("file",asTexture=True,n=slotFileName)
               shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n=slotSG)
               cmds.connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_group)
               cmds.connectAttr('%s.outColor' %file_node, '%s.outColor' %shader)
               cmds.connectAttr('%s.outTransparency' %file_node, '%s.outTransparency' %shader)
               cmds.setAttr('%s.fileTextureName'%slotFileName,fileName,type='string')
               cmds.select(object)
               cmds.hyperShade( assign=slotShaderName )
               cmds.select(cl=True)

             #  print ('create shrfaceShader named %s'%slotShaderName)

          elif len(cmds.ls(slotShaderName)) == 1:
               
               print ('%s is exist'%slotShaderName)
               cmds.select(object)
               cmds.hyperShade( assign=slotShaderName )
               cmds.select(cl=True)

        
   
          
          
     
     def defineImageInfoDock(self):
          #folderDir = "C:/Users/alpha/Documents/GitHub/mayaTool/pipelineTool/UI"

          images = self.getImagesInFolder()
          self.createImageTable(images,50)
          self.createImageInfoTable()
          #self.createImagePreviewTable()

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

       
     def getImagesInFolder(self):
          "define image folder"
          files = os.listdir(self.folderDir)
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
     
     
     def definePreviewImageDock(self):
          self.createPreviewPannel()
          
          

     def createPreviewPannel(self):
         # imageUrl = self.folderDir + '/' + self.imageListTable.currentItem().text()
          self.imagePreviewLabel = QtWidgets.QLabel(self.previewImageDock)
          self.imagePreviewLabel.setGeometry(QtCore.QRect(10, 50, 280, 280))
          self.imagePreviewLabel.setStyleSheet("background-color:#333333;\
                                                  border-radius:10px;\
                                                  border-style:solid;\
                                                  border-width:3px;\
                                                  border-color:#5E749C")
          self.imagePreviewLabel.setText("")
          self.imagePreviewLabel.setPixmap(QtGui.QPixmap())
          self.imagePreviewLabel.setScaledContents(True)
          self.imagePreviewLabel.setObjectName("imagePreview")



          
      
          
          
          
     
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
         
          
          
          
          
          
     def createImageTable(self,images,iconWidth):
          self.imageListTable = QtWidgets.QTableWidget(self.dockWidgetImages)
          imagesCount = len(images)
          columnCount = 5
          columnWidth = iconWidth
          rowCount = int(math.ceil(float(len(images))/float(columnCount)))
          rowHeight = columnWidth
          
          self.imageListTable.setGeometry(QtCore.QRect(10, 50,(columnCount*columnWidth+30), 500+30))

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
               imageUrl = self.folderDir +'/'+ itemName
               iconFile =QtGui.QIcon(imageUrl)
               row = math.floor(float(i)/float(columnCount))
               column = i%columnCount
            #   print images[i]
               self.imageListTable.setIconSize(QtCore.QSize(columnWidth,columnWidth))

               self.imageListTable.setItem(row,column,item)
               
               self.imageListTable.item(row, column).setIcon(iconFile)
               self.imageListTable.item(row, column).setText(QtWidgets.QApplication.translate("MainWindow",'%s'%itemName, None,-1))

          self.imageListTable.setStyleSheet(" border: 3px solid #5E749C;\
                                             color:white;\
                                             text-align: top;\
                                             padding: 4px;\
                                             border-radius: 7px;\
                                             position: absolute;\
                                             border-bottom-left-radius: 7px;\
                                             width: 15px");
                                             

                                                                                               
          self.imageListTable.itemClicked.connect(self.imageInfo)

          
          
          

     def imageInfo(self):
         # print 'asss'
          
         # print self.imageListTable.currentItem().text()
          
          imageUrl = self.folderDir + '/' + self.imageListTable.currentItem().text()
          #print imageUrl
          
          image = ice.Load(imageUrl)
          imageMetaData = image.GetMetaData()
         # print imageMetaData.keys(),len(imageMetaData.keys())

          self.defineImageTableData(imageMetaData)
          self.imagePreviewLabel.setPixmap(QtGui.QPixmap(imageUrl))

         # item = QtWidgets.QTableWidgetItem()
        #  self.imagePreviewTable.setItem(0,0,item)
         # iconFile =QtGui.QIcon(imageUrl)
        #  self.imagePreviewTable.setIconSize(QtCore.QSize(270,270))
        #  self.imagePreviewTable.item(0, 0).setIcon(iconFile)
#

     def run(self):
          print ("export json")
          boneList = self.defineBone('joint19')
          print (boneList)

     def defineBone(self,root):
         
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
                      oy = float("%.3f"%(cmds.getAttr("%s.jointOrientY"%i)))
                      oz = float("%.3f"%(cmds.getAttr("%s.jointOrientZ"%i)))
                      r  = oz+rz
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
                          boneInfo = {"name":i,"parent":parentBone,"rotation":r,"x":x,"y":y,"length":length,"color":"ffffffff"}

             
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
                     
      


     def defineExportData(self):
          
          exportFile = "C:/Users/alpha/Documents/GitHub/spineToolAdv/test_01.json"
          exportData = {'skeleton':{},
                         'bones':[],
                         'slots':[],
                         'skins':{},
                         'events':{},
                         'animations':{}          
          }
          
          



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

