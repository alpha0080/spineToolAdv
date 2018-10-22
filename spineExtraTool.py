
import maya.cmds as cmds
import os,shutil,math

def loopKeyFrameB(obj,startFrame,endFrame,offsetFrame):
    print "loopKeyFrame22",obj,startFrame,endFrame,offsetFrame
    offsetSartFrame = float(startFrame +offsetFrame)   ##os
    #offsetNewStartFrame = float(startFrame +offsetFrame+0.000001)
    #dividOffsetFrame = dividFrame - 0.01
    #endOffsetFrame = endFrame -0.01
    offsetNewEndFrame =float (endFrame +offsetFrame)
   # dividFrame = float(offsetNewEndFrame -offsetFrame)
    SOframe = float(startFrame +offsetFrame)
    EOframe = float(endFrame + offsetFrame)
    DVframe = float(endFrame - offsetFrame)
    DVPframe = float(endFrame - offsetFrame + 0.01)
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
                   # print "aaaaaaaaaaaa",offsetNewStartFrame,startFrame,endFrame,dividFrame
                   # cmds.keyTangent(obj,itt ="linear", ott ="linear")
                   
                    startFrameValue = cmds.getAttr('%s.%s'%(obj,attr),t=startFrame)
                    endFrameValue  = cmds.getAttr('%s.%s'%(obj,attr),t=endFrame)

                    DVframeValue = cmds.getAttr('%s.%s'%(obj,attr),t=DVframe)
                    
                    cmds.setKeyframe(obj,at=attr,t=DVframe,v=DVframeValue)  #setKey to Divide Frame
                    cmds.setKeyframe(obj,at=attr,t=DVPframe,v=DVframeValue) #setKey to Divide Frame Offset 0.01
                    cmds.setKeyframe(obj,at=attr,t=startFrame,v=startFrameValue)  #setKey to Divide Frame
                    cmds.setKeyframe(obj,at=attr,t=endFrame,v=endFrameValue)  #setKey to Divide Frame
                  
                   # cmds.setKeyframe(obj,at=arrt,t=DVframe)
                   # cmds.setKeyframe('bone_candy01_10',at='translateX',t=10.0)
                    
                    cmds.cutKey(obj,at=attr,t= (startFrame,endFrame))
                    cmds.pasteKey(obj,at=attr, t= (SOframe,))
                   # cmds.keyTangent(obj,itt ="linear", ott ="linear")
                   # offsetNewStartFrameValue = cmds.getAttr('%s.%s'%(obj,attr),t=offsetNewStartFrame)
                   # offsetNewEndFrameValue  = cmds.getAttr('%s.%s'%(obj,attr),t=offsetNewEndFrame)
                    
                   # dividFrameValue = cmds.getAttr('%s.%s'%(obj,attr),t=endFrame)
                   # cmds.setKeyframe(obj,at=attr,t=endFrame,v=dividFrameValue)
                   # cmds.setKeyframe(obj,at=attr,t=offsetNewStartFrame,v=offsetNewStartFrameValue)
                   # cmds.setKeyframe(obj,at=attr,t=offsetNewEndFrame,v=offsetNewEndFrameValue)
                  #      
                    
                  #  cmds.keyTangent(obj,itt ="linear", ott ="linear")
                    
                    #
                    
                   # print attr,currentAttrValue
                    
            except:
                pass
                
                
                
    if offsetFrame == 0:
        pass
    else:
        cmds.cutKey(obj,t=((DVPframe+offsetFrame),offsetNewEndFrame) )
       # cmds.pasteKey('bone_candy01_28',t=(2,10),o="scaleReplace")
        cmds.pasteKey(obj,t=(startFrame,(offsetSartFrame-0.01)),o="scaleReplace")
        #cmds.cutKey(obj,t=((endFrame+1),))
       # cmds.keyTangent(obj,t=(offsetSartFrame,offsetSartFrame),ott ="stepnext",e=True) startFrame offsetSartFrame

        
#def drawCircle():    
        

