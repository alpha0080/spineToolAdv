
import maya.cmds as cmds
import os,shutil


def loopKeyFrame(obj,startFrame,endFrame,offsetFrame):
    print "loopKeyFrame"#,obj,startFrame,endFrame,offsetFrame
    offsetNewStartFrame = startFrame +offsetFrame
    dividFrame = float(endFrame -offsetFrame)
    dividOffsetFrame = dividFrame - 0.01
    endOffsetFrame = endFrame -0.01
    offsetNewEndFrame = endFrame +offsetFrame
    cmds.getAttr('%s.translateX'%obj,t=15.0)
    keyAbleAttList=["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ","slot_alpha","slot_red","slot_green","slot_blue"] #["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]

    #cmds.keyframe(obj,at="translateX",q=True)
    for attr in keyAbleAttList:
        cmds.keyTangent(obj,itt ="linear", ott ="linear")
        keyFramesList = cmds.keyframe(obj,at=attr,q=True)
        #print attr,keyFramesList
        if offsetFrame == 0:
            try:
                endFrameAttrValue = cmds.getAttr('%s.%s'%(obj,attr),t=endFrame)
                startFrameAttrValue = cmds.getAttr('%s.%s'%(obj,attr),t=startFrame)
                cmds.setKeyframe(obj,at=attr,t=startFrame,v=startFrameAttrValue) 
                cmds.setKeyframe(obj,at=attr,t=endFrame,v=endFrameAttrValue)
            except:
                pass
            
        else:
            try:
                if len(keyFramesList) >0 :
                   # keyframeListAttr = cmds.keyframe(obj,at=attr)
                    divideFrameAttrValue = cmds.getAttr('%s.%s'%(obj,attr),t=dividFrame)
                    endFrameAttrValue = cmds.getAttr('%s.%s'%(obj,attr),t=endFrame)
                    startFrameAttrValue = cmds.getAttr('%s.%s'%(obj,attr),t=startFrame)
                    offsetFrameValue = cmds.getAttr('%s.%s'%(obj,attr),t=offsetFrame)
                    cmds.setKeyframe(obj,at=attr,t=startFrame,v=startFrameAttrValue) 
                    cmds.setKeyframe(obj,at=attr,t=endFrame,v=endFrameAttrValue) 
                    cmds.keyTangent(obj,itt ="linear", ott ="linear")
         
                    cmds.setKeyframe(obj,at=attr,t=dividFrame,v=divideFrameAttrValue)
                    cmds.setKeyframe(obj,at=attr,t=dividOffsetFrame,v=divideFrameAttrValue)
                    cmds.setKeyframe(obj,at=attr,t=endOffsetFrame,v=endFrameAttrValue)
                    cmds.setKeyframe(obj,at=attr,t=endFrame,v=startFrameAttrValue)

                    cmds.keyTangent(obj,itt ="linear", ott ="linear")
                    
                    #
                    
                   # print attr,currentAttrValue
                    
            except:
                pass
    if offsetFrame == 0:
        pass
    else:
        cmds.cutKey(obj,t=(startFrame,endFrame))
        cmds.pasteKey(obj,t=(offsetNewStartFrame,))
        cmds.keyTangent(obj,itt ="linear", ott ="linear")
        cmds.cutKey(obj,t=(endFrame,offsetNewEndFrame))
        cmds.pasteKey(obj,t=(startFrame,offsetNewStartFrame),o="replace")



def getNextSaveFileName(currentFileName,fileDir,login):
    print "getNextSaveFileName",currentFileName,login

    digitalNum= ["0","1","2","3","4","5","6","7","8","9"]
    
    tempAllFilesInSearchDir = os.listdir(fileDir)
    allFilesInSearchDir = filter(lambda x: x.split('.')[-1] =='mb' ,tempAllFilesInSearchDir)
    allVerList = []
    for i in allFilesInSearchDir:

        fileSpiltList = i.split('.mb')[0].split('_')

        for j in fileSpiltList:
            if len(j) ==4:
                if j[0] =='v':
                    if j[1] in digitalNum:
                        if j[2] in digitalNum:
                            if j[3] in digitalNum:
                                if j in allVerList:
                                    pass
                                else:
                                    allVerList.append(int(j.split('v')[-1]))
                                    
    nextFileVerStr = "v"+str('{0:03d}'.format(allVerList[-1]+1))
                                    

        
    nameSpList = currentFileName.split('_')
    

    for i in range(0,len(nameSpList)):
        if len(nameSpList[i]) == 4:
            
            if nameSpList[i][0] == "v":
                
                if nameSpList[i][1] in digitalNum:
                    
                    if nameSpList[i][2] in digitalNum:
                        if nameSpList[i][3] in digitalNum:
                            verNumIndex = i
                            currentVerStr = nameSpList[i]
                            currentVerNum = int(nameSpList[i].split('v')[-1])
                            nextFileVerNum = currentVerNum + 1
                            nextFileVerStr = "v"+str('{0:03d}'.format(nextFileVerNum))

    nextSaveFileName = ""
    for i in range(0,verNumIndex):

        nextSaveFileName += nameSpList[i] +'_'
        

    nextSaveFileName =  nextSaveFileName + nextFileVerStr +'_' + login +'.mb'

    return nextSaveFileName
         


def delUnusedShaderNode():
    print 'delUnusedShaderNode'
    allTransform = cmds.ls(type='transform')
    allSlotShapeList = []
    usedSGList = []
    usedShaderList = []
    usedFileList = []

    for i in allTransform:
        try:
            if cmds.getAttr('%s.spine_tag'%i) == 'spine_slot':
                shapeName = cmds.listRelatives (i,c=True,type='mesh')[0]
                if shapeName in allSlotShapeList:
                    pass
             
                else:
                    allSlotShapeList.append(shapeName)
        except:
            pass

    for i in allSlotShapeList:
        sg = cmds.listConnections (i,type='shadingEngine')[0]
        try:
            if sg in usedSGList:
                pass
   
            else:
                usedSGList.append(sg)
        except:
            pass
            
    for i in usedSGList:
       # print cmds.listConnections (i,type='lambert')
        try:
            shader = cmds.listConnections (i,type='lambert')[0]
        except:
            shader = cmds.listConnections (i,type='blinn')[0]
        if shader == 0:
            pass
        else:
            if shader in usedShaderList:
                pass
            else:
                usedShaderList.append(shader)
                
    for i in usedShaderList:
        try:
            fileList =  cmds.listConnections (i,type='file')
            for f in fileList:
                if f in usedFileList:
                    pass
                else:
                    usedFileList.append(f)
        except:
            pass
            
    allSGlist = cmds.ls(type='shadingEngine')
    allLSlist = cmds.ls(type='lambert')
    allBSlist = cmds.ls(type='blinn')

    allSGlist.remove('initialParticleSE')
    allSGlist.remove('initialShadingGroup')
    allLSlist.remove('lambert1')
    allFilelist = cmds.ls(type='file')
    print usedSGList
    print usedShaderList
    print usedFileList
    
    for i in allSGlist:
        if i not in usedSGList:
            try:
                cmds.delete(i)
            except:
                pass
                
    for i in allLSlist:
        if i not in usedShaderList:
            try:
                cmds.delete(i)
            except:
                pass
                
    for i in allBSlist:
        if i not in usedShaderList:
            try:
                cmds.delete(i)
            except:
                pass
                
    for i in allFilelist:
        if i not in usedFileList:
            try:
                cmds.delete(i)
            except:
                pass  
   
   
