
import maya.cmds as cmds
import os,shutil


def defineMask(maskObj):
    print "defineMask",maskObj
    vertexCount = cmds.polyEvaluate(maskObj,v=True)
    parentBone = cmds.listRelatives(p=True,type="transform")[0]
    print "parentBone",parentBone
    try:
        cmds.addAttr(maskObj, ln='spineClipping', numberOfChildren=8, attributeType='compound' )

        cmds.addAttr(maskObj, ln='spine_tag', sn='stag' , dt="string", parent='spineClipping'  ) #1
        cmds.addAttr(maskObj, ln='clipping_slot', sn='slot' , dt="string", parent='spineClipping'  )
        cmds.addAttr(maskObj, ln='clipping_vertexCount', parent='spineClipping'  )
        cmds.addAttr(maskObj, ln='clipping_vertexsData', sn='data' , dt="string", parent='spineClipping'  )
        cmds.addAttr(maskObj, ln='clipping_bone', sn='bone' , dt="string", parent='spineClipping'  )
        cmds.addAttr(maskObj, ln='clipping_attachment', sn='attachment' , dt="string", parent='spineClipping'  )
        cmds.addAttr(maskObj, ln='clipping_lastSlot', sn='slot' , dt="string", parent='spineClipping'  )
        cmds.addAttr(maskObj, ln='clipping_color', sn='color' , dt="string", parent='spineClipping'  )


    except:
        pass

    cmds.setAttr('%s.spine_tag'%maskObj,'spine_clipping',type='string')
    cmds.setAttr('%s.clipping_slot'%maskObj,maskObj,type='string')
    cmds.setAttr('%s.clipping_vertexCount'%maskObj,int(vertexCount))
    cmds.setAttr('%s.clipping_bone'%maskObj,parentBone,type='string')
    cmds.setAttr('%s.clipping_attachment'%maskObj,maskObj,type='string')
    cmds.setAttr('%s.clipping_color'%maskObj,"ce3a3aff",type='string')
    vertexList = ""
    for i in range(0,vertexCount):
        vertexP = "%s.vtx[%s]"%(maskObj,str(i))
        x = float('{:.2f}'.format(cmds.pointPosition(vertexP)[0]))
        y = float('{:.2f}'.format(cmds.pointPosition(vertexP)[1]))
        vertexList += (str(x) +","+str(y)+",") 
       # vertexList.append(x)
       # vertexList.append(y)
        
    cmds.setAttr('%s.clipping_vertexsData'%maskObj,str(vertexList),type='string')
    shader = cmds.shadingNode("blinn",asShader=True,n="clipping_shader_#")   
    shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n="clipping_SG_#")
    cmds.connectAttr('%s.color' %shader ,'%s.surfaceShader' %shading_group)

    cmds.select(cl=True) 
    cmds.select(maskObj)
    cmds.hyperShade( assign=shader )
    
    cmds.setAttr('%s.transparency'%shader,0,1,0.9,type='double3')  ### set to normal blend mode
    cmds.setAttr('%s.ambientColor'%shader,1,1,1,type='double3')  ### set to normal blend mode
    cmds.setAttr('%s.diffuse'%shader,0)  ### set to normal blend mode

    #print vertexList
 #  (cmds.pointPosition(i)[0


def createBone(boneName):
    print "createBone"
    

    cmds.select(cl=True)
      
    bone = cmds.joint(p=(0,0,0),n=boneName)

    cmds.addAttr(bone, ln='spineBone', numberOfChildren=25, attributeType='compound' )
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
    cmds.addAttr(bone, ln='curvature', sn='s_curve' , at="enum",en="Linear:Stepped:Cycle:------:BC(0.25,0,0.75,0):BC(0.5,0.5,0.5,0.5)", parent='spineBone' ,k=True )
    

    cmds.setAttr('%s.spine_tag'%bone,'spine_bone',type='string')
    cmds.setAttr('%s.bone_name'%bone,bone,type='string')
    return bone

   
