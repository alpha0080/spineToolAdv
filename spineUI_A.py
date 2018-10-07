

from PySide2 import QtCore, QtGui, QtWidgets#.QFileSystemModel



def test():
    print "test test test"


def buildDock(self):
    
    print "buildDock"
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
    self.workSpaceInfoDock.setMinimumHeight(300)
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




def defineImageButtonDock(self,fontScale):
    
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
                     font-size:%spx;\
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
                     "%(str(fontScale))   
                     
    buttonStyleBLeft = "\
                     QPushButton {\
                     font-size:%spx;\
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
                     "%(str(fontScale))                                      
                                               
                                                            
                                                                         
                                                                                                   
    buttonStyleC = "\
                     QPushButton {\
                     background-color:#333333;\
                     color:#eeeeee;\
                     font-size:%spx;\
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
                     "%(str(fontScale))    

    buttonStyleCMiddle = "\
                     QPushButton {\
                     background-color:#333333;\
                     color:#777777;\
                     font-size:%spx;\
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
                     "%(str(fontScale))                                               

    buttonStyleCRight = "\
                     QPushButton {\
                     background-color:#333333;\
                     color:#777777;\
                     font-size:%spx;\
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
                     "%(str(fontScale))                                                                     
    buttonStyleLeft = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
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
                     "%(str(fontScale))                       
    buttonStyleLeftB = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))   
                     
    buttonStyleRightB = "\
                     QPushButton {\
                     background-color:#778888;\
                     font-size: %spx;\
                     border-top-right-radius:8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#555555;\
                     }\
                     QPushButton:hover{\
                     background-color:#883333;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#883333;\
                     }\
                     QPushButton:pressed{\
                     background-color:#AAAA33;\
                     border-top-left-radius:8px;\
                     border-bottom-left-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#AAAA33;\
                     }\
                     "%(str(fontScale))                                       
                                                                             
                                                                                                         
                                                                                                                                                                 
    lineEditRight = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
    lineEditRightBMiddle = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-style:solid;\
                     border-right-width:1px;\
                     border-color:#555555;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
                     
                                            
    lineEditRightBMiddleDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-style:solid;\
                     border-right-width:1px;\
                     border-color:#555555;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))                                                                                             

    lineEditRightB = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     QComboBox {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     "%(str(fontScale),str(fontScale))   
                                                                                                                                       
                                                                                                                     
    lineEditRightBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     border-top-right-radius: 8px;\
                     border-bottom-right-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
                                                                                                                     
    lineEditBDark = "\
                     QLineEdit {\
                     font-size:%spx;\
                     color:#aaaaaa;\
                     background-color:#333333;\
                     text-align:center;\
                     border-radius: 8px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#333333;\
                     }\
                     "%(str(fontScale))   
                                                                                                                    
                                                                            
    lineEditA = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-radius :6px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))   
                     
    errMsgA = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#888888;\
                     color:#222222;\
                     border-radius :6px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#888888;\
                     text-align:left;\
                     }\
                     "%(str(fontScale))                        
                     
                     
                     
    lineEditB = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-radius :6px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))   
                     
    lineEditC = "\
                     QLineEdit {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-top-right-radius: 6px;\
                     border-bottom-right-radius: 6px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                                                  
                                                                     
    labelA  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#222222;\
                     border-top-left-radius:6px;\
                     border-bottom-left-radius: 6px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                        

    labelTextA  = "\
                     QLabel {\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     QLineEdit {\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale),str(fontScale)) 
    checkA  = "\
                     QCheckBox {\
                     height: 20px;\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale)) 
    spinTextA  = "\
                     QSpinBox {\
                     height: 20px;\
                     font-size:%spx;\
                     text-align:center;\
                     }\
                     "%(str(fontScale)) 


    labelARight  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#222222;\
                     border-top-left-radius:6px;\
                     border-bottom-left-radius: 6px;\
                     border-style:solid;\
                     border-width:0px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))              
    labelAMiddle  = "\
                     QLabel {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#222222;\
                     border-style:solid;\
                     border-left-width:1px;\
                     border-right-width:1px;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))       
    lineEditCMiddle = "\
                     QLineEdit {\
                     height: 30px;\
                     font-size:%spx;\
                     background-color:#333333;\
                     border-style:solid;\
                     border-left-width:1px;\
                     border-right-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                                        
                     
    QGroupBoxA =  "\
                     QGroupBox {\
                     font-size:12px;\
                     font-size:%spx;\
                     background-color:#505050;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))               
                     
    treeA =  "\
                     QTreeWidget {\
                     font-size:%spx;\
                     background-color:#505050;\
                     border-radius :8px;\
                     border-style:solid;\
                     border-width:1px;\
                     border-color:#666666;\
                     text-align:center;\
                     }\
                     "%(str(fontScale))                                                       
        
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
    #self.trimBeforeFrameBtn.clicked.connect(self.trimBeforeFrame)
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
    #self.trimAfterFrameBtn.clicked.connect(self.trimAfterFrame)
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
   # self.trimBetweenFrameBTN.clicked.connect(self.trimBetweenFrame)
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
    #self.alignToFrameBtn.clicked.connect(self.alignKeys)
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
   # self.scaleTimeBtn.clicked.connect(self.scaleFrames)
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
   # self.loopTimeBtn.clicked.connect(self.loopFrames)
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
   # self.defineSelectObjBtn.clicked.connect(self.getSelectSlotBone)
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
   # self.selectAnyTransform.clicked.connect(self.getSelectAnyTransform)
    self.selectAnyTransform.setStyleSheet(buttonStyleB)             



    

    self.renameAllSelectBtn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.renameAllSelectBtn.setGeometry(QtCore.QRect(10, 50, 100, 30))
    self.renameAllSelectBtn.setObjectName("renameAllSelectBtn")
    self.renameAllSelectBtn.setText(QtWidgets.QApplication.translate("MainWindow", "rename selected", None, -1))
   # self.renameAllSelectBtn.clicked.connect(self.renameSelectedBone)
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
   # self.fillet_odd_btn.clicked.connect(self.optionalSelect)
    self.fillet_odd_btn.setStyleSheet(buttonStyleCMiddle)     

    self.fillet_even_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_even_btn.setGeometry(QtCore.QRect(150, 90, 40, 30))
    self.fillet_even_btn.setObjectName("fillet_even_btn")
    self.fillet_even_btn.setCheckable(True)
    self.fillet_even_btn.setChecked(False)  

    self.fillet_even_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#even", None, -1))
    #self.fillet_even_btn.clicked.connect(self.optionalSelect)

    self.fillet_even_btn.setStyleSheet(buttonStyleCMiddle)     
    
    self.fillet_n1_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n1_btn.setGeometry(QtCore.QRect(190, 90, 30, 30))
    self.fillet_n1_btn.setObjectName("fillet_n1_btn")
    self.fillet_n1_btn.setCheckable(True)
    self.fillet_n1_btn.setChecked(False)  
    self.fillet_n1_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#1", None, -1))
    #self.fillet_n1_btn.clicked.connect(self.optionalSelect)
    self.fillet_n1_btn.setStyleSheet(buttonStyleCMiddle)     
     
    self.fillet_n2_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n2_btn.setGeometry(QtCore.QRect(220, 90, 30, 30))
    self.fillet_n2_btn.setObjectName("fillet_n2_btn")
    self.fillet_n2_btn.setCheckable(True)
    self.fillet_n2_btn.setChecked(False)  
    self.fillet_n2_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#2", None, -1))
    #self.fillet_n2_btn.clicked.connect(self.optionalSelect)
    self.fillet_n2_btn.setStyleSheet(buttonStyleCMiddle)      
    self.fillet_n3_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n3_btn.setGeometry(QtCore.QRect(250, 90, 30, 30))
    self.fillet_n3_btn.setObjectName("fillet_n3_btn")
    self.fillet_n3_btn.setCheckable(True)
    self.fillet_n3_btn.setChecked(False)  
    self.fillet_n3_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#3", None, -1))
   # self.fillet_n3_btn.clicked.connect(self.optionalSelect)
    self.fillet_n3_btn.setStyleSheet(buttonStyleCMiddle)                   
                
    self.fillet_n4_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n4_btn.setGeometry(QtCore.QRect(280, 90, 30, 30))
    self.fillet_n4_btn.setObjectName("fillet_n4_btn")
    self.fillet_n4_btn.setCheckable(True)
    self.fillet_n4_btn.setChecked(False)  
    self.fillet_n4_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#4", None, -1))
  #  self.fillet_n4_btn.clicked.connect(self.optionalSelect)
    self.fillet_n4_btn.setStyleSheet(buttonStyleCMiddle)                   
    
                                 
    self.fillet_n5_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n5_btn.setGeometry(QtCore.QRect(310, 90, 30, 30))
    self.fillet_n5_btn.setObjectName("fillet_n5_btn")
    self.fillet_n5_btn.setCheckable(True)
    self.fillet_n5_btn.setChecked(False)  
    self.fillet_n5_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#5", None, -1))
   # self.fillet_n5_btn.clicked.connect(self.optionalSelect)
    self.fillet_n5_btn.setStyleSheet(buttonStyleCMiddle)                   
                                                                        
    self.fillet_n6_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n6_btn.setGeometry(QtCore.QRect(340, 90, 30, 30))
    self.fillet_n6_btn.setObjectName("fillet_n6_btn")
    self.fillet_n6_btn.setCheckable(True)
    self.fillet_n6_btn.setChecked(False)  
    self.fillet_n6_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#6", None, -1))
   # self.fillet_n6_btn.clicked.connect(self.optionalSelect)
    self.fillet_n6_btn.setStyleSheet(buttonStyleCMiddle)                                          
                                        
    self.fillet_n7_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n7_btn.setGeometry(QtCore.QRect(370, 90, 30, 30))
    self.fillet_n7_btn.setObjectName("fillet_n7_btn")
    self.fillet_n7_btn.setCheckable(True)
    self.fillet_n7_btn.setChecked(False)  
    self.fillet_n7_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#7", None, -1))
   # self.fillet_n7_btn.clicked.connect(self.optionalSelect)
    self.fillet_n7_btn.setStyleSheet(buttonStyleCMiddle)       
                                        
    self.fillet_n8_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n8_btn.setGeometry(QtCore.QRect(400, 90, 30, 30))
    self.fillet_n8_btn.setObjectName("fillet_n8_btn")
    self.fillet_n8_btn.setCheckable(True)
    self.fillet_n8_btn.setChecked(False)  
    self.fillet_n8_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#8", None, -1))
   # self.fillet_n8_btn.clicked.connect(self.optionalSelect)
    self.fillet_n8_btn.setStyleSheet(buttonStyleCMiddle)   
    
                                        
    self.fillet_n9_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n9_btn.setGeometry(QtCore.QRect(430, 90, 30, 30))
    self.fillet_n9_btn.setObjectName("fillet_n9_btn")
    self.fillet_n9_btn.setCheckable(True)
    self.fillet_n9_btn.setChecked(False)  
    self.fillet_n9_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#9", None, -1))
    #self.fillet_n9_btn.clicked.connect(self.optionalSelect)
    self.fillet_n9_btn.setStyleSheet(buttonStyleCMiddle)   
    
                                        
    self.fillet_n0_btn = QtWidgets.QPushButton(self.filletSelectGrp)
    self.fillet_n0_btn.setGeometry(QtCore.QRect(460, 90, 30, 30))
    self.fillet_n0_btn.setObjectName("fillet_n0_btn")
    self.fillet_n0_btn.setCheckable(True)
    self.fillet_n0_btn.setChecked(False)  
    self.fillet_n0_btn.setText(QtWidgets.QApplication.translate("MainWindow", "#0", None, -1))
   # self.fillet_n0_btn.clicked.connect(self.optionalSelect)
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
   # self.setModAllFrameBTN.clicked.connect(self.setFrameFilletToAll)
    self.setModAllFrameBTN.setStyleSheet(buttonStyleB)     
    
    self.setModFirstFrameBTN = QtWidgets.QPushButton(self.randomFrameKeyGrp)
    self.setModFirstFrameBTN.setGeometry(QtCore.QRect(65, 10, 50, 30))
    self.setModFirstFrameBTN.setObjectName("setModFirstFrameBTN")
    self.setModFirstFrameBTN.setText(QtWidgets.QApplication.translate("MainWindow", "first", None, -1))
    #self.setModFirstFrameBTN.clicked.connect(self.setFrameFilletToFirst)
    self.setModFirstFrameBTN.setStyleSheet(buttonStyleB)   
          
    self.setModLastFrameBTN = QtWidgets.QPushButton(self.randomFrameKeyGrp)
    self.setModLastFrameBTN.setGeometry(QtCore.QRect(120, 10, 50, 30))
    self.setModLastFrameBTN.setObjectName("setModLastFrameBTN")
    self.setModLastFrameBTN.setText(QtWidgets.QApplication.translate("MainWindow", "last", None, -1))
    #self.setModLastFrameBTN.clicked.connect(self.setFrameFilletToLast)
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
    #self.modReplaceModBtn.clicked.connect(self.changeRelaceMode)
    self.modReplaceModBtn.setStyleSheet(buttonStyleC)                  
    
    self.modOffsetBtn = QtWidgets.QPushButton(self.randomFrameKeyGrp)
    self.modOffsetBtn.setGeometry(QtCore.QRect(405, 10, 30, 30))
    self.modOffsetBtn.setObjectName("modOffsetBtn")
    self.modOffsetBtn.setCheckable(True)
    self.modOffsetBtn.setChecked(True)
    self.modOffsetBtn.setFlat(False)
    self.modOffsetBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Of", None, -1))
   # self.modOffsetBtn.clicked.connect(self.changeOffsetMode)
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
   # self.modTransXBtn.clicked.connect(self.defineModX)
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
    #self.modTransYBtn.clicked.connect(self.defineModY)
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
   # self.modTransZBtn.clicked.connect(self.defineModZ)
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
   # self.modRotateXBtn.clicked.connect(self.defineModRX)
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
   # self.modRotateYBtn.clicked.connect(self.defineModRY)
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
   # self.modRotateZBtn.clicked.connect(self.defineModRZ)
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
    #self.modScaleXBtn.clicked.connect(self.defineModSX)
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
   # self.modScaleYBtn.clicked.connect(self.defineModSY)
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
   # self.modScaleZBtn.clicked.connect(self.defineModSZ)
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
    self.modScaleAllBtn.setText(QtWidgets.QApplication.translate("MainWindow", "mod Sx Sy", None, -1))
    #self.modScaleAllBtn.clicked.connect(self.defineModSAll)
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
    #self.modAlphaGainBtn.clicked.connect(self.defineModAlpha)
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
   # self.modColorBtn.clicked.connect(self.createRootCtrl)
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
   # self.modFadeBtn.clicked.connect(self.createRootCtrl)
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
   # self.selectImageFolderBtn.clicked.connect(self.setImageSourceToDatabase)
    self.selectImageFolderBtn.setStyleSheet(buttonStyleC)     

    self.selectImageFromDiskBTN = QtWidgets.QPushButton(self.dockSpineItemTree)
    self.selectImageFromDiskBTN.setGeometry(QtCore.QRect(85, 20, 70,30))
    self.selectImageFromDiskBTN.setObjectName("selectImageFromDisk")
    self.selectImageFromDiskBTN.setText(QtWidgets.QApplication.translate("MainWindow", "Disk", None, -1))
    self.selectImageFromDiskBTN.setCheckable(True)
    self.selectImageFromDiskBTN.setChecked(False)
    self.selectImageFromDiskBTN.setFlat(False)
   # self.selectImageFromDiskBTN.clicked.connect(self.setToDisk)
    self.selectImageFromDiskBTN.setStyleSheet(buttonStyleC)     

    self.selectSpineJobBtn = QtWidgets.QPushButton(self.dockSpineItemTree)
    self.selectSpineJobBtn.setGeometry(QtCore.QRect(160, 20, 70,30))
    self.selectSpineJobBtn.setObjectName("selectSpineJobBtn")
    self.selectSpineJobBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Spine Job", None, -1))
    self.selectSpineJobBtn.setCheckable(True)
    self.selectSpineJobBtn.setChecked(False)
    self.selectSpineJobBtn.setFlat(False)       
   # self.selectSpineJobBtn.clicked.connect(self.setToSpineJobTree)
    self.selectSpineJobBtn.setStyleSheet(buttonStyleC)     

    self.openSelectedFolderBtn = QtWidgets.QPushButton(self.dockSpineItemTree)
    self.openSelectedFolderBtn.setGeometry(QtCore.QRect(250, 20, 40,30))
    self.openSelectedFolderBtn.setObjectName("selectSpineJobBtn")
    self.openSelectedFolderBtn.setText(QtWidgets.QApplication.translate("MainWindow", "--", None, -1))
    #self.openSelectedFolderBtn.clicked.connect(self.openSelectedFolder)
    self.openSelectedFolderBtn.setStyleSheet(buttonStyleC)                  
                                      
                  
    self.spineItemTree = QtWidgets.QTreeWidget(self.dockSpineItemTree)
    self.spineItemTree.setGeometry(QtCore.QRect(10, 60, 280, 550))
    self.spineItemTree.setDragEnabled(True)
    self.spineItemTree.setDragDropOverwriteMode(True)
    self.spineItemTree.header().setVisible(False)

    self.spineItemTree.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
    self.spineItemTree.setObjectName("spineItemTree")
    self.spineItemTree.setStyleSheet(treeA)     
   # self.spineItemTree.itemClicked.connect(self.defineImageTableFromSel)

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
    self.environmentSetGrp.setGeometry(QtCore.QRect(10, 20, 530, 280))
    self.environmentSetGrp.setObjectName("environmentSetGrp")
    self.environmentSetGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   
    self.environmentSetGrp.setStyleSheet(QGroupBoxA)     
    self.environmentSetGrp.setVisible(True)
    

    self.openSpineMayaFileBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.openSpineMayaFileBtn.setGeometry(QtCore.QRect(10, 20, 110,30))
    self.openSpineMayaFileBtn.setObjectName("openSpineMayaFileBtn")
    self.openSpineMayaFileBtn.setText(QtWidgets.QApplication.translate("MainWindow", "open Maya file", None, -1))
   # self.openSpineMayaFileBtn.clicked.connect(self.openMayaFile)
    self.openSpineMayaFileBtn.setStyleSheet(buttonStyleLeftB)     


    self.openMayaFileLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
    self.openMayaFileLEdit.setGeometry(QtCore.QRect(120, 20, 370, 30))
    self.openMayaFileLEdit.setObjectName("spineWorkSpaceLEdit")
    self.openMayaFileLEdit.setAlignment(QtCore.Qt.AlignCenter)
    self.openMayaFileLEdit.setText('')
    self.openMayaFileLEdit.setStyleSheet(lineEditRightBMiddle)  
    
    self.openMayaFileFolder = QtWidgets.QPushButton(self.environmentSetGrp)
    self.openMayaFileFolder.setGeometry(QtCore.QRect(490, 20, 30,30))
    self.openMayaFileFolder.setObjectName("openMayaFileFolder")
    self.openMayaFileFolder.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
  #  self.openMayaFileFolder.clicked.connect(self.openSpineFolder)
    self.openMayaFileFolder.setStyleSheet(buttonStyleRightB)            
                      
           
                  
                                
    
    
    self.selectSpineWorkSpaceBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.selectSpineWorkSpaceBtn.setGeometry(QtCore.QRect(10, 80, 110,30))
    self.selectSpineWorkSpaceBtn.setObjectName("selectSpineWorkSpaceBtn")
    self.selectSpineWorkSpaceBtn.setText(QtWidgets.QApplication.translate("MainWindow", "work space", None, -1))
   # self.selectSpineWorkSpaceBtn.clicked.connect(self.defineSpineWorkSpace)
    self.selectSpineWorkSpaceBtn.setStyleSheet(buttonStyleLeftB)     


    self.spineWorkSpaceLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
    self.spineWorkSpaceLEdit.setGeometry(QtCore.QRect(120, 80, 370, 30))
    self.spineWorkSpaceLEdit.setObjectName("spineWorkSpaceLEdit")
    self.spineWorkSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
    self.spineWorkSpaceLEdit.setText('')
    self.spineWorkSpaceLEdit.setStyleSheet(lineEditRightBMiddle)  
    
    self.OpenSpineDirBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.OpenSpineDirBtn.setGeometry(QtCore.QRect(490, 80, 30,30))
    self.OpenSpineDirBtn.setObjectName("OpenSpineDirBtn")
    self.OpenSpineDirBtn.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
   # self.OpenSpineDirBtn.clicked.connect(self.openSpineFolder)
    self.OpenSpineDirBtn.setStyleSheet(buttonStyleRightB)            
              
          
                
    
    
    self.selectImageDitBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.selectImageDitBtn.setGeometry(QtCore.QRect(10, 120, 110,30))
    self.selectImageDitBtn.setObjectName("selectImageDitBtn")
    self.selectImageDitBtn.setText(QtWidgets.QApplication.translate("MainWindow", "images Folder", None, -1))
   # self.selectImageDitBtn.clicked.connect(self.defineSpineWorkSpace)
    self.selectImageDitBtn.setStyleSheet(buttonStyleLeftB)     


    self.spineImagesSpaceLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
    self.spineImagesSpaceLEdit.setGeometry(QtCore.QRect(120, 120, 370, 30))
    self.spineImagesSpaceLEdit.setObjectName("spineImagesSpaceLEdit")
    self.spineImagesSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
    self.spineImagesSpaceLEdit.setText('')
    self.spineImagesSpaceLEdit.setStyleSheet(lineEditRightBMiddle)     
    
    self.OpenImageDirBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.OpenImageDirBtn.setGeometry(QtCore.QRect(490, 120, 30,30))
    self.OpenImageDirBtn.setObjectName("OpenImageDirBtn")
    self.OpenImageDirBtn.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
    #self.OpenImageDirBtn.clicked.connect(self.openImagesFolder)
    self.OpenImageDirBtn.setStyleSheet(buttonStyleRightB)            
    
    
    
    
    
    self.selectExportFolderBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.selectExportFolderBtn.setGeometry(QtCore.QRect(10, 160, 110,30))
    self.selectExportFolderBtn.setObjectName("selectExportFolderBtn")
    self.selectExportFolderBtn.setText(QtWidgets.QApplication.translate("MainWindow", "export Folder", None, -1))
   # self.selectExportFolderBtn.clicked.connect(self.defineSpineWorkSpace)
    self.selectExportFolderBtn.setStyleSheet(buttonStyleLeftB)     


    self.spineExportSpaceLEdit = QtWidgets.QLineEdit(self.environmentSetGrp)
    self.spineExportSpaceLEdit.setGeometry(QtCore.QRect(120, 160, 370, 30))
    self.spineExportSpaceLEdit.setObjectName("spineExportSpaceLEdit")
    self.spineExportSpaceLEdit.setAlignment(QtCore.Qt.AlignCenter)
    self.spineExportSpaceLEdit.setText('')
    self.spineExportSpaceLEdit.setStyleSheet(lineEditRightBMiddle)  

    self.OpenExportDirBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.OpenExportDirBtn.setGeometry(QtCore.QRect(490, 160, 30,30))
    self.OpenExportDirBtn.setObjectName("OpenExportDirBtn")
    self.OpenExportDirBtn.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
   # self.OpenExportDirBtn.clicked.connect(self.openExportFolder)
    self.OpenExportDirBtn.setStyleSheet(buttonStyleRightB)            
    


    self.createBGBtn = QtWidgets.QPushButton(self.environmentSetGrp)
    self.createBGBtn.setGeometry(QtCore.QRect(10, 200, 110, 30))
    self.createBGBtn.setObjectName("createBGBtn")
    self.createBGBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Define BG", None, -1))
   # self.createBGBtn.clicked.connect(self.defineCreateBGBtn)
    self.createBGBtn.setStyleSheet(buttonStyleLeftB)


    self.createBG_comboBox = QtWidgets.QComboBox(self.environmentSetGrp)
    self.createBG_comboBox.setGeometry(QtCore.QRect(120, 200, 400, 30))
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
    self.jointSizeLabel.setGeometry(QtCore.QRect(30, 240, 60, 30))
    self.jointSizeLabel.setObjectName("jointSizeLabel")
    self.jointSizeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "joint size", None, -1))
    self.jointSizeLabel.setStyleSheet(labelTextA)

   # self.jointSizeValueLabel = QtWidgets.QLabel(self.environmentSetGrp)
   # self.jointSizeValueLabel.setGeometry(QtCore.QRect(100, 240, 60, 30))
   # self.jointSizeValueLabel.setObjectName("jointSizeValueLabel")
   # self.jointSizeValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", "10", None, -1))
   # self.jointSizeValueLabel.setStyleSheet(labelTextA)
    
    self.jontSizeLEdit = QtWidgets.QSpinBox(self.environmentSetGrp)
    self.jontSizeLEdit.setGeometry(QtCore.QRect(100, 240, 60, 30))
    self.jontSizeLEdit.setObjectName("jontSizeLEdit")
    self.jontSizeLEdit.setAlignment(QtCore.Qt.AlignCenter)
    self.jontSizeLEdit.setProperty("value", 10)
    self.jontSizeLEdit.setStyleSheet(spinTextA)  
    
   # self.horizontalSlider = QtWidgets.QSlider(self.environmentSetGrp)
   # self.horizontalSlider.setGeometry(QtCore.QRect(150, 240, 300, 30))
   # self.horizontalSlider.setMinimum(1)
   # self.horizontalSlider.setMaximum(100)
   # self.horizontalSlider.setProperty("value", 10)
   # self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
   # self.horizontalSlider.setObjectName("horizontalSlider")
    self.vertexSizeLabel = QtWidgets.QLabel(self.environmentSetGrp)
    self.vertexSizeLabel.setGeometry(QtCore.QRect(180, 240, 150, 30))
    self.vertexSizeLabel.setObjectName("vertexSizeLabel")
    self.vertexSizeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "vertex size", None, -1))
    self.vertexSizeLabel.setStyleSheet(labelTextA)

    self.vertexSizeSB = QtWidgets.QSpinBox(self.environmentSetGrp)
    self.vertexSizeSB.setGeometry(QtCore.QRect(270, 240, 60, 30))
    self.vertexSizeSB.setObjectName("vertexSizeSB")
    self.vertexSizeSB.setAlignment(QtCore.Qt.AlignCenter)
    self.vertexSizeSB.setProperty("value", 3)
    self.vertexSizeSB.setStyleSheet(spinTextA)  
    


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
    #self.initialSpineRootBtn.clicked.connect(self.defineSpineRootSkeleton)
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
   # self.createCharacterGrpBTn.clicked.connect(self.createCharacterGrp)
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
   # self.createRootBtn.clicked.connect(self.createRootCtrl)
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
   # self.createImagePlaneBtn.clicked.connect(self.createImagePlane)
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
   # self.defineMeshBtn.clicked.connect(self.getSkinData)
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
   # self.createSlotBtn.clicked.connect(self.createSlot)              
    self.createSlotBtn.setStyleSheet(buttonStyleB)   
    

 
    
    self.createBoneBtn = QtWidgets.QPushButton(self.defineSpineSlotBoneGrpBox)
    self.createBoneBtn.setGeometry(QtCore.QRect(30, 10, 120, 30))
    self.createBoneBtn.setObjectName("createBoneBtn")
    self.createBoneBtn.setText(QtWidgets.QApplication.translate("MainWindow", "create Clean Bone", None, -1))
    #self.createBoneBtn.clicked.connect(self.createCleanBone)
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
    self.slotAmountLabel.setStyleSheet(labelTextA)     
    
    
    
    self.amountSliderNumLEdit = QtWidgets.QLineEdit(self.defineSpineSlotBoneGrpBox)
    self.amountSliderNumLEdit.setGeometry(QtCore.QRect(30, 110, 60, 30))
    self.amountSliderNumLEdit.setObjectName("amountSliderNumLEdit")
    self.amountSliderNumLEdit.setAlignment(QtCore.Qt.AlignCenter)
    self.amountSliderNumLEdit.setText('1')
   # self.amountSliderNumLEdit.textChanged.connect(self.slotAmountEditChange)
    self.amountSliderNumLEdit.setStyleSheet(lineEditA)            
    

    self.amountSlotSlider = QtWidgets.QSlider(self.defineSpineSlotBoneGrpBox)
    self.amountSlotSlider.setGeometry(QtCore.QRect(100, 110, 250, 30))
    self.amountSlotSlider.setMinimum(1)
    self.amountSlotSlider.setMaximum(300)
    self.amountSlotSlider.setProperty("value", 1)
    self.amountSlotSlider.setOrientation(QtCore.Qt.Horizontal)
    self.amountSlotSlider.setObjectName("amountSlotSlider")
   # self.amountSlotSlider.valueChanged.connect(self.slotAmountSliderChange)
    
    
    
    self.enableDynaSlotCheck = QtWidgets.QCheckBox(self.defineSpineSlotBoneGrpBox)
    self.enableDynaSlotCheck.setGeometry(QtCore.QRect(30, 145, 200, 20))
    #self.enableDynaSlotCheck.setChecked(True)
    self.enableDynaSlotCheck.setObjectName("enableDynaSlotCheck")
    self.enableDynaSlotCheck.setText(QtWidgets.QApplication.translate("MainWindow", "Dynamic Slot", None, -1))
    self.enableDynaSlotCheck.setStyleSheet(checkA)   

 
    
    
    
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
             font-size:%spx;\
             text-align:left;\
             }\
             "%(str(fontScale))  
    optionLabelA  = "\
                     QLabel{\
                     font-size:%spx;\
                     }\
                     QLineEdit{\
                     font-size:%spx;\
                     };\
                     "%(str(fontScale),str(fontScale)) 
    optionEditA  = "\
                     QLineEdit {\
                     font-size:%spx;\
                     background-color:#333333;\
                     color:#aaaaaa;\
                     border-radius:3px;\
                     border-style:solid;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     QLineEdit::hover{\
                     font-size:%spx;\
                     background-color:#993333;\
                     color:#aaaaaa;\
                     border-radius:3px;\
                     border-style:solid;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     QLineEdit:read-only {\
                     font-size:%spx;\
                     background-color:#777777;\
                     color:#333333;\
                     border-radius:3px;\
                     border-style:solid;\
                     border-color:#777777;\
                     text-align:center;\
                     }\
                     "%(str(fontScale),str(fontScale),str(fontScale))

    
    self.slotDynaStartFrame = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.slotDynaStartFrame.setGeometry(QtCore.QRect(20, 10, 60, 20))
    self.slotDynaStartFrame.setObjectName("slotDynaStartFrame")
    self.slotDynaStartFrame.setText(QtWidgets.QApplication.translate("MainWindow", "Start Frame", None, -1))  
    self.slotDynaStartFrame.setStyleSheet(labelTextA)   
    
    self.lineEdit_shapeStartFrame = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_shapeStartFrame.setGeometry(QtCore.QRect(90, 10, 40, 20))
    self.lineEdit_shapeStartFrame.setObjectName("lineEdit_shapeStartFrame")       
    self.lineEdit_shapeStartFrame.setText(QtWidgets.QApplication.translate("MainWindow", "1.0", None, -1))  
    self.lineEdit_shapeStartFrame.setStyleSheet(labelTextA)   
   
    
    self.slotDynaEndFrame = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.slotDynaEndFrame.setGeometry(QtCore.QRect(140, 10, 60, 20))
    self.slotDynaEndFrame.setObjectName("slotDynaEndFrame")
    self.slotDynaEndFrame.setText(QtWidgets.QApplication.translate("MainWindow", "End Frame", None, -1))  
    self.slotDynaEndFrame.setStyleSheet(labelTextA)   

    self.lineEdit_shapeEndFrame = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_shapeEndFrame.setGeometry(QtCore.QRect(210, 10, 40, 20))
    self.lineEdit_shapeEndFrame.setObjectName("lineEdit_shapeEndFrame")
    self.lineEdit_shapeEndFrame.setText(QtWidgets.QApplication.translate("MainWindow", "20.0", None, -1))  
    self.lineEdit_shapeEndFrame.setStyleSheet(labelTextA)   

    self.checkBox_offsetRandom = QtWidgets.QCheckBox(self.dynamicSlotGrp)
    self.checkBox_offsetRandom.setGeometry(QtCore.QRect(270, 10, 73, 20))
    self.checkBox_offsetRandom.setChecked(True)
    self.checkBox_offsetRandom.setObjectName("checkBox_offsetRandom")
    self.checkBox_offsetRandom.setText(QtWidgets.QApplication.translate("MainWindow", "random", None, -1))
    self.checkBox_offsetRandom.setStyleSheet(checkA)   





    #### dyna Raditional
    self.radioButton_createRad = QtWidgets.QRadioButton(self.dynamicSlotGrp)
    self.radioButton_createRad.setGeometry(QtCore.QRect(20, 40, 70, 20))
    self.radioButton_createRad.setChecked(True)
    self.radioButton_createRad.setObjectName("radioButton_createRad")
    self.radioButton_createRad.setText(QtWidgets.QApplication.translate("MainWindow", "Radiation", None, -1))
    self.radioButton_createRad.setStyleSheet(radioBtnStyleA)     
    
    self.RValueLabel = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.RValueLabel.setGeometry(QtCore.QRect(100, 40, 30, 20))
    self.RValueLabel.setObjectName("RValueLabel")
    self.RValueLabel.setText(QtWidgets.QApplication.translate("MainWindow", "R:", None, -1))
    self.RValueLabel.setStyleSheet(optionLabelA)   
    
    self.lineEdit_RadiusA = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_RadiusA.setEnabled(True)
    self.lineEdit_RadiusA.setGeometry(QtCore.QRect(115, 40, 40, 20))
    self.lineEdit_RadiusA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
    self.lineEdit_RadiusA.setObjectName("lineEdit_RadiusA") 
    self.lineEdit_RadiusA.setStyleSheet(optionLabelA)   

    #### dyna Square
    self.radioButton_createSquare = QtWidgets.QRadioButton(self.dynamicSlotGrp)
    self.radioButton_createSquare.setGeometry(QtCore.QRect(20, 70, 70, 20))
    self.radioButton_createSquare.setObjectName("radioButton_createSquare")  
    self.radioButton_createSquare.setText(QtWidgets.QApplication.translate("MainWindow", "Square", None, -1))
    self.radioButton_createSquare.setStyleSheet(radioBtnStyleA)        
     
    self.lineEdit_widthSquare = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_widthSquare.setEnabled(False)
    self.lineEdit_widthSquare.setGeometry(QtCore.QRect(115, 70, 40, 20))
    self.lineEdit_widthSquare.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
    self.lineEdit_widthSquare.setObjectName("lineEdit_widthSquare")
    self.lineEdit_widthSquare.setStyleSheet(optionLabelA)   
    
    self.label_WidthSquare = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_WidthSquare.setGeometry(QtCore.QRect(100, 70, 30, 20))
    self.label_WidthSquare.setObjectName("label_WidthSquare")
    self.label_WidthSquare.setText(QtWidgets.QApplication.translate("MainWindow", "W:", None, -1))
    self.label_WidthSquare.setStyleSheet(optionLabelA)   

    self.lineEdit_HeightA = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_HeightA.setEnabled(False)
    self.lineEdit_HeightA.setGeometry(QtCore.QRect(175,70, 40, 20))
    self.lineEdit_HeightA.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))
    self.lineEdit_HeightA.setObjectName("lineEdit_HeightA")                  
    self.lineEdit_HeightA.setStyleSheet(optionLabelA)   
    

    self.label_HeighthSquare = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_HeighthSquare.setGeometry(QtCore.QRect(160, 70, 30, 20))
    self.label_HeighthSquare.setObjectName("label_HeighthSquare")                    
    self.label_HeighthSquare.setText(QtWidgets.QApplication.translate("MainWindow", "H:", None, -1))
    self.label_HeighthSquare.setStyleSheet(optionLabelA)                      
                    
    self.checkBox_squareFillIn = QtWidgets.QCheckBox(self.dynamicSlotGrp)
    self.checkBox_squareFillIn.setGeometry(QtCore.QRect(240, 70, 70, 20))
    self.checkBox_squareFillIn.setChecked(False)
    self.checkBox_squareFillIn.setObjectName("checkBox_squareFillIn")   
    self.checkBox_squareFillIn.setText(QtWidgets.QApplication.translate("MainWindow", "Fill in", None, -1))
    self.checkBox_squareFillIn.setStyleSheet(checkA)   

    self.checkBox_squareAimO = QtWidgets.QCheckBox(self.dynamicSlotGrp)
    self.checkBox_squareAimO.setGeometry(QtCore.QRect(300, 70, 70, 20))
    self.checkBox_squareAimO.setChecked(False)
    self.checkBox_squareAimO.setObjectName("checkBox_squareAimO")   
    self.checkBox_squareAimO.setText(QtWidgets.QApplication.translate("MainWindow", "Aim O.O", None, -1))
    self.checkBox_squareAimO.setStyleSheet(checkA)                             
       