def drawline(boneList,pointListString,lineWidth,startTime,endTime):
    print "drawline________1",boneList,pointListString
   # bone = boneList[0]
  #  pointLineList = pointListString.split('\n')
  #  for b in pointListString:
     #   print "bbbbbbbbbbbb",
    pointLineList = pointListString.split('\n')
    lineCount = len(pointLineList)
    pointCount = 0
   # print 'pointLineList pointLineList pointLineList',pointLineList
    boneForLine = []
    allDotPoint = []
    for j in range(0,lineCount):
        pointLine = pointLineList[j]
        tempPointList = pointLine.split(' ')
        tempPointList = filter(lambda x: len(x) > 0, tempPointList)
       # print 'tempPointList tempPointList tempPointList',tempPointList

        pointListPreLine = [] ## points pre line
        boneListPreLine = []
        for i in range(0,len(tempPointList)):
            pointPair = str(tempPointList[i])
        #    print 'pointPair',pointPair
            if len(pointPair.split(',')) == 2:
           # print 'iiiiiiiiiiii',i,len(i.split(','))
                pointListPreLine .append((int(pointPair.split(',')[0]),int(pointPair.split(',')[1])))
                if i < (len(tempPointList)-1):
                  #  print 'pointCountpointCountpointCountpointCount',pointCount
                    boneListPreLine.append(boneList[pointCount])
                    pointCount = pointCount + 1
        if len(pointListPreLine) >0:
            allDotPoint.append(pointListPreLine)
      #  print 'pointListPreLine pointListPreLine pointListPreLine',pointListPreLine,boneListPreLine
    #print 'pointList',pointList

       
        for i in range(0,len(boneListPreLine)):   
            bone = boneListPreLine[i]
            boneForLine.append(bone)
           # print 'bone bone bone bone bone bone',bone
            slotWidth = cmds.getAttr('%s.slot_width'%bone)
            slotName = cmds.getAttr('%s.bone_slot'%bone)
            cmds.setAttr('%s.translateX'%slotName,slotWidth/2) #move Slot plane
            
        
            x= pointListPreLine[i][0]
            y =pointListPreLine[i][1]
            print 'current',x,y
            xsec = pointListPreLine[i+1][0]
            ysec = pointListPreLine[i+1][1]
            print 'next',xsec,ysec
            
            deltaS = math.sqrt((x-xsec)*(x-xsec) + (y-ysec)*(y-ysec))
            if deltaS ==0:
                degree = 0
                sx = (x-xsec)/slotWidth
            else:
                cosAng = (abs(x-xsec))/deltaS
                degree = math.degrees(math.acos(cosAng))
                sx = (deltaS)/slotWidth
            
            deltaTime = float((endTime - startTime)/float(len(boneListPreLine)))
            
            cmds.setAttr('%s.translateX'%boneListPreLine[i],x)
            cmds.setAttr('%s.translateY'%boneListPreLine[i],y)
            cmds.setAttr('%s.scaleX'%boneListPreLine[i],sx)
            cmds.setAttr('%s.scaleY'%boneListPreLine[i],lineWidth)
            scaleStartFrame = startTime + i*deltaTime
            scaleEndFrame = scaleStartFrame + deltaTime
            cmds.setKeyframe(bone,at='scaleX',t=scaleStartFrame,v=0.01)
            cmds.setKeyframe(bone,at='slot_alpha',t=scaleStartFrame,v=0)
            cmds.setKeyframe(bone,at='slot_alpha',t=(scaleStartFrame+0.01),v=1)
            cmds.setKeyframe(bone,at='slot_alpha',t=scaleEndFrame,v=1)

            cmds.setKeyframe(bone,at='scaleX',t=scaleEndFrame,v=sx)
            print 'degree______________0',degree

            if (x-xsec) < 0 and (y-ysec) < 0:
              #  print '11111111111'
                degree = degree
            elif (x-xsec) > 0 and (y-ysec) < 0:
              #  print '222222'

                degree = 90 +(90-degree)
            elif (x-xsec) > 0 and (y-ysec) > 0:
              #  print '3333333'

                degree = 180 + degree
            elif (x-xsec) < 0 and (y-ysec) > 0:
            #    print '444444'

                degree =  -degree
            print 'degree',degree,bone

            cmds.setAttr('%s.rotateZ'%boneListPreLine[i],degree)
            
    for bone in boneForLine: #get bone for dot
        boneList.remove(bone)
        
   # print boneList,len(boneList)
    boneForDot = boneList 
    #for i in boneForDot:
    dotBoneIndeCount = 0
    for dotLine in allDotPoint:
        linePoints = []
        for i in range(0,len(dotLine)):
            dot = dotLine[i]
            bone = boneForDot[dotBoneIndeCount]
            x = dot[0]
            y=  dot[1]
            deltaTime = float((endTime - startTime)/float(len(dotLine)-1))
            linePoints.append((x,y,0))
            cmds.setAttr('%s.translateX'%bone,x)
            cmds.setAttr('%s.translateY'%bone,y)
            cmds.setAttr('%s.scaleX'%bone,lineWidth)
            cmds.setAttr('%s.scaleY'%bone,lineWidth)

            #cmds.setATtr('%s.slot_alpha'%bone,y)
            scaleStartFrame = startTime + i*deltaTime

            cmds.setKeyframe(bone,at='slot_alpha',t=scaleStartFrame,v=0)
            cmds.setKeyframe(bone,at='slot_alpha',t=(scaleStartFrame+0.01),v=1)
            
            dotBoneIndeCount = dotBoneIndeCount +1
            #print x,y,dotBoneIndeCount,bone,deltaTime
        print 'dotLine',dotLine
        curveName = "line_#"
        curve = cmds.curve(d=1,p=linePoints,n = curveName )     

                          
    #print boneForDot,allDotPoint   

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
   
   