def getDrawOrder(objList,fps):  
    #objList = cmds.ls(sl=True,type='joint')

    allZKeyFrameList = []
    try:
        for obj in objList:
            
            for f in cmds.keyframe(obj,at='translateZ',q=True):
                if f in allZKeyFrameList:
                    pass
                else:
                    allZKeyFrameList.append(f)

    
        zListDict = {}                    
        for f in allZKeyFrameList:
            tempZListPreKey = {}
            for obj in objList:
                z = cmds.getAttr('%s.translateZ'%obj,t=f)
                tempZListPreKey.update({obj:z})

            zListPreKey =  sorted(tempZListPreKey.items(), key=lambda kv: kv[1])

            zListDict.update({f:zListPreKey})
            

        zKeyFrameList =  sorted(zListDict.keys())
        setupDrawOrder = []
        animationDrawOrder = []
        
        for obj in objList:
            setupDrawOrder.append(obj)
        setupDrawOrder = list(reversed(setupDrawOrder))
        #print 'setupDrawOrder',setupDrawOrder
        for i in range(0,len(zKeyFrameList)):
            f = zKeyFrameList[i]
            pf = zKeyFrameList[0]
            cL =  zListDict[f]
            cL = list(reversed(zListDict[f]))
            pL = zListDict[pf]
          #  pL = list(reversed(zListDict[pf]))
            tempObjDrawOrderList = []
           # print 'cl',cL
          #  print 'pl',setupDrawOrder
            for obj in objList:
                
                f_el = filter(lambda x:x[0] == obj ,cL)[0]
                obj_f_index = cL.index(f_el)
                pr_el =  filter(lambda x:x[0] == obj ,pL)[0]   
                obj_pf_index = pL.index(pr_el)   
                obj_setupIndex = setupDrawOrder.index(obj) 
              #  print obj,obj_f_index,obj_setupIndex
                modulNum = len(objList)-obj_f_index
                slotName = cmds.getAttr('%s.bone_slot'%obj)
                tempObjDrawOrderList.append({"slot":slotName,"offset": (-1*((obj_f_index-obj_setupIndex)))})
              #  if i == 0:
                   # setupDrawOrder.append({obj:obj_f_index})
            animationDrawOrder.append({"time":f/fps, "offsets":tempObjDrawOrderList})   
        return [setupDrawOrder,animationDrawOrder]
    except:
        return [[],[]]
    
      
def createShader(sourceImage,targetDir):    #slotName, imageSort name, image full name
   # print "createShader",imageName, currentImage 
    
   # imageName = currentImage.split('.')[0]
    imageName = sourceImage.split('/')[-1].split('.')[0]
    targetFileName =targetDir +'/' + sourceImage.split('/')[-1]
  
    slotShaderName =  imageName + '_shader'
    slotFileName = imageName + '_imageFile'
    slotSG = imageName + '_SG'   
 
    
    shader = cmds.shadingNode("blinn",asShader=True,n=slotShaderName)   
     
    file_node=cmds.shadingNode("file",asTexture=True,n=slotFileName)
    
    try:
        if os.path.isfile(targetFileName) == True:
            print "file exist"
            
        else:
            #os.remove(targetFile)
            shutil.copyfile(sourceImage,targetFileName)        
    
    except:
                   
        pass    
        
        
    
   # print "targetFileName_________1",targetFileName,os.path.isfile(targetFileName)
    cmds.addAttr(shader, ln='spineShaderSet', numberOfChildren=2, attributeType='compound' )
    cmds.addAttr(shader, ln='spine_tag', sn='stag' , dt="string", parent='spineShaderSet' ,k=False )
    cmds.addAttr(shader, ln='slot_blend', sn='s_blend' , at="enum",en="normal:additive:multiply:screen", parent='spineShaderSet' ,k=True )
            
    cmds.setAttr('%s.spine_tag'%shader,'spine_shader',type='string')
           
            
    
    
    print 'file_node____1',file_node
    shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n=slotSG)
    cmds.connectAttr('%s.color' %shader ,'%s.surfaceShader' %shading_group)
    cmds.connectAttr('%s.outColor' %file_node, '%s.color' %shader)
    cmds.connectAttr('%s.outTransparency' %file_node, '%s.transparency' %shader)
    cmds.connectAttr('%s.outAlpha' %file_node, '%s.reflectivity' %shader)
    cmds.setAttr('%s.specularColor'%shader,0,0,0,type='double3')
    cmds.setAttr('%s.reflectedColor'%shader,0,0,0,type='double3')  ### set to normal blend mode

    cmds.setAttr('%s.fileTextureName'%file_node,targetFileName,type='string')
   
    return shader
    
    
    