### set dyna sector
        
    self.radioButton_createSector = QtWidgets.QRadioButton(self.dynamicSlotGrp)
    self.radioButton_createSector.setGeometry(QtCore.QRect(20, 100, 70, 20))
    self.radioButton_createSector.setObjectName("radioButton_createSector")
    self.radioButton_createSector.setText(QtWidgets.QApplication.translate("MainWindow", "Sector", None, -1))
    self.radioButton_createSector.setStyleSheet(radioBtnStyleA)        

                                                                                                          
    self.label_dynaSectorDegree = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_dynaSectorDegree.setGeometry(QtCore.QRect(100, 100, 30, 20))
    self.label_dynaSectorDegree.setObjectName("label_dynaSectorDegree")                                                
    self.label_dynaSectorDegree.setText(QtWidgets.QApplication.translate("MainWindow", "D:", None, -1))
    self.label_dynaSectorDegree.setStyleSheet(optionLabelA)                      
                                                                 
    self.lineEdit_AngleA_start = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_AngleA_start.setEnabled(False)
    self.lineEdit_AngleA_start.setGeometry(QtCore.QRect(115, 100, 40, 20))
    self.lineEdit_AngleA_start.setText(QtWidgets.QApplication.translate("MainWindow", "-90", None, -1))
    self.lineEdit_AngleA_start.setObjectName("lineEdit_AngleA_start")
    self.lineEdit_AngleA_start.setStyleSheet(optionLabelA)   

    self.lineEdit_AngleA_end = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_AngleA_end.setEnabled(False)
    self.lineEdit_AngleA_end.setGeometry(QtCore.QRect(175, 100, 40, 20))
    self.lineEdit_AngleA_end.setText(QtWidgets.QApplication.translate("MainWindow", "90", None, -1))
    self.lineEdit_AngleA_end.setObjectName("lineEdit_AngleA_end")    
    self.lineEdit_AngleA_end.setStyleSheet(optionLabelA)   


