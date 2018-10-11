import shutil


fileList =[ "//mcd-one/database/assets/scripts/maya_scripts/spineTool2.py","//mcd-one/database/assets/scripts/python2.7_alpha/22/spineUI_A.py"]
targetDir = "C:/Users/alpha/Documents/GitHub/spineToolAdv"
for i in fileList:
    fileName = i.split('/')[-1]
    longFileName = targetDir +'/'+fileName
    print longFileName 

    shutil.copyfile(i,longFileName)  
