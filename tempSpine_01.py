import ice,os,math

def createAtlasImage(maxImageW,maxImagwH):

    points =  [(0,0,0),(0,maxImagwH,0),(maxImageW,maxImagwH,0),(maxImageW,0,0),(0,0,0)]
    
    atlasImageEditAreaCurve = cmds.ls("atlasImageEditArea")
    if len(atlasImageEditAreaCurve) == 0:
        curve = cmds.curve(d=1,p=points,n = "atlasImageEditArea" )   
        textImage01 = cmds.textCurves(t="image_01",f='Arial',n="imageArea_01")  


        print "textImage01",textImage01
        cmds.setAttr('%s.scaleX'%textImage01[0],100)
        cmds.setAttr('%s.scaleY'%textImage01[0],100)
        cmds.setAttr('%s.translateY'%textImage01[0],-100)


    else:
        pass

    
    
    tempTransformObj = cmds.ls(type="transform")
    spineRootObj = []

    for i in tempTransformObj:
        try:
            if cmds.getAttr('%s.spine_tag'%i) == "spine_RootSkeleton":
                if i in spineRootObj:
                    pass
                else:
                    spineRootObj.append(i)
        except:
            pass
            
            
    spineSlotNMeshInRoot = []    
    for i in spineRootObj:
        for j in cmds.listRelatives(i,c=True,ad=True):
            spineSlotNMeshInRoot.append(j)
            
    tempMeshList = filter(lambda x:cmds.nodeType(x) == "mesh" ,spineSlotNMeshInRoot)
     
    spineImageMeshList = []               
    for i in tempMeshList :      
       
        try:
            currentParent = cmds.listRelatives(i,p=True)[0]
          #  print cmds.listRelatives(i,p=True)[0],cmds.getAttr('%s.spine_tag'%currentParent)
            if cmds.getAttr('%s.spine_tag'%currentParent) == "spine_slot" or cmds.getAttr('%s.spine_tag'%currentParent) == "spine_skin":
                if currentParent in spineImageMeshList:
                    pass
                else:
                    spineImageMeshList.append(i)
        except:
            pass

    spineImageList = []
    for i in spineImageMeshList:
        
        shadingGrps = cmds.listConnections(i,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)

        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')

        currentFile = cmds.getAttr("%s.fileTextureName" %fileNode[0])
        if currentFile in spineImageList:
            pass
        else:
            spineImageList.append(currentFile)
        
     
    imageInfoDictList = []
    atlasImageList = []
    for i in spineImageList: 
        image = ice.Load(i)
        imageMetaData = image.GetMetaData()
        currentImage = i.split('/')[-1]
        #imageSize = imageMetaData['Original Size']
        w = int(imageMetaData['Original Size'].split(" ")[0].split("(")[1])
        h = int(imageMetaData['Original Size'].split(" ")[1].split(")")[0])
        area = w*h 
        pName = "imageAtlasPlane_"+ currentImage.split('.')[0]
        #print pName
        imageInfoDictList.append({"image":currentImage,"w":w,"h":h,"area":area,"url":i,"pName":pName})    
        if pName in atlasImageList:
            pass
        else:
            atlasImageList.append(pName)
       # print i,w,h
        
        
    widthFirstImageInfoList =  list((sorted(imageInfoDictList, key = lambda x: x["w"],reverse=True))) #reversed




    getImageAtlasGrp = cmds.ls("imageAtlas")

    if len(getImageAtlasGrp) == 0:
        cmds.createNode('transform',ss=True,n= "imageAtlas")
        
    else:
        

        pass
        



    planeInImageAtlas = cmds.listRelatives("imageAtlas",c=True,typ="transform")
    existAtlasImage = []
    try:
        for i in planeInImageAtlas:

            shape = cmds.listRelatives(i,c=True,type="mesh")
            shadingGrps = cmds.listConnections(shape,type='shadingEngine')
 
            shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)

            fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')

            currentFile = cmds.getAttr("%s.fileTextureName" %fileNode[0])  
            if currentFile in existAtlasImage:
                pass
            else:
                existAtlasImage.append(currentFile)

    except:
        pass

    for i in widthFirstImageInfoList:
      #  print i
        pw= i['w']
        ph= i['h']
        pName = i['pName']#"imageAtlasPlane_"+i['image'].split('.')[0]

        targetFileName = i['url']
        if targetFileName in existAtlasImage:
            pass
        else:
        
        
            plane = cmds.polyPlane(sx=1,sy=1,w=pw,h=ph,name =pName )
            cmds.setAttr('%s.rotateX'%pName,90)
            cmds.setAttr('%s.translateX'%pName,-2500)


            cmds.parent(plane,"imageAtlas")
            slotShaderName =  pName + '_ia_shader'
            slotFileName = pName + '_ia_imageFile'
            slotSG = pName + '_ia_SG'   
            shader = cmds.shadingNode("blinn",asShader=True,n=slotShaderName)       
            file_node=cmds.shadingNode("file",asTexture=True,n=slotFileName)   
            shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True,n=slotSG)
            cmds.connectAttr('%s.color' %shader ,'%s.surfaceShader' %shading_group)
            cmds.connectAttr('%s.outColor' %file_node, '%s.color' %shader)
            cmds.connectAttr('%s.outTransparency' %file_node, '%s.transparency' %shader)
            cmds.connectAttr('%s.outAlpha' %file_node, '%s.reflectivity' %shader)
            cmds.setAttr('%s.specularColor'%shader,0,0,0,type='double3')
            cmds.setAttr('%s.ambientColor'%shader,1,1,1,type='double3')
            cmds.setAttr('%s.diffuse'%shader,0)

            cmds.setAttr('%s.reflectedColor'%shader,0,0,0,type='double3')  ### set to normal blend mode
            cmds.setAttr('%s.fileTextureName'%file_node,targetFileName,type='string')       
            cmds.select(cl=True) 

            cmds.select(plane)
            cmds.hyperShade( assign=shader )
            cmds.select(cl=True) 
            
    try:
        cmds.parent("atlasImageEditArea","imageAtlas")
        cmds.parent(textImage01[0],"imageAtlas")
    except:
        pass
    
    
    
    return widthFirstImageInfoList,atlasImageList
    
    
