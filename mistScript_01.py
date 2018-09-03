'{:04d}'.format(1)
SaberArtGoStage2_surfaceShader

cmds.nodeType('polySurface12')

cmds.getAttr('polySurface17.spine_tag')

obj = cmds.ls(sl=True)[0]
#parentBone = cmds.listRelatives(obj,p=True)[0]
getObj =  cmds.ls(obj,dag=1)[1]
shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
fileNode = cmds.listConnections('%s.outColor' % (shaders[0]), type='file')
currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
fileInSlot = currentFile.split("/")[-1].split(".png")[0]