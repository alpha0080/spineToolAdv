allLambertShaderLiset = cmds.ls(type='lambert')
allNeedShaderList = []
for i in allLambertShaderLiset:
    linkList = cmds.listConnections(i)
  #  print linkList
    for j in linkList:
        print j
        try:
            if cmds.getAttr('%s.spine_tag'%j) == 'spine_slot':
                print j
                if j in allDeleteShaderList:
                    pass
                else:
                    allNeedShaderList.append(i)
        except:
            pass
        