def alignSignalImage(imagePlane,bb):
    imagePlaneW = imagePlane["w"]
    imagePlaneH = imagePlane["h"]
    if imagePlaneW < (bb[2]-bb[0]) and imagePlaneH < (bb[3]-bb[1]):
        
        areaA = [bb[0],bb[1],imagePlane["w"],imagePlane["h"]]
        areaB = [(bb[0]+imagePlane["w"]),bb[1],bb[2],(bb[1]+imagePlane["h"])]
        areaC = [bb[0],(bb[1]+imagePlane["h"]),bb[2],bb[3]]

    else:
        pass
    
def alignAtlasImage(maxImageW,maxImageH):
    
    #maxImageW = 2048
    #maxImageH = 2048
    atlasImageData  = createAtlasImage(maxImageW,maxImageH)    
    widthFirstImageInfoList = atlasImageData[0]
    atlasImageList = atlasImageData[1]
    
    dividAreaData = []
    usedDividAreaList = []
    notUsedDividAreaList = []
    firstPlane = widthFirstImageInfoList[0]
    firstPlaneW = firstPlane["w"]
    firstPlaneH = firstPlane["h"]
    firstPlaneName = firstPlane["pName"]
    bCount = 0
    cCount = 0
    if firstPlaneW < maxImageW and firstPlaneH < maxImageH:

        areaA = [(0+1),(0+1),(firstPlaneW+1),(firstPlaneH+1)]
        areaB = [(firstPlaneW+1+1),(0+1),maxImageW,firstPlaneH]
        areaC = [(0+1),(firstPlaneH+1+1),maxImageW,maxImageH]

        notUsedDividAreaList.append(areaB)
        notUsedDividAreaList.append(areaC)
        usedDividAreaList.append({firstPlaneName:areaA})
        

    else:
        pass
    

   # bb=[0,0,2048,2048]
    allImagePlane = []
    for i in widthFirstImageInfoList[1:]:
        plane = i["pName"]
        if plane in allImagePlane:
            pass
        else:
            allImagePlane.append(plane)
    
    for i in widthFirstImageInfoList[1:]:
        dividData = alignToDividArea(i,notUsedDividAreaList,usedDividAreaList,allImagePlane)
        notUsedDividAreaList = dividData[0]
        usedDividAreaList = dividData[1]
        allImagePlane = dividData[2]

    print "usedDividAreaList________________111",usedDividAreaList
    for i in usedDividAreaList:
        plane = i.keys()[0]
        area = i[plane]
        cmds.setAttr("%s.translateX"%plane,(area[0]+math.ceil((area[2]-area[0])/2)))
        cmds.setAttr("%s.translateY"%plane,(area[1]+math.ceil((area[3]-area[1])/2)))
    pageCount = 1
    while len(allImagePlane) > 0:
        pageCount = pageCount +1
        allImagePlane = defineImagePlaneAtlas(pageCount,maxImageW,maxImageH,allImagePlane,widthFirstImageInfoList)
   # print "allImagePlane______________last",allImagePlane
 
 #   defineImagePlaneAtlas(2,maxImageW,maxImageH,allImagePlane,widthFirstImageInfoList)   ### call define imagePlaneAtlas function
    
