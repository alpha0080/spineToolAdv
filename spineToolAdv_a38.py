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
import getpass

import datetime
import time

from time import gmtime,strftime

#from PySide2.QtCore import QString
import os,math,json,shutil
import sys,subprocess
try:
    sys.path.append("C:/Users/alpha/Documents/GitHub/spineToolAdv")
    import spineUI_A
    reload(spineUI_A)
except:
    pass


try:
    sys.path.append("//mcd-one/database/assets/scripts/python2.7_alpha/22")
except:
    sys.path.append("C:/Program Files/Pixar/RenderManProServer-22.1/lib/python2.7/Libs/ite-packages")
import ice

try:    
    import psycopg2
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
        fontSize = 12
          #initial data
       # self.folderDir = '//mcd-3d/data3d/spine_imageSources'  #'C:/Temp/testImage'
        self.imagesFilter = ['jpg','JPG','png','PNG']



        spineUI_A.buildDock(self)
        spineUI_A.defineImageButtonDock(self,fontSize)
        

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
         
        self.trimBeforeFrameBtn.clicked.connect(self.trimBeforeFrame)
        self.trimAfterFrameBtn.clicked.connect(self.trimAfterFrame)
        self.trimBetweenFrameBTN.clicked.connect(self.trimBetweenFrame)
        self.alignToFrameBtn.clicked.connect(self.alignKeys)
        self.scaleTimeBtn.clicked.connect(self.scaleFrames)
        self.loopTimeBtn.clicked.connect(self.loopFrames)
        self.defineSelectObjBtn.clicked.connect(self.getSelectSlotBone)
        self.selectAnyTransform.clicked.connect(self.getSelectAnyTransform)
        self.renameAllSelectBtn.clicked.connect(self.renameSelectedBone)
        self.fillet_odd_btn.clicked.connect(self.optionalSelect)
        self.fillet_even_btn.clicked.connect(self.optionalSelect)
        self.fillet_n1_btn.clicked.connect(self.optionalSelect)
        self.fillet_n2_btn.clicked.connect(self.optionalSelect)
        self.fillet_n3_btn.clicked.connect(self.optionalSelect)
        self.fillet_n4_btn.clicked.connect(self.optionalSelect)
        self.fillet_n5_btn.clicked.connect(self.optionalSelect)
        self.fillet_n6_btn.clicked.connect(self.optionalSelect)
        self.fillet_n7_btn.clicked.connect(self.optionalSelect)
        self.fillet_n8_btn.clicked.connect(self.optionalSelect)
        self.fillet_n9_btn.clicked.connect(self.optionalSelect)
        self.fillet_n0_btn.clicked.connect(self.optionalSelect)
        self.setModAllFrameBTN.clicked.connect(self.setFrameFilletToAll)
        self.setModFirstFrameBTN.clicked.connect(self.setFrameFilletToFirst)
        self.setModLastFrameBTN.clicked.connect(self.setFrameFilletToLast)
        self.modReplaceModBtn.clicked.connect(self.changeRelaceMode)
        self.modOffsetBtn.clicked.connect(self.changeOffsetMode)
        self.modTransXBtn.clicked.connect(self.defineModX)
        self.modTransYBtn.clicked.connect(self.defineModY)
        self.modTransZBtn.clicked.connect(self.defineModZ)
        self.modRotateXBtn.clicked.connect(self.defineModRX)
        self.modRotateYBtn.clicked.connect(self.defineModRY)
        self.modRotateZBtn.clicked.connect(self.defineModRZ)
        self.modScaleXBtn.clicked.connect(self.defineModSX)
        self.modScaleYBtn.clicked.connect(self.defineModSY)
        self.modScaleZBtn.clicked.connect(self.defineModSZ)
        self.modScaleAllBtn.clicked.connect(self.defineModSAll)
        self.modAlphaGainBtn.clicked.connect(self.defineModAlpha)
        self.modColorBtn.clicked.connect(self.createRootCtrl)
        self.modFadeBtn.clicked.connect(self.createRootCtrl)
        self.selectImageFolderBtn.clicked.connect(self.setImageSourceToDatabase)
        self.selectImageFromDiskBTN.clicked.connect(self.setToDisk)
        self.selectSpineJobBtn.clicked.connect(self.setToSpineJobTree)
        self.openSelectedFolderBtn.clicked.connect(self.openSelectedFolder)
        self.spineItemTree.itemClicked.connect(self.defineImageTableFromSel)
        self.openSpineMayaFileBtn.clicked.connect(self.openMayaFile)
        self.selectSpineWorkSpaceBtn.clicked.connect(self.defineSpineWorkSpace)
        self.OpenSpineDirBtn.clicked.connect(self.openSpineFolder)
        self.OpenImageDirBtn.clicked.connect(self.openImagesFolder)
        self.OpenExportDirBtn.clicked.connect(self.openExportFolder)
        self.createBGBtn.clicked.connect(self.defineCreateBGBtn)
        self.copyBoneKey.clicked.connect(self.copyKeyToSelectBone)
        self.pastedBoneKey.clicked.connect(self.pasteKeyToSelectBone)
        
        self.initialSpineRootBtn.clicked.connect(self.defineSpineRootSkeleton)
        self.createCharacterGrpBTn.clicked.connect(self.createCharacterGrp)
        self.createRootBtn.clicked.connect(self.createRootCtrl)
        self.createImagePlaneBtn.clicked.connect(self.createImagePlane)
        self.defineMeshBtn.clicked.connect(self.getSkinData)
        self.createSlotBtn.clicked.connect(self.createSlot) 
        self.duplicateSlotBtn.clicked.connect(self.duplicateSlot) 
        self.characterCreateBtn.clicked.connect(self.switchToCharacterMode)
        self.defineSpineBoneBtn.clicked.connect(self.switchToSlotMode)
        self.defineSpineMaskBtn.clicked.connect(self.switchToMaskMode)
                                 
                                                       
        self.createBoneBtn.clicked.connect(self.createCleanBone)
        self.selectExportFileBTn.clicked.connect(self.defineExportFileName)
        self.exportToSpineFileBtn.clicked.connect(self.exortTOSpineJson)              
        self.setSlotColor.clicked.connect(self.setColorToSelectBone)
        self.setSlotColorKey.clicked.connect(self.setSlotColorKeyFrame)
        self.setNewSlot.clicked.connect(self.setSlotNewImage)
             
         
        self.amountSlotSlider.valueChanged.connect(self.slotAmountSliderChange)
        self.amountSliderNumLEdit.textChanged.connect(self.slotAmountEditChange)
        self.jontSizeLEdit.valueChanged.connect(self.jointSizeValueChange)
        self.vertexSizeSB.valueChanged.connect(self.vertexSizeChange)
                     
         
        self.openMayaFileFolder.clicked.connect(self.openMayaFileHstory)   
        self.saveMayaFileBtn.clicked.connect(self.saveMayaFile)      
        self.saveMayaFileDialogBtn.clicked.connect(self.selectSaveFile)      
        self.mayaRecentFileTable.itemClicked.connect(self.fileOpenItemClick)
   
        
    def switchToCharacterMode(self):
        print "switchToCharacterMode"
        self.defineSpineSlotBoneGrpBox.setVisible(False)
        self.defineClippedGrpBox.setVisible(False)
        self.characterCreateBtn.setChecked(True)
        self.defineSpineBoneBtn.setChecked(False)
        self.defineSpineMaskBtn.setChecked(False)

    def switchToSlotMode(self):
        print "switchToSlotMode"
        self.defineSpineCharacterGrpBox.setVisible(True)
        self.defineSpineSlotBoneGrpBox.setVisible(True)
        self.defineClippedGrpBox.setVisible(False)

        self.characterCreateBtn.setChecked(False)
        self.defineSpineBoneBtn.setChecked(True)
        self.defineSpineMaskBtn.setChecked(False)
 
    def switchToMaskMode(self):
        print "switchToSlotMode"
        self.defineSpineCharacterGrpBox.setVisible(True)
        self.defineClippedGrpBox.setVisible(True)
        self.defineSpineSlotBoneGrpBox.setVisible(False)

        self.characterCreateBtn.setChecked(False)
        self.defineSpineBoneBtn.setChecked(False)
        self.defineSpineMaskBtn.setChecked(True)       
        
     
        
    def defineMask(self):
        print "defineMask"
        '''
        "skins": {
        "default": {
		"clipping": {
			"clipping": {
				"type": "clipping",
				"end": "dust",
				"vertexCount": 9,
				"vertices": [ 66.76, 509.48, 19.98, 434.54, 5.34, 336.28, 22.19, 247.93, 77.98, 159.54, 182.21, -97.56, 1452.26, -99.8, 1454.33, 843.61, 166.57, 841.02 ],
				"color": "ce3a3aff"
			}
		},
        '''      
                 
                       
        
    def fileOpenItemClick(self ):
        print "fileOpenItemClick"
        
        fileName =  self.spineWorkSpaceLEdit.text() + self.mayaRecentFileTable.currentItem().text()
        self.mayaRecentFileTable.itemDoubleClicked.connect(lambda x:self.openMayaSpineFile(fileName))
       # lambda x:self.imageInfo(currentFolder)
    def openMayaSpineFile(self,fileName):
        print "openMayaSpineFile",fileName
        try:
            cmds.file(fileName,open=True,f=True)     
            self.initialSpineItemTree()
            self.mayaFileHistoryGrp.setVisible(False)
        except:
            self.errorMsgLEdit.setTet('file %s error'%fileName)
                                      
    def selectSaveFile(self):
        print "selectSaveFile"
        basicFilter = "*.mb"
        fullFileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2)[0]
        self.saveMayaFileLEdit.setText(fullFileName)

          
    def openMayaFileHstory(self):
        print "openMayaFileHstory"
        
        login = getpass.getuser()    
        self.mayaFileHistoryGrp.setVisible(True)
        
        #self.mayaRecentFileTable
            
        conn3 = psycopg2.connect(database='3D_db', user= 'postgres', password= '', host= '192.168.161.193', port= '5432')
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT * FROM spine_maya")
        tempSpineMayaData = cursor3.fetchall()
        spineMayaData = list((sorted(tempSpineMayaData, key = lambda x: x[0],reverse=True)))
        spineMayaDataByUser = filter(lambda x:x[1] == login ,spineMayaData)
        #cursor3.execute( "UPDATE shots set icon_url = '%s' where name = '%s';" % ( iconURL, itemName))
        
        conn3.commit()
        conn3.close() 
        fileCount = len(spineMayaDataByUser)
        self.mayaRecentFileTable.setRowCount(0)
        self.mayaRecentFileTable.setColumnCount(0)        

        self.mayaRecentFileTable.setRowCount(10)
        self.mayaRecentFileTable.setColumnCount(2)
        for i in range(0,fileCount):
            self.mayaRecentFileTable.setColumnWidth(0, 20)
            self.mayaRecentFileTable.setColumnWidth(1, 505)
            #self.mayaRecentFileTable.setColumnWidth(2, 1)

            self.mayaRecentFileTable.setRowHeight(i, 30) 
            fileName = spineMayaDataByUser[i][0].split('/')[-1]
            fileUrl = spineMayaDataByUser[i][0]
            self.mayaRecentFileTable.setItem(i,1,QtWidgets.QTableWidgetItem())
            self.mayaRecentFileTable.item(i, 1).setText(QtWidgets.QApplication.translate("MainWindow",fileName, None,-1))
            #self.mayaRecentFileTable.setItem(i,2,QtWidgets.QTableWidgetItem())
            #self.mayaRecentFileTable.item(i, 2).setText(QtWidgets.QApplication.translate("MainWindow",fileUrl, None,-1))

        print spineMayaDataByUser    
        
                   
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
        currentSceneFile = cmds.file(q=True, sn=True)
        if len(currentSceneFile) == 0:
            pass
        else:
            fileName = currentSceneFile.split('/')[-1]
            fileDir = currentSceneFile.split(fileName)[0]
            spineImageDir = fileDir + 'images'
            spineExportDir =  fileDir + 'export'
            print fileName,fileDir
            #cmds.file(fileName,open=True,f=True)
            self.openMayaFileLEdit.setText(fileName)
            self.spineWorkSpaceLEdit.setText(fileDir)
            self.spineImagesSpaceLEdit.setText(spineImageDir)
            self.spineExportSpaceLEdit.setText(spineExportDir)
           # exportFolder = self
            exportFileName = spineExportDir + '/' + fileName.split('.')[0] + "_spineExport.json"
            self.selectExportFileBTnLEdit.setText(exportFileName)
            
            try:
                os.mkdir(spineImageDir)
            except:
                pass
            try:
                os.mkdir(spineExportDir)
            except:
                pass
            
                
        saveFileName = fileName.split('.mb')[0].split('_')[-2]
        print 'fileName__',fileName,saveFileName,fileDir
        
        try:
            
          #  saveFileName = fileName.split('.mb')[0].spiit('_')[-2]
            

          #  currentFileName = fileName
            
            
            print 'os.path.isfile(fileNameLong)', saveFileName
            
            verIndexList = []
            print 'fileDIr______3 ', os.listdir(fileDir)
            for i in os.listdir(fileDir):
                fileNameLong = fileDir +i
                print 'fileNameLong',fileNameLong
                
                if os.path.isfile(fileNameLong) == True:
                    if i.split('.')[-1] == "mb":
                        if len(i.split('_')[-2]) ==4:
                            if i.split('_')[-2][0] == 'v':
                                versionNum = i.split('_')[-2].split('v')[1]
                                #versionNum = int(i.split('v')[1])
                                print versionNum
                                if versionNum in verIndexList:
                                    pass
                                else:
                                    verIndexList.append(versionNum)
                                    
            verIndexList = sorted(verIndexList)
            nextIndexNum = int(verIndexList[-1]) +1
            nextIndexNumString = 'v'+str('{0:03d}'.format(nextIndexNum))
            tempNewFileName = ""     
            for i in fileName.split('.mb')[0].split('_')[0:-2]:
                tempNewFileName += i + '_'
                
            newSaveFileName =  tempNewFileName + nextIndexNumString  +'_'+ fileName.split('.mb')[0].split('_')[-1]+'.mb'               
            
          
        except:
            newSaveFileName = fileName
        
        self.saveMayaFileLEdit.setText(newSaveFileName)
                        
                                

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




    def openMayaFile(self):
        print "openMayaFile"
        basicFilter = "*.mb"
        fullFileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2,fm=1)[0]
        fileName = fullFileName.split('/')[-1]
        fileDir = fullFileName.split(fileName)[0]
        spineImageDir = fileDir + 'images'
        spineExportDir =  fileDir + 'export'
        print fileName,fileDir
        cmds.file(fileName,open=True,f=True)
        self.openMayaFileLEdit.setText(fileName)
        self.spineWorkSpaceLEdit.setText(fileDir)
        self.spineImagesSpaceLEdit.setText(spineImageDir)
        self.spineExportSpaceLEdit.setText(spineExportDir)
       # exportFolder = self
        exportFileName = spineExportDir + '/' + fileName.split('.')[0] + "_spineExport.json"
        self.selectExportFileBTnLEdit.setText(exportFileName)
        
        try:
            os.mkdir(spineImageDir)
        except:
            pass
        try:
            os.mkdir(spineExportDir)
        except:
            pass
            

    def saveMayaFile(self):
        print "saveMayaFile"
        
        dir = self.spineWorkSpaceLEdit.text()
        file_name = dir + self.saveMayaFileLEdit.text()
        login = getpass.getuser()    
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        cmds.file( rename= file_name )
        cmds.file( save=True, type='mayaBinary' )

        print file_name,login,timestamp
         
        try:   
            conn3 = psycopg2.connect(database='3D_db', user= 'postgres', password= '', host= '192.168.161.193', port= '5432')
            cursor3 = conn3.cursor()

            inputData = (file_name,login,timestamp)
            cursor3.execute("INSERT INTO spine_maya (file_name,login,timestamp) VALUES('%s','%s','%s')"%inputData)

            conn3.commit()
            conn3.close() 
        except:
            pass


        self.initialWorkSpace()

    def setSlotNewImage(self):
        print "setSlotNewImage"
        currentImage = self.imageListTable.currentItem().text()
        imageName = currentImage.split('.')[0]
        fileName = self.imageInfoTable.item(0,1).text()
        
        targetFileName = self.spineImagesSpaceLEdit.text() +'/' +currentImage
        imageW = int(self.imageInfoTable.item(3,1).text())
        imageH = int(self.imageInfoTable.item(4,1).text())
        
        ###create new shader
        slotShaderName =  imageName + '_shader'
        slotFileName = imageName + '_imageFile'
        slotSG = imageName + '_SG'
        selectJointList = cmds.ls(sl=True,type='joint')
        cmds.select(cl=True) 

        shader = cmds.shadingNode("lambert",asShader=True,n=slotShaderName)
       # print 'shader',shader
        cmds.select(shader)
        shaderName = cmds.ls(sl=True)[0]
            # shader=cmds.rename(shader,slotShaderName)
       #     print 'shaderName',shaderName,shader
        file_node=cmds.shadingNode("file",asTexture=True,n=slotFileName)
        shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n=slotSG)
        cmds.connectAttr('%s.color' %shader ,'%s.surfaceShader' %shading_group)
        cmds.connectAttr('%s.outColor' %file_node, '%s.color' %shader)
           # print 'fileName',fileName
        
    
        cmds.connectAttr('%s.outTransparency' %file_node, '%s.transparency' %shader)
        cmds.setAttr('%s.fileTextureName'%slotFileName,fileName,type='string')
        cmds.select(cl=True) 

        selectBoneList = filter(lambda x: cmds.getAttr('%s.spine_tag'%x)== 'spine_bone' ,selectJointList)
        print "currentFile",fileName,targetFileName
        try:
            if os.path.isfile(targetFileName) == True:
                print "file exist"
                
            else:
                #os.remove(targetFile)
                shutil.copyfile(fileName,targetFileName)        
        
        except:
                       
            pass
        cmds.setAttr('%s.fileTextureName'%slotFileName,targetFileName,type='string')

        for bone in selectBoneList:
            slotName = cmds.getAttr('%s.bone_slot'%bone)
            print 'slotName',slotName
            cmds.select(slotName)
            cmds.hyperShade( assign=slotShaderName )
            cmds.setAttr('%s.scaleX'%slotName,imageW)
            cmds.setAttr('%s.scaleZ'%slotName,imageH)
            cmds.setAttr('%s.slot_width'%slotName,imageW)
            cmds.setAttr('%s.slot_height'%slotName,imageH)
            cmds.setAttr('%s.slot_width'%bone,imageW)
            cmds.setAttr('%s.slot_height'%bone,imageH)

            cmds.setAttr('%s.slot_attachment'%slotName,imageName,type="string")

            cmds.select(cl=True) 
        print 'currentImage',currentImage,fileName,selectBoneList
        
    def setSlotColorKeyFrame(self):
        print "setSlotColorKeyFrame"
        selectJointList = cmds.ls(sl=True,type='joint')
        selectBoneList = filter(lambda x: cmds.getAttr('%s.spine_tag'%x)== 'spine_bone' ,selectJointList)
        for bone in selectBoneList:
            
            cmds.setKeyframe(bone, at='slot_red')
            cmds.setKeyframe(bone, at='slot_green')
            cmds.setKeyframe(bone, at='slot_blue')

        #print 'selectBoneList',selectBoneList


    def setColorToSelectBone(self):
        print "setColorToSelectBone"
        color = QtWidgets.QColorDialog.getColor()
       # self.testLabel.setAutoFillBackground(True)
       # print color,type(color),dir(color)
       # print color.redF(),color.blueF()
        selectJoint = cmds.ls(sl=True,type='joint')
        sampleBone = selectJoint[0]
        sampleMesh = cmds.getAttr('%s.bone_slot'%sampleBone)
        
        
        getObj =  cmds.ls(sampleMesh,dag=1)[1]
        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
        #currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
        cmds.setAttr('%s.colorGain'%fileNode, color.redF(), color.greenF(), color.blueF(), type="double3")
        #print 'currentFile',currentFile
      #  selectBone = []
        for i in selectJoint:
            if cmds.getAttr('%s.spine_tag'%i) == 'spine_bone':
                #selectBone.append(i)
                cmds.setAttr('%s.slot_red'%i,float(color.redF()))
                cmds.setAttr('%s.slot_blue'%i,float(color.blueF()))
                cmds.setAttr('%s.slot_green'%i,float(color.greenF()))

       # print selectBone
     #   if color.isValid():
     #       palette = self.testLabel.palette()
        #    palette.setColor(QtGui.QPalette.Background, color)
        #    self.testLabel.setPalette(color)
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
        objList = self.getObjList()
        alignFrame = int(float(self.alignToFrameLEdit.text()))
        print 'alignFrame',alignFrame
       # print objList
        
        for obj in objList:
         #   print obj
          #  keyFrameList= []
            tempKeyFrameList = cmds.keyframe(obj,q=True)
            

            tempKeyFrameList = sorted(tempKeyFrameList)
            firstKey = tempKeyFrameList[0]
            LastKey = tempKeyFrameList[-1]
            cmds.cutKey( obj, time=(firstKey,LastKey))
            cmds.pasteKey( obj, time=(alignFrame,))   
            
            
            
            
    
                    
                    
                    
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
    

    def openSpineFolder(self):
        print "openSpineFolder"
        dir = self.spineWorkSpaceLEdit.text()

        currentProjWin =''   
        for cha in dir:
            if cha =="/":
                currentProjWin += '\\'
            else:    
                currentProjWin += cha 
        openCmd = "explorer "+'%s'%currentProjWin
        subprocess.call(openCmd)

    def openImagesFolder(self):
        print "openImagesFolder"
        dir = self.spineImagesSpaceLEdit.text()

        currentProjWin =''   
        for cha in dir:
            if cha =="/":
                currentProjWin += '\\'
            else:    
                currentProjWin += cha 
        openCmd = "explorer "+'%s'%currentProjWin
        subprocess.call(openCmd)       
         
    def openExportFolder(self):
        print "openExportFolder"
        dir = self.spineExportSpaceLEdit.text()

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
        
        exportFileName = exportFolder + '/' + "spineExport.json"
        self.selectExportFileBTnLEdit.setText(exportFileName)
        
        
        
    
    
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
                            cmds.parent(curve,currentSet)
                            self.errorMsgLEdit.setText('Root %s created'%rootName)
                    
                else:
                    self.errorMsgLEdit.setText('%s is not spine Character Set'%currentSet[0])
            except:
                self.errorMsgLEdit.setText('%s is not character set'%currentSet[0])
               # self.errorMsgLEdit.setText('%s is not spine Character Set'%currentSet[0])
                
                

       # characterSet = 
        '''      
        
        
        '''
          
   



    def exortTOSpineJson(self): #regionSlot
        print "exortTOSpineJson"
        cmds.currentTime(0,e=True)
        errMsg = "define all items in root ctrl"
        rootCtrlName = self.exportSpineRootLabelLEdit.text()
        fileName = self.selectExportFileBTnLEdit.text()
        characterSetGrp =[]
        #boneList = [{ "name":rootCtrlName}]
        allMeshItem = []
        meshSlotList = []
        tempAllBoneList = []
        allCharacterSetList =[]
        #skinDict = {"default":{}}
        allObjInRootCtrl = cmds.listRelatives(rootCtrlName,c=True)
        print 'rootCtrlName',rootCtrlName
        for i in allObjInRootCtrl:
            if cmds.getAttr('%s.spine_tag'%i) == "spine_characterSet":
                characterSetGrp.append(i)
        ### check if bone/joints in spineRootSkeleton
            
        allJointInRootCtrl = cmds.listRelatives(rootCtrlName,ad=True,type="joint") 
        try:
            jointsCount = len(allJointInRootCtrl)
        except:
            print "no joints in spine_rootSkeleton"
            jointsCount = 0
            
        if jointsCount == 0:
            boneList = [{ "name":rootCtrlName}]
            skinDict= {"default":{}}
            slotList = []
       
            allBoneList = []
            pass
        else:
            depthList = []
            for i in allJointInRootCtrl:
                try:
                    if cmds.getAttr('%s.spine_tag'%i) == "spine_bone":
                        tempAllBoneList.append(i) 
                        depth = len(cmds.ls(i,l=True)[0].split('|'))
                        if depth in depthList:
                            pass
                        else:
                            depthList.append(depth)
                except:
                    pass
            

            depthList = sorted(depthList)
            allBoneList = []
            for depth in depthList:
                for i in tempAllBoneList:
                   # print len(cmds.ls(i,l=True)[0].split('|'))
                    if len(cmds.ls(i,l=True)[0].split('|')) == depth:
                        if i in allBoneList:
                            pass
                        else:
                            allBoneList.append(i)
                        
            rootBoneList = [{ "name":rootCtrlName}]
            boneList = self.getAllBoneList(allBoneList,rootBoneList)
            slotList = self.getAllRegionSlotList(allBoneList) 
            initSkinList= {"default":{}}

            skinDict = self.getAllRegionSkinList(slotList,initSkinList)
        if len(characterSetGrp) == 0: 
        
            print "no character set"
            allMeshSlotList = []
            allSkinNameList = []
            
        if  len(characterSetGrp) > 0: 
            allMeshSlotList = []
            allSkinNameList = []

            for chaSet in characterSetGrp:
                boneList.append({"name":chaSet,'parent':rootCtrlName})
             #   print 'chaSet',chaSet
                allBoneList.append(chaSet)
                allTransformsList =  cmds.listRelatives(chaSet,c=True,p=False)
                
                if allTransformsList == None :
                    print "no mesh in characterSet %s"%chaSet
                    pass
                else:
                    for i in allTransformsList:
                        for j in cmds.listRelatives(i,c=True,p=False):
                
                            try:
                                if cmds.nodeType(j) =='mesh' and cmds.getAttr('%s.spine_skinType'%j) =='mesh':
                                    allMeshSlotList.append(i)
                                    allSkinNameList.append(j)
                            except:
                                pass
            
            for slot in allMeshSlotList: ## define all mesh's slot
            #   print cmds.ls(i)
                try:
                    self.defineSlot(slot,rootCtrlName) 
                except:
                    pass
                try:
                 #   print 'slot',slot
                    currentParent = cmds.listRelatives(slot,p=True)[0]
                #    print 'currentParent',currentParent
                    if cmds.getAttr('%s.spine_tag'%currentParent) == 'spine_characterSet':
                        cmds.setAttr('%s.slot_bone'%slot,currentParent,type='string')
                except:
                    print 'current slot/mesh not in character set'
                    pass
            
            for i in allSkinNameList:
                skinData = json.loads(cmds.getAttr('%s.spine_skinData'%i))
                skinDict['default'].update(skinData)   
                
            for slotData in self.getAllMeshSlots(allMeshSlotList):
                slotList.append(slotData)
                
            ### check how many animLayers   
        animLayerList = cmds.ls(type ="animLayer")
        allAnimDict= {}
       # print "all all all",slotList,allBoneList,allMeshSlotList,characterSetGrp
        if len(animLayerList) == 0 :
            
            animDict = self.defineAllAnimLayerDict("default",slotList,allBoneList,allMeshSlotList,characterSetGrp)  
          #  print 'animDict',animDict
            slotAnimLayerDict = animDict['slotRegionTimeLineDict']
            boneAnimLayerDict = animDict['boneRegionTimeLineDict']
            deformAnimLayerDict = animDict['deformTimeLineDict'] 
            allAnimDict.update({"default":{"slots":slotAnimLayerDict,"bones":boneAnimLayerDict,"deform":deformAnimLayerDict}})
        else:
            for i in animLayerList:
                if i == "BaseAnimation":
          
                    animDict = self.defineAllAnimLayerDict("default",slotList,allBoneList,allMeshSlotList,characterSetGrp)
                    
                  
                else:
                    animDict = self.defineAllAnimLayerDict(i,slotList,allBoneList,allMeshSlotList,characterSetGrp)
                    
                slotAnimLayerDict = animDict['slotRegionTimeLineDict']
                boneAnimLayerDict = animDict['boneRegionTimeLineDict']
                deformAnimLayerDict = animDict['deformTimeLineDict'] 

                allAnimDict.update({i:{"slots":slotAnimLayerDict,"bones":boneAnimLayerDict,"deform":deformAnimLayerDict}})

        exportData = {"skeleton":{"images": "../images/"},"bones":boneList,"slots":slotList,"skins":skinDict,"animations":allAnimDict}
        writeData = json.dumps(exportData, sort_keys=True , indent =4) 
        with open(fileName, 'w') as the_file:
            the_file.write(writeData)

           # slotRegionTimeLineDict = self.defineRegionSlotAnimation(regionSlotList)
            #boneTimeLineDict = self.defineBoneAnimation(allBoneList)
           # slotList = regionSlotList
           # boneAnimDict = boneTimeLineDict
          #  slotAnimDict= slotRegionTimeLineDict



    def defineAllAnimLayerDict(self,animLayerName,slotList,allBoneList,allMeshSlotList,characterSetGrp):
        print "animLayerName________",animLayerName
       # print "slotList",slotList
       # print "allBoneList",allBoneList
       # print "allMeshSlotList",allMeshSlotList
       # print "characterSetGrp",characterSetGrp
        if animLayerName == "default":
            slotInAnimLayer = []
            slotNotInAnimLayer = []
            boneInAnimLayer = allBoneList
            boneNotInAnimLayer = []
            for i in range(0,len(slotList)):
                slotInAnimLayer.append(slotList[i]['name'])
        else:
            
            slotInAnimLayer = []
            slotNotInAnimLayer = []
            boneInAnimLayer = []
            boneNotInAnimLayer = []
            
            for i in range(0,len(slotList)):
                cmds.select(cl=True)
                slotName=slotList[i]['name']
                boneName = cmds.getAttr('%s.slot_bone'%slotName)
               # print 'slotName',slotName,boneName

                cmds.select(boneName)
                ableSlotInAnimLayer = []
                ableSlotInAnimLayer = cmds.animLayer(afl=True,q=True)
              
               # print 'tempAbleSlotInAnimLayer',tempAbleSlotInAnimLayer
               
                
                
              #  print 'ableSlotInAnimLayer',ableSlotInAnimLayer
                cmds.select(cl=True)
                if ableSlotInAnimLayer == None:
                    print '%s not in animationLayer'%slotName
                    if slotName in slotNotInAnimLayer:
                        pass
                    else:
                        slotNotInAnimLayer.append(slotName)
                    if boneName in boneNotInAnimLayer:
                        pass
                    else:
                        boneNotInAnimLayer.append(boneName)
                else:
                    if animLayerName in ableSlotInAnimLayer:
                        if slotName in slotInAnimLayer:
                            pass
                        else:
                            slotInAnimLayer.append(slotName)
                        if boneName in boneInAnimLayer:
                            pass
                        else:
                            boneInAnimLayer.append(boneName)    
                            
                            
                    else:
                        if slotName in slotNotInAnimLayer:
                            pass
                        else:
                            slotNotInAnimLayer.append(slotName)
                            
                        if boneName in boneNotInAnimLayer:
                            pass
                        else:
                            boneNotInAnimLayer.append(boneName)   
      #  print 
        slotRegionTimeLineDict = self.defineRegionSlotAnimation(slotInAnimLayer,slotNotInAnimLayer,animLayerName)  
        boneRegionTimeLineDict = self.defineBoneAnimation(boneInAnimLayer,boneNotInAnimLayer,animLayerName)
        deformerDict = self.defineDeformAnimation(boneInAnimLayer,boneNotInAnimLayer,animLayerName)
        
        
        print 'slotRegionTimeLineDict____7',animLayerName,slotRegionTimeLineDict
        print 'boneRegionTimeLineDict____8',animLayerName,boneRegionTimeLineDict
        print 'deformerDict',deformerDict
  
  
        print 'slotInAnimLayer',animLayerName,slotInAnimLayer
        print 'slotNotInAnimLayer',animLayerName,slotNotInAnimLayer

        print 'boneInAnimLayer',animLayerName,boneInAnimLayer
        print 'boneNotInAnimLayer',animLayerName,boneNotInAnimLayer

        return {'slotRegionTimeLineDict':slotRegionTimeLineDict,'boneRegionTimeLineDict':boneRegionTimeLineDict,'deformTimeLineDict':deformerDict}
    


    #### 輸出     
    def defineDeformAnimation(self,boneInAnimLayer,boneNotInAnimLayer,animLayerName):
        print "defineDeformAnimation",boneInAnimLayer,boneNotInAnimLayer
        chaInAnimLayer = []
        chaNotInAnimLayer =[]
        
        for i in boneInAnimLayer:
            if cmds.getAttr('%s.spine_tag'%i) == 'spine_characterSet':  
                chaInAnimLayer.append(i)
        for i in boneNotInAnimLayer:
            if cmds.getAttr('%s.spine_tag'%i) == 'spine_characterSet':  
                chaNotInAnimLayer.append(i)   
                
        print 'chaInAnimLayer',chaInAnimLayer,chaNotInAnimLayer
        allKeyFrameListByDeformers = self.findAllMeshKeyframes(chaInAnimLayer,chaNotInAnimLayer) ## 根據控制器，變形器，骨架，取得所有的keyFrame 

        meshDeformDict = self.defineVertexsValueDeltaTime(allKeyFrameListByDeformers,animLayerName) ## 取得每個keyframe的vertex 數值
        #print 'meshDeformDict',meshDeformDict
        return meshDeformDict

               
    ### find all keyframe in characterSet    ## 根據控制器，變形器，骨架，取得所有的keyFrame 
    def findAllMeshKeyframes(self,characterSetGrp,chaNotInAnimLayer):
        print "findAllKeyframes"
        #characterSetGrp = 'saberSet'  ###input
        startFrame = float(self.timeStartLEdit.text())
        endFrame = float(self.timeEndLEdit.text())
        allObjects = cmds.ls(characterSetGrp,fl=True,dag=True,type='mesh')
       # print 'allObjects',allObjects
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
      #  print 'meshList',meshList
              
        for i in meshList:
            allKeyframesList = [startFrame,endFrame]
            allDeformersList = cmds.listHistory(i)
           #  allKeyframes = cmds.keyframe( deformer, query=True)
           # print 'allDeformersList',allDeformersList
           
          
            for deformer in allDeformersList:
                allLayerKeys = self.findKeysAllAnimLayer(deformer,'none',startFrame,endFrame) ## without baseAnimationLayer
                baseAnimationLayerKeys = self.findKeysBaseAnimationLayer(deformer,'none',startFrame,endFrame)
              #  print 'allLayerKeys',allLayerKeys,baseAnimationLayerKeys
                for f in allLayerKeys:
                    if f in allKeyframesList:
                        pass
                    else:
                        allKeyframesList.append(f)
                for f in baseAnimationLayerKeys:
                    if f in allKeyframesList:
                        pass
                    else:
                        allKeyframesList.append(f)
                    
            allKeyFrameDict.update({i:sorted(allKeyframesList)})
                        
                                                                                                                                             
                                                                                                  
      #  print 'allKeyFrameDict',allKeyFrameDict
        return allKeyFrameDict                

              
    def defineVertexsValueDeltaTime(self,allKeyFrameListByDeformers,animLayerName):
        print "defineVertexsValueDeltaTime"
        errMsg = "get vertexValue Error"
        fps = float(self.fpsLEdit.text())

        #print allKeyFrameListByDeformers
        frameStart = float(self.timeStartLEdit.text())
        frameEnd = float(self.timeEndLEdit.text())
        skinName = "default"#animLayerName
        meshDeformDict = {skinName:{}}
        
        meshList = allKeyFrameListByDeformers.keys()
        
        self.deSelectAllAnimationLayer()
        try:              
            cmds.animLayer( animLayerName, e=True, selected=True,l=false)    
        except:
            pass
        print 'meshList',meshList
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
            for vertex in vertexList:
                vertexPositionPreFrameList.append(0.0)
                vertexPositionPreFrameList.append(0.0)
                
            vertexPositionZeroFrame =[]
            cmds.currentTime(0.0,e=True)
            for vertex in vertexList:
                vertexPositionZeroFrame.append(float('{:.3f}'.format(cmds.pointPosition(vertex)[0])))
                vertexPositionZeroFrame.append(float('{:.3f}'.format(cmds.pointPosition(vertex)[1])) )            
               
           # print 'vertexPositionPreFrameList_original',vertexPositionPreFrameList
            filterKeyFrameList = []
            for k in keyFrameList:
                if k in filterKeyFrameList:
                    pass
                else:
                    filterKeyFrameList.append(k)
                    
            
           # print 'filterKeyFrameList',filterKeyFrameList
            for f in filterKeyFrameList:
                vertexPositionCurrentFrameList = []
                deltaVertexPositionPreFrameList=[]

                cmds.currentTime(f,e=True)
                for vertex in vertexList:
                    #print vertex
                    vertexPosionX_CurrentFrame = float('{:.3f}'.format(cmds.pointPosition(vertex)[0]))
                    vertexPosionY_CurrentFrame =float('{:.3f}'.format(cmds.pointPosition(vertex)[1])) 

                    vertexPositionCurrentFrameList.append(vertexPosionX_CurrentFrame)
                    vertexPositionCurrentFrameList.append(vertexPosionY_CurrentFrame)
 
                        
                for i in range(0,len(vertexPositionCurrentFrameList)):
                  #  if f == 0.0:
                    #     deltaVertexPositionPreFrameList.append(0)
                  #  else:
                    deltaPosition =  vertexPositionCurrentFrameList[i] -vertexPositionZeroFrame[i]
                    if abs(deltaPosition) <0.01:
                        deltaVertexPositionPreFrameList.append(0)
                    else:
                        deltaVertexPositionPreFrameList.append(float('{:.3f}'.format(deltaPosition)))
                   # print deltaPosionX,deltaPosionY float('{:.3f}'.format(deltaPosition))
                vertexPositionPreFrameList = []
                vertexPositionPreFrameList = vertexPositionCurrentFrameList
              #  print 'vertexPositionPreFrameList',vertexPositionPreFrameList
                frame = float(f)/float(fps)
                print f,frame
                meshDeformDict[skinName][slotName][attachmentName].append({"time":float('{:.3f}'.format(frame)),"vertices":deltaVertexPositionPreFrameList})
        print 'meshDeformDict__',meshDeformDict
        return meshDeformDict
                         

                               
                                                        
    def getAllBoneList(self,allBoneList,rootBoneList):
        rootCtrlName = self.exportSpineRootLabelLEdit.text()
       # characterSetGrp =[]
        boneList = rootBoneList
        #boneList = []
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
           # print inheritScale,inheritRation
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
        print "allBoneList",allBoneList
        slotList = []
        
        for i in allBoneList:
              
                
            itemList = cmds.listRelatives(i,c=True)
            
            
            
            for j in itemList:
               # print j , cmds.nodeType(j)
                if cmds.getAttr('%s.spine_tag'%j) == 'spine_slot':
                    boneName = cmds.getAttr('%s.slot_bone'%j)#i["name"]
                    blendModeGet = int(cmds.getAttr("%s.slot_blend"%boneName))
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
                    fade = float(cmds.getAttr('%s.slot_fade'%boneName))
                    color = cmds.getAttr('%s.slot_color'%boneName)[0]
                    alpha = float(cmds.getAttr('%s.slot_alpha'%boneName)) *fade
                    dark = cmds.getAttr('%s.slot_dark'%boneName)[0]
                    attachment = cmds.getAttr('%s.slot_attachment'%j)
                    alphaHex = "%02x"%int((alpha/1)*255)
                    colorHex = "%02x"%int((color[0]/1)*255) + "%02x"%int((color[1]/1)*255) +"%02x"%int((color[2]/1)*255)
                    darkHex = "%02x"%int((dark[0]/1)*255) + "%02x"%int((dark[1]/1)*255) +"%02x"%int((dark[2]/1)*255)
                    exportColorHex = str(colorHex + alphaHex)
                   # print 'blendMode',blendMode
                    slotDict =  {"name":slotName,
                                 "bone":parent,
                                 "color":exportColorHex,
                                 "dark":darkHex,
                                 "attachment":attachment,
                                 "blend":blendMode}
                   # print 'darkHex',darkHex,type(darkHex)
                    if darkHex == "000000":
                        pass
                    else:
                        slotDict.update({"dark":darkHex})
                    slotList.append(slotDict)  #additive

                       
        return slotList    
 

    def getAllRegionSkinList(self,regionSlotList,skinList):
        print "getAllRegionSkinList"
       # print 'regionSlotList',regionSlotList
       # skinList= {"default":{}}
        
       # print "slotList",slotList
       # print "slotListLength",len(slotList)
            
        for i in regionSlotList:
            slotName = i["name"]
            attachment = cmds.getAttr('%s.slot_attachment'%slotName)
            width = int(cmds.getAttr( "%s.slot_width"%slotName))
            height = int(cmds.getAttr( "%s.slot_height"%slotName))
           # attachment = cmds.getAttr('%s.slot_attachment'%slotName)
            slot_sequence = cmds.getAttr('%s.slot_sequence'%slotName)
            seqAmount = int(float(cmds.getAttr('%s.slot_sequenceAmount'%slotName)))

            x = int(cmds.getAttr( "%s.translateX"%slotName))
            y = int(cmds.getAttr( "%s.translateY"%slotName))
            r = float(cmds.getAttr( "%s.rotateZ"%slotName))

            if slot_sequence == 1:
                regionSlotSkinDict={}

                for i in range(0,seqAmount):
                    attachmentSeq = attachment.split('.')[0] 
                    atchmentName = attachmentSeq+ '.' + str('{0:04d}'.format(i+1))
                    regionSlotSkinDict.update({atchmentName:{"width": width,"height": height, "x":x,"y":y }})
            else:
           
                regionSlotSkinDict = {attachment:{"width": width,"height": height, "x":x,"y":y }}

            if r == 0.0:
                pass
            else:
                regionSlotSkinDict[attachment].update({"rotation":'{:.2f}'.format(r)})
             
            skinList["default"].update({slotName:regionSlotSkinDict})                                                                                                              
        return skinList
                

    def defineRegionSlotAnimation(self,regionSlotList,slotNotInAnimLayer,animLayerName):
        print "defineRegionSlotAnimation"
        #slotInAnimLayer,animLayerName

        print "regionSlotList",regionSlotList
        print "slotNotInAnimLayer",slotNotInAnimLayer
        print "animLayerName",animLayerName
        animLayerList = cmds.ls(type ="animLayer")
        cmds.currentTime(0.0,e=True)
        startFrame = float(self.timeStartLEdit.text())
        endFrame = float(self.timeEndLEdit.text())
        fps = float(self.fpsLEdit.text())
       # fileName = self.selectExportFileBTnLEdit.text()
        
        actionName = animLayerName
        animationList = {}
        actionAnimation={actionName:{"slots":{},
                                     "bones":{}}}     
        
        slotColorAttr = ["slot_color","slot_alpha","slot_dark"]                       
        soltsAnimationDict= {}    
        slotTimeLineDict ={} 
        #print regionSlotList
        for slot in regionSlotList:  
        
        
            slotName = slot#str(slot["name"])
            boneName = str(cmds.getAttr('%s.slot_bone'%slotName))
            
            if cmds.getAttr('%s.spine_tag'%boneName) == "spine_characterSet":
                pass
            elif cmds.getAttr('%s.spine_tag'%boneName) == "spine_bone":
                attachment = cmds.getAttr('%s.slot_attachment'%slotName)

                slot_sequence = cmds.getAttr('%s.slot_sequence'%slotName)
                slotTimeLineDict.update({slotName:{"color":[]}})

                #slotTimeLineDict = {slotName:{"color":[],"attachment":[]}}
                
                #soltsAnimationDict.update(tempSlotDict)
                
               # print 'attr',slotName,boneName,attachment,slotColor,slotAlpha,slotDark,slot_frequenceCheck
               # attachment = slot["attachment"]    
               
                slotColorKeyFrameList = [startFrame,endFrame] 
                
                
                
               # print "animLayerList",animLayerList

                for attr in slotColorAttr:
                    allLayerKeys = self.findKeysAllAnimLayer(boneName,attr,startFrame,endFrame) ## without baseAnimationLayer
                    baseAnimationLayerKeys = self.findKeysBaseAnimationLayer(boneName,attr,startFrame,endFrame)
                  #  print 'allLayerKeys',allLayerKeys,baseAnimationLayerKeys
                    for f in allLayerKeys:
                        if f in slotColorKeyFrameList:
                            pass
                        else:
                            slotColorKeyFrameList.append(f)
                    for f in baseAnimationLayerKeys:
                        if f in slotColorKeyFrameList:
                            pass
                        else:
                            slotColorKeyFrameList.append(f)
                        
                
                

                   
                slotColorKeyFrameList = sorted(slotColorKeyFrameList)
                
                #for f in slotColorKeyFrameList                 
                #frameValue = cmds.keyframe(obj,at=attr,t=(frame,frame),q=True,eval=True)[0]    starFrame                 
                print 'slotColorKeyFrameList_____4',slotColorKeyFrameList
                for i in range(0,len(slotColorKeyFrameList)) :
                    f = slotColorKeyFrameList[i]
                     
                    if f == 0.0:

                        color = cmds.getAttr('%s.slot_color'%boneName,t=0.0)[0]

                        slotAlpha = cmds.getAttr('%s.slot_alpha'%boneName,t=0.0)

                        dark = cmds.getAttr('%s.slot_dark'%boneName,t=0.0)[0]

                        fade = cmds.getAttr('%s.slot_fade'%boneName,t=0.0)
                       # print color, slotAlpha,dark,boneName,fade
                        alpha = slotAlpha * fade
                        alphaHex = "%02x"%int((alpha/1)*255)
                        colorHex = "%02x"%int((color[0]/1)*255) + "%02x"%int((color[1]/1)*255) +"%02x"%int((color[2]/1)*255)
                        darkHex = "%02x"%int((dark[0]/1)*255) + "%02x"%int((dark[1]/1)*255) +"%02x"%int((dark[2]/1)*255)
                        exportColorHex = str(colorHex + alphaHex)
                        exportDarkHex = str(darkHex + alphaHex)
                        slotTimeLineDict[slotName]["color"].append({ "time": 0.0, "color":exportColorHex,"dark": exportDarkHex })
                    
                    else:
                        pf = slotColorKeyFrameList[i-1]
                       # for attr in slotColorAttr:
                        tempSlorColordTdict = {}
                        colorF = cmds.getAttr('%s.slot_color'%boneName,t=f)[0]
                        slotAlphaF = cmds.getAttr('%s.slot_alpha'%boneName,t=f)
                        darkF = cmds.getAttr('%s.slot_dark'%boneName,t=f)[0]
                        fadeF = cmds.getAttr('%s.slot_fade'%boneName,t=f)
                        alphaF = slotAlphaF * fadeF
                        colorPF = cmds.getAttr('%s.slot_color'%boneName,t=pf)[0]
                        slotAlphaPF =cmds.getAttr('%s.slot_alpha'%boneName,t=pf)
                        darkPF = cmds.getAttr('%s.slot_dark'%boneName,t=pf)[0]
                        fadePF = cmds.getAttr('%s.slot_fade'%boneName,t=pf)
                        alphaPF = slotAlphaPF * fadePF

                        colorHex = "%02x"%int((colorF[0]/1)*255) + "%02x"%int((colorF[1]/1)*255) +"%02x"%int((colorF[2]/1)*255)
                        alphaHex = "%02x"%int((alphaF/1)*255)
                        darkHex = "%02x"%int((darkF[0]/1)*255) + "%02x"%int((darkF[1]/1)*255) +"%02x"%int((darkF[2]/1)*255)
                        colorHexPF = "%02x"%int((colorPF[0]/1)*255) + "%02x"%int((colorPF[1]/1)*255) +"%02x"%int((colorPF[2]/1)*255)
                        alphaHexPF = "%02x"%int((alphaPF/1)*255)
                        darkHexPF = "%02x"%int((darkPF[0]/1)*255) + "%02x"%int((darkPF[1]/1)*255) +"%02x"%int((darkPF[2]/1)*255)                    

                        
                        exportColorHexF = str(colorHex + alphaHex)
                        exportDarkHexF = str(darkHex + alphaHex)
                        exportColorHexPF = str(colorHexPF + alphaHexPF)
                        exportDarkHexPF = str(darkHexPF + alphaHexPF)                    
                      #  if exportColorHexF == exportColorHexPF:
                       #     pass
                        #else:
                        tempSlorColordTdict.update({"time":float('{:.3f}'.format(float(f)/fps)),"color":exportColorHexF})
                        #if exportDarkHexF == exportDarkHexPF:
                        #    pass
                        #else:
                        tempSlorColordTdict.update({"time":float('{:.3f}'.format(float(f)/fps)),"dark":exportDarkHexF})
                        slotTimeLineDict[slotName]["color"].append(tempSlorColordTdict)     
                if slot_sequence == 1:
                    #slotTimeLineDict.update({slotName:{"color":[],"attachment":[]}})
                    slotTimeLineDict[slotName].update({"attachment":[]})
                    print "frequenceImageMode"
                    seqAmount = int(float(cmds.getAttr('%s.slot_sequenceAmount'%slotName)))
                    seqSpeed = float(cmds.getAttr('%s.slot_sequenceSpeed'%slotName))
                   # keyframeList = [] slot_frequenceCheck
                    randomCheck = cmds.getAttr('%s.slot_sequence_random'%slotName)
                    if randomCheck == 0:
                        fileNumCount = 1
                    else:
                        fileNumCount = random.randint(0,seqAmount)
                    f = startFrame
                    attachmentSeq = attachment.split('.')[0]
                    #fileNumCount = 1
                    while f < endFrame:
                       # print f,type(f)
                        if seqSpeed <= 1.0:  ###low speed f= 0,5,10,15; fileNum= 0,1,2,3,4,5...seqAmount
                        
                            fSpace = int(1.0/seqSpeed)
                            atchmentName = attachmentSeq+ '.' + str('{0:04d}'.format(int(fileNumCount)))
                            slotTimeLineDict[slotName]["attachment"].append({"time":float('{:.3f}'.format(float(f)/fps)),"name":str(atchmentName)})
       
                            f = f+fSpace
                            fileNumCount = (fileNumCount )%seqAmount +1
                        else:  ##highSpeed, f = 0,1,2,3,4,5,.....endFrame ;fileNum 1,5,9,13.....
                            atchmentName = attachmentSeq+ '.' + str('{0:04d}'.format(int(fileNumCount)))
                            slotTimeLineDict[slotName]["attachment"].append({"time":float('{:.3f}'.format(float(f)/fps)),"name":str(atchmentName)}) 
                            f= f+1
                            fileNumCount = (fileNumCount + seqSpeed)%seqAmount
        
            
                
        for slot in slotNotInAnimLayer:
            slotName = slot#str(slot["name"])
            boneName = str(cmds.getAttr('%s.slot_bone'%slotName))
            
           # if cmds.getAttr('%s.spine_tag'%boneName) == "spine_characterSet":
            tempSlorColordTdict = {slotName:{"color": [{'color': 'ffffff00', 'dark': '000000ff', 'time': 0.0}]}}
                
               # pass
          #  elif cmds.getAttr('%s.spine_tag'%boneName) == "spine_bone":
               # tempSlorColordTdict = {slotName:{"color": [{'color': 'ffffff00', 'dark': '000000ff', 'time': 0.0}]}}
            slotTimeLineDict.update(tempSlorColordTdict)
        
        return slotTimeLineDict                                           
    


    def findKeysAllAnimLayer(self,obj,attr,startFrame,endFrame):
       # print "findKeysAllAnimLayer"
        keyframeList = []

        animLayerList = cmds.ls(type ="animLayer")
        if len(animLayerList) == 0:
            try:
                tempKeyframeList = cmds.keyframe(obj, t=(startFrame,endFrame),query=True)
                for k in tempKeyframeList:
                    if k in keyframeList:
                        pass
                    else:
                        keyframeList.append(k)
            except:
                pass
        else:
            
            for j in animLayerList:
             #   print "findKeysAllAnimationLayer %s"%j, obj

                if j == 'BaseAnimation':
                    pass
                else:
                    self.deSelectAllAnimationLayer()

                    cmds.animLayer( j, e=True, selected=True,l=False)
                    try:
                        tempKeyframeList = cmds.keyframe(obj, t=(startFrame,endFrame),query=True)
                 
                  #  print 'tempKeyframeList',j,tempKeyframeList 
                        for k in tempKeyframeList:
                            if k in keyframeList:
                                pass
                            else:
                                keyframeList.append(k)
                    except:
                        pass
        #keyframeList = sorted(keyframeList)             
        return keyframeList

    def findKeysBaseAnimationLayer(self,obj,attr,startFrame,endFrame):  
        print "findKeysBaseAnimationLayer"
      #  print 'obj,attr,startFrame,endFrame',obj,attr,startFrame,endFrame,type(obj),type(attr),type(startFrame),type(endFrame)
        try:
            animLayerList = cmds.ls(type ="animLayer")
        except:
            animLayerList=[]
        baseAniLayerKeyframeList = []
        if len(animLayerList) == 0:
            try:
                if attr == "none":
                    tempKeyframeList = cmds.keyframe(obj, t=(startFrame,endFrame),query=True)
                else:
                    
                    tempKeyframeList = cmds.keyframe(obj, t=(startFrame,endFrame),query=True,at=attr)
            except:
                tempKeyframeList= []
            try:
                for k in tempKeyframeList:
                    if k in baseAniLayerKeyframeList:
                        pass
                    else:
                        baseAniLayerKeyframeList.append(k)     
            except:
                pass
        else:
            self.deSelectAllAnimationLayer()
            cmds.animLayer( 'BaseAnimation', e=True, selected=True,l=False)  
            try: 
                if attr == "none":
                    tempKeyframeList = cmds.keyframe(obj, t=(startFrame,endFrame),query=True)
                else:
                    
                    tempKeyframeList = cmds.keyframe(obj, t=(startFrame,endFrame),query=True,at=attr)
            except:
                pass
            
            try:
                for k in tempKeyframeList:
                    if k in baseAniLayerKeyframeList:
                        pass
                    else:
                        baseAniLayerKeyframeList.append(k)     
               # print baseAniLayerKeyframeList
            except:
                pass
       # print 'baseAniLayerKeyframeList',baseAniLayerKeyframeList
        return baseAniLayerKeyframeList
        
     
                                      
                                                                                                        
    def deSelectAllAnimationLayer(self):
        animLayerList = cmds.ls(type ="animLayer")
        for L in animLayerList:
            #if L == "BaseAnimation":
                
            cmds.animLayer( L, e=True, selected=False,l=True)
            
    
    def defineBoneAnimation(self,boneInAnimLayer,boneNotInAnimLayer,animLayerName):
        print "defineBoneAnimation",animLayerName
        print "boneInAnimLayer",boneInAnimLayer
        print "boneNotInAnimLayer",boneNotInAnimLayer
        animLayerList = cmds.ls(type ="animLayer")
              
        for j in animLayerList:
            cmds.animLayer( j, e=True, selected=False,s=False)## deselect all animation Layer
        try:              
            cmds.animLayer( animLayerName, e=True, selected=True,s=True)
        except:
            pass
        
        
        startFrame = float(self.timeStartLEdit.text())
        endFrame = float(self.timeEndLEdit.text())
        fps = float(self.fpsLEdit.text())

        boneTimeLineDict ={}
        boneAttr = ['translateX','translateY','rotateZ','scaleX','scaleY']
        for bone in boneInAnimLayer:
           # print 'bone______',bone
            if  cmds.getAttr('%s.spine_tag'%bone) == "spine_characterSet":
                pass
            elif cmds.getAttr('%s.spine_tag'%bone) == "spine_bone":
                boneTimeLineDict.update({bone:{"rotate":[],"translate":[],"scale":[]}})
                boneKeyFrameList = [startFrame,endFrame]

            
                for attr in boneAttr:
                    allLayerKeys = self.findKeysAllAnimLayer(bone,attr,startFrame,endFrame) ## without baseAnimationLayer
                    baseAnimationLayerKeys = self.findKeysBaseAnimationLayer(bone,attr,startFrame,endFrame)

                    for f in allLayerKeys:
                        if f in boneKeyFrameList:
                            pass
                        else:
                            boneKeyFrameList.append(f)
                    for f in baseAnimationLayerKeys:
                        if f in boneKeyFrameList:
                            pass
                        else:
                            boneKeyFrameList.append(f)
                   # except:
                      #  pass
                            
                boneKeyFrameList = sorted(boneKeyFrameList)
                print 'boneKeyFrameList_________5',boneKeyFrameList
                self.deSelectAllAnimationLayer()
                try:              
                    cmds.animLayer( animLayerName, e=True, selected=True,l=false)    
                except:
                    pass
                for f in boneKeyFrameList:
                  #  if f == 0.0:
                    rotate = cmds.getAttr('%s.rotateZ'%bone,t = f)
                    x = cmds.getAttr('%s.translateX'%bone,t = f)
                    y = cmds.getAttr('%s.translateY'%bone,t = f)
                    sx = cmds.getAttr('%s.scaleX'%bone,t = f)
                    sy = cmds.getAttr('%s.scaleY'%bone,t = f)
                    boneTimeLineDict[bone]['rotate'].append({"time":float('{:.3f}'.format(float(f)/fps)),"angle":float('{:.3f}'.format(float(rotate)))})
                    boneTimeLineDict[bone]['translate'].append({"time":float('{:.3f}'.format(float(f)/fps)),"x":float('{:.3f}'.format(float(x))),"y":float('{:.3f}'.format(float(y)))})
                    boneTimeLineDict[bone]['scale'].append({"time":float('{:.3f}'.format(float(f)/fps)),"x":float('{:.3f}'.format(float(sx))),"y":float('{:.3f}'.format(float(sy)))})
      #  print "boneTimeLineDict_______1",boneTimeLineDict
        
        for bone in boneNotInAnimLayer:
            boneTimeLineDict.update({bone:{"rotate":[{"time":0.0,"angle":0.0}],"translate":[{"time":0.0,"x":0.0,"y":0.0}],"scale":[{"time":0.0,"x":1.0,"y":1.0}]}})
        # print 'boneKeyFrameList',bone,boneKeyFrameList
     #   print "boneTimeLineDict",boneTimeLineDict
        return boneTimeLineDict    
                                                                                                                                                                                                                                                                                                                              



        
        
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
            cmds.addAttr(bone, ln='spineBone', numberOfChildren=18, attributeType='compound' )
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
           # cmds.addAttr(bone, ln='set_path', sn='s_path' , at="bool", dv=0,parent='spineBone' ,k=True )
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
        currentMeshTransform = cmds.ls(sl=True,type = 'transform')
        parentCharacterSet = cmds.listRelatives(currentMeshTransform,p=True)[0]
        print 'parentCharacterSet1',parentCharacterSet
        try:
            if len(parentCharacterSet) >0:
                if cmds.nodeType(parentCharacterSet) == 'transform':
                   # print parent
                    if cmds.getAttr('%s.spine_tag'%parentCharacterSet) =='spine_characterSet':
                        print 'parent CharacterSet %s is selected'%parentCharacterSet
                    
                else:
                    self.errorMsgLEdit.setText('current mesh not in characterSet Code skin 001')
        except:
            self.errorMsgLEdit.setText('current mesh not in characterSet Code skin 002')

            pass
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
        print 'parentCharacterSet',parentCharacterSet
        
        
        cmds.setAttr('%s.spine_tag'%meshName,'spine_skin',type='string')
        cmds.setAttr('%s.spine_skinType'%meshName,'mesh',type='string')

        cmds.setAttr('%s.spine_slotName'%meshName,slotName,type='string')
        cmds.setAttr('%s.spine_skinName'%meshName,slotName,type='string')  
        cmds.setAttr('%s.spine_boneName'%meshName,parentCharacterSet,type='string')             
                  
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
     
     
        jointSize = float(self.jontSizeLEdit.text())

        cmds.jointDisplayScale(jointSize)
        
        
    def vertexSizeChange(self):
        print "jointDisplayScale"
        vertexSize  = float(self.vertexSizeSB.text())
        
        cmds.polyOptions(sv=vertexSize)

     
     
    def defineCreateBGBtn(self):
        print "defineCreateBGBtn"
        bgWidth = int(self.createBG_comboBox.currentText().split('x')[0])
        bgHeight = int(self.createBG_comboBox.currentText().split('x')[1])
      #  print (bgWidth,bgHeight)
        slotPlane = cmds.polyPlane(n='BG_plane',sx=1,sy=1)[0]
        cmds.setAttr('%s.rotateX'%slotPlane,90)
        cmds.setAttr('%s.scaleX'%slotPlane,bgWidth)
        cmds.setAttr('%s.scaleZ'%slotPlane,bgHeight)
        shader = cmds.shadingNode("lambert",asShader=True,n='bgPlane')
        cmds.setAttr('%s.color'%shader, 0.0,0.0, 0.0, type="double3")
        cmds.select(cl=True)
        cmds.select(slotPlane)
        cmds.hyperShade( assign=shader ) 
        cmds.select(cl=True)
        
        
        

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
        cmds.addAttr(bone, ln='spineBone', numberOfChildren=24, attributeType='compound' )
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
        cmds.addAttr(bone, ln='set_path', sn='s_path' , at="bool", dv=0,parent='spineBone' ,k=True )
       
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
    
    def copyKeyToSelectBone(self):
        print "copyKeyToSelectBone"
        
        tempSourceBoneSelected = cmds.ls(sl=True) 
        self.currentSelectedBone = filter(lambda x: cmds.getAttr('%s.spine_tag'%x)== 'spine_bone' ,tempSourceBoneSelected)
        sourceBoneCount = len(self.currentSelectedBone)
        
        self.copyBoneKey.setText('copy Bone Keys _(%s)'%sourceBoneCount)
        
        #target
    def pasteKeyToSelectBone(self):
        
        print "pasteKeyToSelectBone"
        print self.currentSelectedBone
        tempSourceBoneSelected = cmds.ls(sl=True) 
        currentSelectedBone = filter(lambda x: cmds.getAttr('%s.spine_tag'%x)== 'spine_bone' ,tempSourceBoneSelected)
        targetBoneCount = len(currentSelectedBone)
        sourceBoneCount = len(self.currentSelectedBone)
        if  targetBoneCount != sourceBoneCount:
            self.errorMsgLEdit.setText('count error') 
        else:
            for i in range(0,sourceBoneCount):
                cmds.currentTime(0,e=True)
                cmds.copyKey(self.currentSelectedBone[i])
                targetBone = currentSelectedBone[i]
                cmds.pasteKey(targetBone)
            
            
        


    def duplicateSlot(self):
        print "duplicateSlot"
        
        tempSourceBoneSelected = cmds.ls(sl=True) 
        sourceBoneSelected = filter(lambda x: cmds.getAttr('%s.spine_tag'%x)== 'spine_bone' ,tempSourceBoneSelected)
        
        sourceBoneCount = len(sourceBoneSelected)
        for i in range(0,sourceBoneCount):
            sourceBoneName = cmds.getAttr('%s.bone_name'%sourceBoneSelected[i])
            sourceSlotName = cmds.getAttr('%s.bone_slot'%sourceBoneSelected[i])
            newSlotW = cmds.getAttr('%s.slot_width'%sourceBoneSelected[i])
            newSlotH = cmds.getAttr('%s.slot_height'%sourceBoneSelected[i])
            parentBone = cmds.getAttr('%s.bone_parent'%sourceBoneName)

            attachmentFile = cmds.getAttr('%s.slot_attachment'%sourceSlotName)

            existNameBoneCount = len(cmds.ls('%s*'%sourceBoneName))
            newBoneCount = existNameBoneCount +1
            boneName = sourceBoneName +'_'+'{:02}'.format(newBoneCount)
            slotName = boneName.split('bone_')[1]
            #cmds.setAttr('%s.slot_attachment'%bone,attachmentFile,type='string')
            print 'parentBone',parentBone,'boneName',boneName,'slotName',slotName,'attachmentFile',attachmentFile 
            
            self.createBone(boneName)
            slotPlane = str(cmds.polyPlane(n='%s'%slotName,sx=1,sy=1)[0])

            cmds.setAttr('%s.bone_parent'%boneName,parentBone,type='string')
            cmds.setAttr('%s.bone_slot'%boneName,slotPlane,type='string')
            cmds.setAttr('%s.bone_slot'%boneName,slotPlane,type='string')
            cmds.setAttr('%s.slot_attachment'%boneName,attachmentFile,type='string')

            cmds.setAttr('%s.slot_width'%boneName,newSlotW)
            cmds.setAttr('%s.slot_height'%boneName,newSlotH)
           # print 'attachmentFile',attachmentFile 
           # cmds.setAttr('%s.slot_attachment'%bone,attachmentFile,type='string')
            try:
                self.defineSlot(slotPlane,boneName)
            except:
                pass
            cmds.setAttr('%s.slot_width'%slotPlane,float(newSlotW))
            cmds.setAttr('%s.slot_height'%slotPlane,float(newSlotH))
            cmds.setAttr('%s.slot_attachment'%slotPlane,attachmentFile,type='string')
            cmds.setAttr('%s.scaleX'%slotPlane,float(newSlotW))
            cmds.setAttr('%s.scaleZ'%slotPlane,float(newSlotH))
            cmds.setAttr('%s.rotateX'%slotPlane,90)
            
            slotPlaneShape = cmds.listRelatives(sourceSlotName,c=True,p=False)[0]
            shadingGrps = cmds.listConnections(slotPlaneShape,type='shadingEngine')[0]
            shader = cmds.ls(cmds.listConnections(shadingGrps),materials=1)[0]
            cmds.select(cl=True)
            cmds.select(slotPlane)
            cmds.hyperShade( assign=shader )
            cmds.select(cl=True)
            cmds.copyKey(sourceBoneName)
            cmds.pasteKey(boneName)
            cmds.parent(slotName,boneName)
            cmds.parent(boneName,parentBone)
            

        
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
            cmds.addAttr(slot, ln='spineSlot', numberOfChildren=14, attributeType='compound' )
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
            cmds.addAttr(slot, ln='slot_sequence', sn='s_seq' , at="bool", dv=0,parent='spineSlot' )
            cmds.addAttr(slot, ln='slot_sequenceAmount', attributeType='float',dv=1.0, parent='spineSlot')
            cmds.addAttr(slot, ln='slot_sequenceSpeed', attributeType='float',dv=1.0, parent='spineSlot')
            cmds.addAttr(slot, ln='slot_sequence_random', sn='s_seqRand' , at="bool", dv=0,parent='spineSlot' )


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
       # if cmds.nodeType(shaders) == 'lambert':
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
      #  elif cmds.nodeType(shaders) == 'surfaceShader':

          #  fileNode = cmds.listConnections('%s.outColor' % (shaders[0]), type='file')
        currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
         # print 'currentFile',currentFile
        fileName = currentFile.split("/")[-1]
        fileInSlot = currentFile.split("/")[-1][0:-4]
        searchPath = currentFile.split(fileName)[0]
        allFilesInDir = os.listdir(searchPath)
        
        allSequenceFilesList = []
        for i in allFilesInDir:
            if i.split('.')[-1] in self.imagesFilter:
                print len(i.split('.'))
                if len(i.split('.')) == 3:
                    #print i
                    try:
                        if i.split('.')[0] == fileInSlot.split('.')[0]:
                            allSequenceFilesList.append(i)
                    except:
                        pass
        print 'allSequenceFilesList',allSequenceFilesList
        sequenceAmount = len(allSequenceFilesList)
        if sequenceAmount > 0:
            cmds.setAttr('%s.slot_sequenceAmount'%slot,sequenceAmount)   
        else:
            cmds.setAttr('%s.slot_sequenceAmount'%slot,1)   
                    
       # print 'allFilesInDir',allFilesInDir
          #print 'fileInSlot',fileInSlot
        cmds.setAttr('%s.slot_attachment'%slot,fileInSlot,type='string')
        targetFile = self.spineImagesSpaceLEdit.text() + '/' +fileName
        try:
            if os.path.isfile(targetFile) ==True:
                print "file exist"
                pass
            else:
                #os.remove(targetFile)
                shutil.copyfile(currentFile,targetFile)
        except:
            shutil.copyfile(currentFile,targetFile)
            
        print 'currentFile',currentFile,targetFile
      #  shutil.copyfile(currentFile,targetFile)
        
        print 'fileNode',fileNode
        cmds.setAttr('%s.fileTextureName'%fileNode[0],targetFile,type='string')
        ## copy file sequences
        fileDep = fileName.split('.')
        print 'fileDep',fileDep
        if len(fileDep) == 3:
            fileDigList = ['0','1','2','3','4','5','6','7','8','9']
            fileDigPart = fileDep[-2]
            if len(fileDigPart) == 4:
                if fileDigPart[-1] in fileDigList:
                    for file in allFilesInDir:
                        if file.split('.')[0] == fileDep[0]:
                            sourceSeqFile = searchPath +'/'+file
                            targetSeqFile = self.spineImagesSpaceLEdit.text() + '/'+file
                            try:
                                shutil.copyfile(sourceSeqFile,targetSeqFile)
                            except:
                                pass
        else:
            pass
        
        
        print 'currentFilefffffff',currentFile
                                          
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
        #imagesDir  = 'C:/Temp/images'#"//mcd-3d/data3d/spine_imageSources/"
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
        try:
            os.mkdir('c:/temp')
        except:
            pass
        try: 
            os.mkdir("c:/temp/images")
        except:
            pass     
               
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
      #  print fileName,shortName,fileSize,imageW,imageH
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

          ## define preview image table item
         
          
          
          
    def createImagePlane(self):
        print "createImagePlane"
       # print self.currentImageFullName
        currentImage = self.imageListTable.currentItem().text()
        imageName = currentImage.split('.')[0]
        fileName = self.imageInfoTable.item(0,1).text()
        
        targetFileName = self.spineImagesSpaceLEdit.text() +'/' +currentImage
        imageW = int(self.imageInfoTable.item(3,1).text())
        imageH = int(self.imageInfoTable.item(4,1).text())
        
        slotPlane = str(cmds.polyPlane(n='polyPlane_%s_#'%imageName,sx=1,sy=1)[0])
        cmds.setAttr('%s.rotateX'%slotPlane,90)
        cmds.setAttr('%s.scaleX'%slotPlane,imageW)
        cmds.setAttr('%s.scaleZ'%slotPlane,imageH)
        ###create new shader
        slotShaderName =  imageName + '_shader'
        slotFileName = imageName + '_imageFile'
        slotSG = imageName + '_SG'
        print 'currentImage',currentImage,fileName,targetFileName
        cmds.select(cl=True) 
        
        shader = cmds.shadingNode("lambert",asShader=True,n=slotShaderName)
       # print 'shader',shader
        cmds.select(shader)
        shaderName = cmds.ls(sl=True)[0]
            # shader=cmds.rename(shader,slotShaderName)
       #     print 'shaderName',shaderName,shader
        file_node=cmds.shadingNode("file",asTexture=True,n=slotFileName)
        shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n=slotSG)
        cmds.connectAttr('%s.color' %shader ,'%s.surfaceShader' %shading_group)
        cmds.connectAttr('%s.outColor' %file_node, '%s.color' %shader)
           # print 'fileName',fileName
        
    
        cmds.connectAttr('%s.outTransparency' %file_node, '%s.transparency' %shader)
        cmds.setAttr('%s.fileTextureName'%slotFileName,fileName,type='string')
        cmds.select(cl=True) 
        
        try:
            if os.path.isfile(targetFileName) == True:
                print "file exist"
                
            else:
                #os.remove(targetFile)
                shutil.copyfile(fileName,targetFileName)        
        
        except:
                       
            pass
        cmds.setAttr('%s.fileTextureName'%slotFileName,targetFileName,type='string')

        cmds.select(slotPlane)
        cmds.hyperShade( assign=slotShaderName )
        cmds.select(cl=True)
        print "currentFile",fileName,targetFileName
 
        
          

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

