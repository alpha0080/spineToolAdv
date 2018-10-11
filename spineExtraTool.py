
import maya.cmds as cmds
import os,shutil


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
   
   