def defineImagePlaneAtlas(pageCount,maxImageW,maxImageH,allImagePlane,widthFirstImageInfoList):
    print "widthFirstImageInfoList___________00000",widthFirstImageInfoList

    points =  [((maxImageW*(pageCount-1)),0,0),(maxImageW*(pageCount-1),maxImageH,0),(pageCount*maxImageW,maxImageH,0),(pageCount*maxImageW,0,0),(maxImageW*(pageCount-1),0,0)]
    curveName = "atlasImageEditArea_" + str(pageCount)
    #atlasImageEditAreaCurve = cmds.ls("atlasImageEditAreaB")
    curve = cmds.curve(d=1,p=points,n =curveName)   
    text = "image_"+ str(pageCount)
    textName = "imageArea_"+str(pageCount)
    textImage = cmds.textCurves(t=text,f='Arial',n=textName)  
    cmds.setAttr('%s.scaleX'%textImage[0],100)
    cmds.setAttr('%s.scaleY'%textImage[0],100)
    cmds.setAttr('%s.translateX'%textImage[0],maxImageW*(pageCount-1))

    cmds.setAttr('%s.translateY'%textImage[0],-100)
    
    firstPlane = filter(lambda x:x["pName"] == allImagePlane[0] ,widthFirstImageInfoList)[0]
    firstPlaneW = firstPlane["w"]
    firstPlaneH = firstPlane["h"]
    firstPlaneName = firstPlane["pName"]
    
    areaA = [((maxImageW*(pageCount-1))+1),(0+1),((maxImageW*(pageCount-1)+1)+firstPlaneW),(firstPlaneH+1)]
    areaB = [((maxImageW*(pageCount-1)+1)+firstPlaneW+1),(0+1),(maxImageW*pageCount),firstPlaneH]

    areaC = [((maxImageW*(pageCount-1)+1)),(firstPlaneH+1+1),(maxImageW*pageCount),firstPlaneH]    
    notUsedDividAreaList = []
    usedDividAreaList = []
    notUsedDividAreaList.append(areaB)
    notUsedDividAreaList.append(areaC)
    usedDividAreaList.append({firstPlaneName:areaA})

    allImagePlane.remove(firstPlaneName)
    for i in allImagePlane:
        planeData  = filter(lambda x:x["pName"] == i ,widthFirstImageInfoList)[0]
        #print "iiiii",i,planeData

        dividData = alignToDividArea(planeData,notUsedDividAreaList,usedDividAreaList,allImagePlane)
        notUsedDividAreaList = dividData[0]
        usedDividAreaList = dividData[1]
        allImagePlane = dividData[2]

    print "usedDividAreaListB",usedDividAreaList    
    
    for i in usedDividAreaList:
        plane = i.keys()[0]
        area = i[plane]
        cmds.setAttr("%s.translateX"%plane,(area[0]+math.ceil((area[2]-area[0])/2)))
        cmds.setAttr("%s.translateY"%plane,(area[1]+math.ceil((area[3]-area[1])/2))) 
    
    try:
        cmds.parent(curveName,"imageAtlas")
        cmds.parent(textImage[0],"imageAtlas")
    except:
        pass
    
    return allImagePlane
    