def defineSlot(slotName,boneName,sourceDir,targetDir):
      
        print "defineSlot",slotName,boneName,sourceDir,targetDir

        try:
            cmds.addAttr(slotName, ln='spineSlot', numberOfChildren=14, attributeType='compound' )
            cmds.addAttr(slotName, ln='spine_tag', sn='stag' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slotName, ln='slot_name', sn='s_name' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slotName, ln='slot_bone', sn='s_bone' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slotName, ln='slot_width', sn='s_w', parent='spineSlot'  )
            cmds.addAttr(slotName, ln='slot_height', sn='s_h', parent='spineSlot'  )
            
            cmds.addAttr(slotName, ln='slot_color', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
            cmds.addAttr(slotName, ln='slot_red', attributeType='float',dv=1.0, parent='slot_color',k=True )
            cmds.addAttr(slotName, ln='slot_green', attributeType='float',dv=1.0, parent='slot_color',k=True )
            cmds.addAttr(slotName, ln='slot_blue', attributeType='float',dv=1.0, parent='slot_color',k=True )
            cmds.addAttr(slotName, ln='slot_alpha', attributeType='float',dv=1.0, parent='spineSlot',k=True )

            cmds.addAttr(slotName, ln='slot_dark', usedAsColor=True, attributeType='float3',parent='spineSlot' ,k=True )
            cmds.addAttr(slotName, ln='slot_darkRed', attributeType='float', parent='slot_dark',k=True )
            cmds.addAttr(slotName, ln='slot_darkGreen', attributeType='float', parent='slot_dark',k=True )
            cmds.addAttr(slotName, ln='slot_darkBlue', attributeType='float', parent='slot_dark',k=True )                
            cmds.addAttr(slotName, ln='slot_attachment', sn='s_att' , dt="string", parent='spineSlot'  )
            cmds.addAttr(slotName, ln='slot_sequence', sn='s_seq' , at="bool", dv=0,parent='spineSlot' )
            cmds.addAttr(slotName, ln='slot_sequenceAmount', attributeType='float',dv=1.0, parent='spineSlot')
            cmds.addAttr(slotName, ln='slot_sequenceSpeed', attributeType='float',dv=1.0, parent='spineSlot')
            cmds.addAttr(slotName, ln='slot_sequence_random', sn='s_seqRand' , at="bool", dv=0,parent='spineSlot' )


            cmds.addAttr(slotName, ln='slot_blend', sn='s_blend' , at="enum",en="normal:additive:multiply:screen", parent='spineSlot' ,k=True )

           # cmds.setAttr ('%s.translateZ'%slotName,keyable = False, cb = False, lock = True)  
           # cmds.setAttr ('%s.rotateX'%slotName, lock = True)  
           # cmds.setAttr ('%s.rotateY'%slotName,keyable = False, cb = False, lock = True)  

           # cmds.setAttr ('%s.scaleX'%slotName, lock = True)  
           # cmds.setAttr ('%s.scaleZ'%slotName, lock = True)  
           # cmds.setAttr ('%s.scaleY'%slotName,keyable = False, cb = False, lock = True)  
           # cmds.setAttr ('%s.visibility'%slotName,keyable = False, cb = False, lock = True)  
               
               
        except:
            pass
        slotList = cmds.listRelatives( slotName, c=True,ad=True,s=True)
        if len(slotList) > 1:
            errMsg = 'more than one shape in slot transform'
            #self.errMsgLabel.setText('more than one shape in slot transform')
        else:
            pass
           # slotName =  slot#cmds.listRelatives(slotList[0],p=True)[0]
        cmds.setAttr('%s.spine_tag'%slotName,'spine_slot',type='string')
        cmds.setAttr('%s.slot_name'%slotName,slotName,type='string')
        cmds.setAttr('%s.slot_bone'%slotName,boneName,type='string')
        getObj =  cmds.ls(slotName,dag=1)[1]
          #print 'getObj',getObj
        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
       # if cmds.nodeType(shaders) == 'lambert':
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
      #  elif cmds.nodeType(shaders) == 'surfaceShader':

          #  fileNode = cmds.listConnections('%s.outColor' % (shaders[0]), type='file')
        currentFile = cmds.getAttr("%s.fileTextureName" %fileNode[0])
        fileName = currentFile.split("/")[-1]
        fileInSlot = currentFile.split("/")[-1][0:-4]
        searchPath = sourceDir#currentFile.split(fileName)[0]
        allFilesInDir = os.listdir(searchPath)
        print 'currentFile',currentFile,fileInSlot,searchPath,allFilesInDir

        allSequenceFilesList = []
        imagesFilter = ['jpg','JPG','png','PNG']
        for i in allFilesInDir:
            if i.split('.')[-1] in imagesFilter:
               # print len(i.split('.'))
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
            cmds.setAttr('%s.slot_sequenceAmount'%slotName,sequenceAmount)   
        else:
            cmds.setAttr('%s.slot_sequenceAmount'%slotName,1)   
                    
       # print 'allFilesInDir',allFilesInDir
          #print 'fileInSlot',fileInSlot
        cmds.setAttr('%s.slot_attachment'%slotName,fileInSlot,type='string')
        targetFile = targetDir + '/' +fileName
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
                            sourceSeqFile = searchPath +file
                            print 'sourceSeqFile',sourceSeqFile
                            targetSeqFile = targetDir + '/'+file
                            print 'targetSeqFile',targetSeqFile
                            try:
                                shutil.copyfile(sourceSeqFile,targetSeqFile)
                            except:
                                pass
        else:
            pass
        
        #return errMsg
        #print 'currentFilefffffff',currentFile
                                              
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    