#### set dyna direction
    self.radioButton_createDirection = QtWidgets.QRadioButton(self.dynamicSlotGrp)
    self.radioButton_createDirection.setGeometry(QtCore.QRect(20, 130, 70, 20))
    self.radioButton_createDirection.setObjectName("radioButton_createDirection")
    
    self.radioButton_createDirection.setText(QtWidgets.QApplication.translate("MainWindow", "Direction", None, -1))
    self.radioButton_createDirection.setStyleSheet(radioBtnStyleA)        

    self.label_dynDirectionX = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_dynDirectionX.setGeometry(QtCore.QRect(100, 130, 30, 20))
    self.label_dynDirectionX.setObjectName("label_dynDirectionX")
    self.label_dynDirectionX.setText(QtWidgets.QApplication.translate("MainWindow", "X:", None, -1))
    self.label_dynDirectionX.setStyleSheet(optionLabelA)    
    
                      
    self.lineEdit_DirectionX = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_DirectionX.setEnabled(False)
    self.lineEdit_DirectionX.setGeometry(QtCore.QRect(115, 130, 40, 20))
    self.lineEdit_DirectionX.setObjectName("lineEdit_DirectionX")    
    self.lineEdit_DirectionX.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))                                                       
    self.lineEdit_DirectionX.setStyleSheet(optionLabelA)   

    self.label_dynDirectionY = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_dynDirectionY.setGeometry(QtCore.QRect(160, 130, 30, 20))
    self.label_dynDirectionY.setObjectName("label_dynDirectionY")
    self.label_dynDirectionY.setText(QtWidgets.QApplication.translate("MainWindow", "Y:", None, -1))
    self.label_dynDirectionY.setStyleSheet(optionLabelA)    
    
    self.lineEdit_DirectionY = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_DirectionY.setEnabled(False)
    self.lineEdit_DirectionY.setGeometry(QtCore.QRect(175, 130, 40, 20))
    self.lineEdit_DirectionY.setObjectName("lineEdit_DirectionY")
    self.lineEdit_DirectionY.setText(QtWidgets.QApplication.translate("MainWindow", "500", None, -1))  
    self.lineEdit_DirectionY.setStyleSheet(optionLabelA)   
    
    self.label_dynDirectionD = QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_dynDirectionD.setGeometry(QtCore.QRect(220, 130, 30, 20))
    self.label_dynDirectionD.setObjectName("label_dynDirectionD")     
    self.label_dynDirectionD.setText(QtWidgets.QApplication.translate("MainWindow", "D:", None, -1))
    self.label_dynDirectionD.setStyleSheet(optionLabelA)    
    
   
    self.lineEdit_directionDegree = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_directionDegree.setEnabled(False)
    self.lineEdit_directionDegree.setGeometry(QtCore.QRect(240, 130, 40, 20))
    self.lineEdit_directionDegree.setObjectName("lineEdit_directionDegree") 
    self.lineEdit_directionDegree.setStyleSheet(optionLabelA)   
    self.lineEdit_directionDegree.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
    self.lineEdit_directionDegree.setStyleSheet(optionLabelA)   

    
    
    self.label_dynDirectionS= QtWidgets.QLabel(self.dynamicSlotGrp)
    self.label_dynDirectionS.setGeometry(QtCore.QRect(285, 130, 30, 20))
    self.label_dynDirectionS.setObjectName("label_dynDirectionS")
    self.label_dynDirectionS.setText(QtWidgets.QApplication.translate("MainWindow", "S:", None, -1))
    self.label_dynDirectionS.setStyleSheet(optionLabelA)    
   
    self.lineEdit_directionSpread = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_directionSpread.setEnabled(False)
    self.lineEdit_directionSpread.setGeometry(QtCore.QRect(300, 130, 40, 20))
    self.lineEdit_directionSpread.setObjectName("lineEdit_directionSpread")
    self.lineEdit_directionSpread.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
    self.lineEdit_directionSpread.setStyleSheet(optionLabelA)   