def alignToDividArea(i,notUsedDividAreaList,usedDividAreaList,allImagePlane):
    imageW = i["w"]
    imageH = i["h"]
    imageName = i["pName"]

    areaIn = 0
    for area in notUsedDividAreaList:
        if areaIn == 0:
            areaW = area[2]-area[0]
            areaH = area[3]-area[1]
            if imageW < (areaW-2) and imageH < (areaH-2):

                notUsedDividAreaList.remove(area)
                allImagePlane.remove(imageName)
                
                areaA = [area[0],area[1],(area[0]+imageW),(area[1]+imageH)]
                areaB = [(area[0]+1+imageW),area[1],area[2],(area[1]+imageH)]
                areaC = [area[0],(area[1]+imageH+1),area[2],area[3]]
                notUsedDividAreaList.append(areaB)
                notUsedDividAreaList.append(areaC)

                usedDividAreaList.append({imageName:areaA})
                 
                areaIn =1
           # else:
                # notUsedPlane.append(imageName)
        else:
           
            pass
    return notUsedDividAreaList,usedDividAreaList,allImagePlane
      #  print area,areaW,areaH
   # print i
 
    
    
def checkAlignImageMode(maxImageW,maxImageH,imageName,exportDir):
    imageAtlasCheck = len(cmds.ls("imageAtlas"))
   # print imageAtlasCheck
    if imageAtlasCheck > 0:
        allPageImagesAtlasData = defineImageAtlasData(maxImageW,maxImageH,imageName)
        allPageImagesAtlas = allPageImagesAtlasData[0]
        allPages = allPageImagesAtlasData[1]
               # print "xy",x,y,w,h
    else:
        alignAtlasImage(maxImageW,maxImageH)
        allPageImagesAtlasData = defineImageAtlasData(maxImageW,maxImageH,imageName)
        allPageImagesAtlas = allPageImagesAtlasData[0]
        allPages = allPageImagesAtlasData[1]
    print "allPageImagesAtlas",allPageImagesAtlas,allPages
    

    for i in allPages:
        if i < 0:
            pass
        else:
            currentImageAtlasData = filter(lambda x:x['page'] == i ,allPageImagesAtlas)
            print "currentImageAtlasData",currentImageAtlasData
            writeAtlasFile(imageName,i,exportDir,maxImageW,maxImageH,currentImageAtlasData)
            writeImage(imageName,i,exportDir,maxImageW,maxImageH,currentImageAtlasData)
    #fileName = imageName

def writeImage(imageName,pageCount,exportDir,maxImageW,maxImageH,currentImageAtlasData):
    
    if pageCount == 0:
        imageAtlasFileName = exportDir+'/'+imageName + '.png'
    else:
        imageAtlasFileName = exportDir+'/'+imageName + str(pageCount+1)+'.png'
    print "currentImageAtlasData_____________2",currentImageAtlasData
    #fileName = exportDir +'/' +imageName
    
    box = [0, maxImageW, 0, maxImageH]
    color = [0.0, 0.0, 0.0, 0.0]
    
    bg = ice.FilledImage(ice.constants.FLOAT, box, color)
    format = ice.constants.FMT_PNG
   # print "currentImageAtlasData_______1",currentImageAtlasData
    for i in currentImageAtlasData:
        fileName = i["url"]
        x = i["x"]
        y = i["y"]
        w = i["w"]
        h = i["h"]
        print "pageCount,file",pageCount,fileName,x,y,w,h
        print "image is existed ",os.path.isfile(fileName)
        fg= ice.Load(fileName)
        fgbox = [0,0,w,h]
        fgCard = ice.FilledImage(ice.constants.FLOAT, fgbox, color)
        fgResult = fgCard.Cover(fg)
        #cropBox = [x,(x+w),y,(y+h)]
        #fgCorp = fg.SubImageWorld(cropBox)
        translateAmount = (x,y)
        translateFilter = ice.constants.FILTER_CATROM
        fgResult = fgResult.Translate(translateAmount, translateFilter) 
        #fgResult = fgResult.SubImageWorld(cropBox)
        bg = bg.Cover(fgResult) 
           
      #  fgResult = fg.Scale(scaleAmoiunt, scaleFilter)
        
      #  bg = bg.Over(fgResult)  
    bg.Save(imageAtlasFileName, format)

        
