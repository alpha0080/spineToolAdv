import sys
import shutil

fileList = ["//mcd-one/database/assets/scripts/maya_scripts/spineTool.py",
            "//mcd-one/database/assets/scripts/maya_scripts/spineTool2.py",
            "//mcd-one/database/assets/scripts/python2.7_alpha/22/spineUI_A.py",
            "//mcd-one/database/assets/scripts/python2.7_alpha/22/spineExtraTool.py",
            "//mcd-one/database/assets/scripts/python2.7_alpha/22/spineMainTool.py"
            ]

targetDir = "C:/Users/alpha/Documents/GitHub/spineToolAdv"

for i in fileList:
    targetFile = targetDir + '/' + i.split('/')[-1] 
    shutil.copyfile(i,targetFile)