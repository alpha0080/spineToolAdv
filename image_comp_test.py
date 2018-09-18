import os, math,time

try:
    sys.path.append("C:/Program Files/Pixar/RenderManProServer-22.1/lib/python2.7/Libs/ite-packages")
    #sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.7/lib/python2.7/Lib/site-packages")

    import ice
except:
    pass
     
import ice


max_frames_row = 10.0
frames = []
tile_width = 0
tile_height = 0

spritesheet_width = 0
spritesheet_height = 0

folder = "C:/Temp/testImage/1"
files = os.listdir(folder)
files.sort()
#print(files)


for i in files:
    filename = folder +'/' +i
    image = ice.Load(filename)
    imageMetaData = image.GetMetaData()
    frames.append(imageMetaData)
    
print frames
   # imageSize = imageMetaData['Original Size']
    #imageWidth = int(imageMetaData['Original Size'].split(" ")[0].split("(")[1])
    #imageHeight = int(imageMetaData['Original Size'].split(" ")[1].split(")")[0])


###ref https://minzkraut.com/2016/11/23/making-a-simple-spritesheet-generator-in-python/