import ice

import os, math,time

max_frames_row = 10.0
frames = []
tile_width = 0
tile_height = 0

spritesheet_width = 0
spritesheet_height = 0

folder = "C:/Temp/testImage/1"
files = os.listdir(folder)
files.sort()
print(files)