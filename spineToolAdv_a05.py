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

import os,math,json
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
        self.folderDir = 'C:/Temp/images'  #'C:/Temp/testImage'
          
          
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
        self.errMsgLabel.setGeometry(QtCore.QRect(0, 30, 500, 50))
        self.errMsgLabel.setObjectName("errMsgLabel")
        self.errMsgLabel.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))


        self.createRootBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createRootBtn.setGeometry(QtCore.QRect(0, 100, 150, 50))
        self.createRootBtn.setObjectName("createRoot")
        self.createRootBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Root", None, -1))
        self.createRootBtn.clicked.connect(self.createRootCtrl)




        self.createSlotBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createSlotBtn.setGeometry(QtCore.QRect(0, 170, 150, 50))
        self.createSlotBtn.setObjectName("createSlot")
        self.createSlotBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Slot", None, -1))
        self.createSlotBtn.clicked.connect(self.definecreateSlotBtn)

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



        self.defineMeshBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.defineMeshBtn.setGeometry(QtCore.QRect(0, 240, 150, 50))
        self.defineMeshBtn.setObjectName("defineMesh")
        self.defineMeshBtn.setText(QtWidgets.QApplication.translate("MainWindow", "define Mesh", None, -1))
        self.defineMeshBtn.clicked.connect(self.getSkinData)





        self.createBoneBtn = QtWidgets.QPushButton(self.dockImageButton)
        self.createBoneBtn.setGeometry(QtCore.QRect(170, 240, 150, 50))
        self.createBoneBtn.setObjectName("createBone")
        self.createBoneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Bone", None, -1))
        self.createBoneBtn.clicked.connect(self.defineCreateBoneBtn)


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
        self.testBBtn.setGeometry(QtCore.QRect(200, 520, 150, 50))
        self.testBBtn.setObjectName("setRootBoneBtn")
        self.testBBtn.setText(QtWidgets.QApplication.translate("MainWindow", "testB", None, -1))
        self.testBBtn.clicked.connect(self.defineAllItemInRootCtrl)

        self.createRootBtn.setStyleSheet(buttonStyle)     

        self.createSlotBtn.setStyleSheet(buttonStyle)     
        self.createMeshBtn.setStyleSheet(buttonStyle)             
        self.createClippingBtn.setStyleSheet(buttonStyle)             




        self.defineMeshBtn.setStyleSheet(buttonStyle)

        self.createBoneBtn.setStyleSheet(buttonStyle)
        self.createBGBtn.setStyleSheet(buttonStyle)
        self.setRootBoneJointBtn.setStyleSheet(buttonStyle)             
        self.setRootLineEdit.setStyleSheet(buttonStyle)             
        self.testABtn.setStyleSheet(buttonStyle)             
        self.testBBtn.setStyleSheet(buttonStyle)             




        self.createBG_comboBox.setStyleSheet(buttonStyle)


          
          
    def createRootCtrl(self):
        errMsg = "create Root Ctrl"
          
        ctrlScale = 10
        points = [(0,2*ctrlScale,0),(6*ctrlScale,2*ctrlScale,0),(6*ctrlScale,3*ctrlScale,0),(9*ctrlScale,0,0),(6*ctrlScale,-3*ctrlScale,0),(6*ctrlScale,-2*ctrlScale,0),(0,-2*ctrlScale,0),(-6*ctrlScale,-2*ctrlScale,0),(-6*ctrlScale,-3*ctrlScale,0),(-9*ctrlScale,0,0),(-6*ctrlScale,3*ctrlScale,0),(-6*ctrlScale,2*ctrlScale,0),(0,2*ctrlScale,0)]

        curve = cmds.curve(d=1,p=points)     
          
          
        cmds.addAttr(curve, ln='spineRootCtrl', numberOfChildren=2, attributeType='compound' )
        cmds.addAttr(curve, ln='spine_tag', sn='stag' , dt="string", parent='spineRootCtrl'  )

        cmds.addAttr(curve, ln='spine_rootCtrl', sn='rootCtrl' , dt="string", parent='spineRootCtrl'  )
          
        cmds.setAttr('%s.spine_tag'%curve,'spine_ctrl',type='string')

        cmds.rename(curve,'rootCtrl')
     
          
               
                    
                         
    #### ¿é¥X     
    def defineDeformAnimation(self,meshName):
        
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
                                                        
    def defineAllItemInRootCtrl(self):
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

        allItemsInRootCtrl = cmds.listRelatives( rootCtrlName, c=True,ad=True )


        allItems = cmds.listRelatives( 'rootCtrl', c=True,ad=True)

        for i in allItems:
            #  print i, cmds.nodeType(i)
            if cmds.nodeType(i) == 'transform':
                itemsInTransformNode = cmds.listRelatives(i,c=True,s=True,ni=True)
                if len(itemsInTransformNode) > 1:
                        errMsg = "more than one obj in transform node"
                if len(itemsInTransformNode) == 1:
                        if cmds.nodeType(itemsInTransformNode[0]) == "mesh":
                            errMsg = "define %s as slot"%itemsInTransformNode[0]
                            #slot = i
                            meshSlotList.append(i)
                    
          
          
        for i in allItemsInRootCtrl:
            ###check duplicated name object
            items = cmds.ls(i)
            if len(items) >1:
                errmsg = "duplicated items"
               
            else:
                #print cmds.nodeType(i)
                
                if cmds.nodeType(i) == "mesh":
                    try:
                              
                        if cmds.getAttr('%s.spine_skinType'%i) == "mesh":
                            allMeshItem.append(i)
                    except:
                        pass
              # print i,cmds.nodeType(i)
          
          #self.defineExportData(boneList,skinDict)
        for i in meshSlotList: ## define all mesh's slot
        #   print cmds.ls(i)
            self.defineSlot(i,rootCtrlName) 
          
          
        for i in allMeshItem:
            print 'allMeshItem',i
            skinData = json.loads(cmds.getAttr('%s.spine_skinData'%i))
            # skinDict.update(skinData)
            skinDict["default"].update(skinData)
        #  exportFile = "C:/Users/alpha/Documents/GitHub/spineToolAdv/test_01.json" 
          #print errMsg,skinDict
          #print allSlotItem
        slotList = self.getAllMeshSlots(meshSlotList)

        self.defineExportData(boneList,skinDict,slotList)

         # print slotList
          
          

          
        
    def defineRootBone(self):
        rootBone = cmds.ls(sl=True,typ='joint')
        if len(rootBone) == 1:
            rootBoneName = rootBone[0]
            self.setRootLineEdit.setText(rootBoneName)
            #print rootBone
        else:
            errMsg = 'get root bone'
            print errMsg
      
    def definecreateMesh(self):
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
        slotList = []
        for i in meshSlotList:
            slotName = cmds.getAttr('%s.slot_name'%i)
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
        'meshName,borderEdges'
        meshName = cmds.ls(sl=True,dag=2,typ='mesh')[0]
          
        cmds.addAttr(meshName, ln='spineSlot', numberOfChildren=7, attributeType='compound' )
        cmds.addAttr(meshName, ln='spine_tag', sn='stag' , dt="string", parent='spineSlot')
        cmds.addAttr(meshName, ln='spine_skinType', sn='skinType' , dt="string", parent='spineSlot')

        cmds.addAttr(meshName, ln='spine_slotName', sn='slotName' , dt="string", parent='spineSlot')
        cmds.addAttr(meshName, ln='spine_skinName', sn='skunName' , dt="string", parent='spineSlot')
        cmds.addAttr(meshName, ln='spine_attachmentName', sn='attachName' , dt="string", parent='spineSlot')
        cmds.addAttr(meshName, ln='spine_boneName', sn='boneName' , dt="string", parent='spineSlot')
        cmds.addAttr(meshName, ln='spine_skinData', sn='skinData' , dt="string", parent='spineSlot')


     

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
          
          
               
        
          
          
        slotName = meshName
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
        print "meshName",meshName
         
        shadingGrps = cmds.listConnections(meshName ,type='shadingEngine')
          
        print shadingGrps
         
          
 
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
         
         currentFile = cmds.getAttr("%s.fileTextureName" % fileNode)
         fileInSlot = currentFile.split("/")[-1].split(".png")[0]
         image = ice.Load(currentFile)
         imageMetaData = image.GetMetaData()
         imageSize = imageMetaData['Original Size']
         imageWidth = int(imageMetaData['Original Size'].split(" ")[0].split("(")[1])
         imageHeight = int(imageMetaData['Original Size'].split(" ")[1].split(")")[0])

         return currentFile,imageWidth,imageHeight




                                                                           

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
            imageSize = self.imageInfoTable.item(10,1).text()[1:-1].split(' ')
            fileName = self.imageInfoTable.item(2,1).text()

            imageW = int(imageSize[0])
            imageH = int(imageSize[1])
            slotPlane = cmds.polyPlane(n='%s_#'%slotName,sx=1,sy=1)[0]
            cmds.setAttr('%s.rotateX'%slotPlane,90)
            cmds.setAttr('%s.scaleX'%slotPlane,imageW)
            cmds.setAttr('%s.scaleZ'%slotPlane,imageH)

            self.assignSurfaceShader(slotName,slotPlane,fileName)
            print slotPlane
               
      
    def defineSelectObj(self):
          
        currentTarget = cmds.ls(sl=True,typ='transform')[0]
     
        self.defineSlot(currentTarget)
        self.defineSkin(currentTarget)
          
          
          
          
          
          
          
          
    def defineSlot(self,slot,boneName):

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
            slotName = slotList[0]
        cmds.setAttr('%s.spine_tag'%slot,'spine_slot',type='string')
        cmds.setAttr('%s.slot_name'%slot,slotName,type='string')
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
                     
      


    def defineExportData(self,boneList,skinDict,slotList):
          
        exportFile = "C:/Temp/images/test_01.json"
        exportData = {'skeleton':{},
                         'bones':boneList,
                         'slots':slotList,
                         'skins':skinDict,
                         'events':{},
                         'animations':{}          
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