#checkAlignImageMode(maxImageW,maxImageH,imageName,exportDir)       
            
                
#os.remove("c:/temp/aaaa/abcde.atlas")                      
def writeAtlasFile(imageName,pageCount,exportDir,maxImageW,maxImageH,currentImageAtlasData):
    atlasFileName = exportDir+'/'+imageName + '.atlas'

    
    if pageCount == 0:
        imageAtlasFileName = imageName + '.png'
        atlasFileName = exportDir+'/'+imageName + '.atlas'

        try:
            checkFile = os.path.isfile(atlasFileName)
            print "checkFile checkFile checkFile",checkFile
            if checkFile == True:
                print "remove remove remove file",atlasFileName
                os.remove(atlasFileName)
            else:
                pass
        except:
            pass
    
    else:
        imageAtlasFileName = imageName + str(pageCount+1)+'.png'
    f  = open(atlasFileName, "a")
    f.write('\n')

    f.write(imageAtlasFileName+'\n')
    f.write("size: "+str(maxImageW)+','+str(maxImageH)+'\n')
    f.write("format: RGBA8888"+'\n')
    f.write("filter: Linear,Linear"+'\n')
    f.write("repeat: none"+'\n')
    for i in currentImageAtlasData:
        image = i["image"]
        xy = str(i["x"])+", "+str(i["y"])
        size = str(i["w"])+", " +str(i["h"])
        offset = "0, 0"
        index= "-1"
        f.write(image+'\n')
        f.write("  rotate: false"+'\n')
        f.write("  xy: "+ xy +'\n')
        f.write("  size: "+ size +'\n')
        f.write("  orig: "+ size +'\n')
        f.write("  offset: "+ offset +'\n')
        f.write("  index: "+ index +'\n')

    f.close()
  #  fileName = 

def defineImageAtlasData(maxImageW,maxImageH,imageName):

    allImagesMeshInAtlas = cmds.listRelatives("imageAtlas",c=True,ad=True,type="mesh")
    print "allImagesMeshInAtlas allImagesMeshInAtlas_________111",allImagesMeshInAtlas
    allImageList = []
    allPageImagesAtlas = []
    allPages= []
    for i in allImagesMeshInAtlas:
        imagePlane = cmds.listRelatives(i,p=True,type="transform")[0]

        #print "imagePlane"
        allImageList.append(imagePlane)
        shadingGrps = cmds.listConnections(i,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)

        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')

        currentFile = cmds.getAttr("%s.fileTextureName" %fileNode[0])
        imageName = currentFile.split('/')[-1].split('.')[0]
        imageBB = cmds.exactWorldBoundingBox(imagePlane)   
        minX = imageBB[0]
        maxX = imageBB[3]
        minY = imageBB[1]
        maxY = imageBB[4]
        #if int(minY)/ int(maxImageH) >=0 and int(maxX)/int(maxImageW) <= 1:
       # print "ooooooooooooooo imageName",imageName,maxY,minY
        if maxY <= maxImageH and minY >= 0:
           # print  "currentFile",currentFile,minX,maxX,minY,maxY
            pageCount =  int(minX) / int(maxImageW)
            if pageCount in allPages:
                pass
            else:
                allPages.append(pageCount)
           # print "pageCount",pageCount
            x = int(minX -maxImageW*pageCount)
            y = int(maxImageH - maxY)
            image = ice.Load(currentFile)
            imageMetaData = image.GetMetaData()
            currentImage = i.split('/')[-1]
           # print "i i i i i i imageName",imageName

            #imageSize = imageMetaData['Original Size']
            w = int(imageMetaData['Original Size'].split(" ")[0].split("(")[1])
            h = int(imageMetaData['Original Size'].split(" ")[1].split(")")[0])
            allPageImagesAtlas.append({"image":imageName,"page":pageCount,"x":x,"y":y,"w":w,"h":h,"url":currentFile})    
    print "allPageImagesAtlas allPageImagesAtlas allPageImagesAtlas 000000000",allPageImagesAtlas
    return allPageImagesAtlas,allPages
#int(-3848)/2048
#cmds.nodeType("imageAtlasPlane_FG_BG")    
#cmds.exactWorldBoundingBox("imageAtlasPlane_Spiral_012_line")   
#alignAtlasImage()    
maxImageW = 2048    
maxImageH = 2048
imageName = "abcde"
exportDir = "//mcd-one/3d_project/candy_rush_v01/assets/other/win_line_a/rigging/scenes/export"
#checkAlignImageMode(maxImageW,maxImageH,imageName,exportDir)       
    
    
    
    