#### dyna set follow curve
    self.radioButton_createFollowCurve = QtWidgets.QRadioButton(self.dynamicSlotGrp)
    self.radioButton_createFollowCurve.setGeometry(QtCore.QRect(20, 160, 110, 20))
    self.radioButton_createFollowCurve.setObjectName("radioButton_createFollowCurve")
    self.radioButton_createFollowCurve.setText(QtWidgets.QApplication.translate("MainWindow", "Follow Curve", None, -1))
    self.radioButton_createFollowCurve.setStyleSheet(radioBtnStyleA)        


    self.lineEdit_selectCurve = QtWidgets.QLineEdit(self.dynamicSlotGrp)
    self.lineEdit_selectCurve.setEnabled(False)
    self.lineEdit_selectCurve.setGeometry(QtCore.QRect(120, 160, 220, 20))
    self.lineEdit_selectCurve.setObjectName("lineEdit_selectCurve")
    self.lineEdit_selectCurve.setText(QtWidgets.QApplication.translate("MainWindow", "select curve", None, -1))
    self.lineEdit_selectCurve.setStyleSheet(optionLabelA)   


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
    self.label_dynCurveKeys.setStyleSheet(labelTextA)    
   
    self.lineEdit_keys = QtWidgets.QLineEdit(self.groupBox_keysOption)
    self.lineEdit_keys.setEnabled(False)
    self.lineEdit_keys.setGeometry(QtCore.QRect(60, 10, 40, 16))
    self.lineEdit_keys.setObjectName("lineEdit_keysA")    
    self.lineEdit_keys.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
    self.lineEdit_keys.setStyleSheet(optionLabelA)    
    
    
    self.label_dynCurveNoise = QtWidgets.QLabel(self.groupBox_keysOption)
    self.label_dynCurveNoise.setGeometry(QtCore.QRect(20, 35, 41, 16))
    self.label_dynCurveNoise.setObjectName("label_dynCurveNoise")
    self.label_dynCurveNoise.setText(QtWidgets.QApplication.translate("MainWindow", "Noise:", None, -1))
    self.label_dynCurveNoise.setStyleSheet(labelTextA)    
    
    self.lineEdit_NoiseA = QtWidgets.QLineEdit(self.groupBox_keysOption)
    self.lineEdit_NoiseA.setEnabled(False)
    self.lineEdit_NoiseA.setGeometry(QtCore.QRect(60, 35, 40, 16))
    self.lineEdit_NoiseA.setObjectName("lineEdit_NoiseA")     
    self.lineEdit_NoiseA.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
    self.lineEdit_NoiseA.setStyleSheet(optionLabelA)    
            
    

    self.label_dynCurvePow = QtWidgets.QLabel(self.groupBox_keysOption)
    self.label_dynCurvePow.setGeometry(QtCore.QRect(20, 60, 41, 16))
    self.label_dynCurvePow.setObjectName("label_ef_16")    
    self.label_dynCurvePow.setText(QtWidgets.QApplication.translate("MainWindow", "Pow:", None, -1))
    self.label_dynCurvePow.setStyleSheet(labelTextA)    

    
    self.lineEdit_pow = QtWidgets.QLineEdit(self.groupBox_keysOption)
    self.lineEdit_pow.setEnabled(False)
    self.lineEdit_pow.setGeometry(QtCore.QRect(60, 60, 40, 16))
    self.lineEdit_pow.setObjectName("lineEdit_pow")
    self.lineEdit_pow.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
    self.lineEdit_pow.setStyleSheet(optionLabelA)    
            



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
    self.startFrameLabel.setStyleSheet(labelTextA)  


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
    self.endFrameLabel.setStyleSheet(labelTextA)  


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
    self.fpsLabel.setStyleSheet(labelTextA)  
      
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
   # self.selectExportFileBTn.clicked.connect(self.defineExportFileName)
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
   # self.exportToSpineFileBtn.clicked.connect(self.exortTOSpineJson)              
    self.exportToSpineFileBtn.setStyleSheet(buttonStyleB)   
    

    self.slotColorGrp = QtWidgets.QGroupBox(self.dockImageButton)
    self.slotColorGrp.setGeometry(QtCore.QRect(10,20, 530, 150))
    self.slotColorGrp.setTitle("")
    self.slotColorGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "", None, -1))   

    self.slotColorGrp.setObjectName("slotColorGrp") 
    self.slotColorGrp.setStyleSheet(QGroupBoxA)     
    self.slotColorGrp.setVisible(True)

          
    self.setSlotColor = QtWidgets.QPushButton(self.slotColorGrp)
    self.setSlotColor.setGeometry(QtCore.QRect(10, 10, 100, 30))
    self.setSlotColor.setObjectName("setSlotColor")
    self.setSlotColor.setText(QtWidgets.QApplication.translate("MainWindow", "set color", None, -1))
    self.setSlotColor.setStyleSheet(buttonStyleB)     
    #self.setSlotColor.clicked.connect(self.setColorToSelectBone)

    self.setSlotColorKey = QtWidgets.QPushButton(self.slotColorGrp)
    self.setSlotColorKey.setGeometry(QtCore.QRect(120, 10, 100, 30))
    self.setSlotColorKey.setObjectName("setSlotColorKey")
    self.setSlotColorKey.setText(QtWidgets.QApplication.translate("MainWindow", "set key", None, -1))
    self.setSlotColorKey.setStyleSheet(buttonStyleB)     
    #self.setSlotColorKey.clicked.connect(self.setSlotColorKeyFrame)
    
    self.copyBoneKey = QtWidgets.QPushButton(self.slotColorGrp)
    self.copyBoneKey.setGeometry(QtCore.QRect(240, 10, 150, 30))
    self.copyBoneKey.setObjectName("copyBoneKey")
    self.copyBoneKey.setText(QtWidgets.QApplication.translate("MainWindow", "copy Bone Keys", None, -1))
    self.copyBoneKey.setStyleSheet(buttonStyleB)    
    
    self.pastedBoneKey = QtWidgets.QPushButton(self.slotColorGrp)
    self.pastedBoneKey.setGeometry(QtCore.QRect(400, 10, 100, 30))
    self.pastedBoneKey.setObjectName("pastedBoneKey")
    self.pastedBoneKey.setText(QtWidgets.QApplication.translate("MainWindow", "paste Bone Keys", None, -1))
    self.pastedBoneKey.setStyleSheet(buttonStyleB)       
    
    
    
    self.setNewSlot = QtWidgets.QPushButton(self.slotColorGrp)
    self.setNewSlot.setGeometry(QtCore.QRect(10, 50, 100, 30))
    self.setNewSlot.setObjectName("setNewSlot")
    self.setNewSlot.setText(QtWidgets.QApplication.translate("MainWindow", "set Slot", None, -1))
    self.setNewSlot.setStyleSheet(buttonStyleB)             
   # self.setNewSlot.clicked.connect(self.setSlotNewImage)
   
    
    #lay.addWidget(self.testBtn)
    #lay.addWidget(self.testLabel)    

