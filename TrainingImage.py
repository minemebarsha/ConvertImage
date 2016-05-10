import glob
import os
import re
import sys
from PIL import Image
from numpy import savetxt

# function to take an image file and coordinate and output to given location
def convertToZeroOne(in_img_filename, in_cordinate_file, out_file_loc):
    
    im = Image.open(in_img_filename)    
    imN = Image.new("L", im.size)
    txt = open(in_cordinate_file)
    
    line = txt.readline()
    cordinates = line.split(' ')
    x1 = int(cordinates[0])
    y1 = int(cordinates[1])
    x2 = int(cordinates[2])
    y2 = int(cordinates[3])
    
    point1 = (x1 + 25, y1 + 35)
    point2 = (x2, y2)
    
    imageW = im.size[0]
    imageH = im.size[1]
    
    for y in range(0, imageH):
      for x in range(0, imageW):
        xy = (x, y)
        imN.putpixel(xy, 0)
#         print imN.getpixel(xy)
    
    imN.putpixel(point1, 1)
    imN.putpixel(point2, 1)
    
    
    imN.save(out_file_loc)

# ==============================================Main============================================
img_top_loc = "/u/koller/work/signlanguage/setups/features/phoenix-cont/all.20120120/magdalena-orig/data/01.feature-extraction-orig-210-260-TRAIN-colorChannels3.dump/RWTH-PHOENIX-v02-split01-CLEANED.compound/"

cordinate_loc = "/work/cv2/koller/features/phoenix-cont/all.20120120/magdalena-tracking-groundtrouth-newIds.20120626/data/manualAnnotations/train/right-hand-frames/RWTH-PHOENIX-v02-split01-CLEANED.compound/"

out_dir = "/work/cv3/zaman/TraningImageOutput"

sub_dir_with_img = "/1/u/signlanguage/phoenix/video/divx2pass/all-years"


list_img_dir = os.listdir(img_top_loc)

# list_cordinate_dir = os.listdir(cordinate_loc)

count = 0

for index, it in enumerate(list_img_dir):
    full_img_dir = img_top_loc + it + sub_dir_with_img
    list_img_file = glob.glob(full_img_dir + "/*.png")
    list_img_file.sort()
    
    full_cordinate_dir = cordinate_loc + it
    list_cordinate_file = glob.glob(full_cordinate_dir + "/*.png")
    list_cordinate_file.sort()
    full_out_dir = out_dir + it
    
    if not os.path.exists(full_out_dir):
        os.mkdir(full_out_dir)

    if len(list_img_file) == len(list_cordinate_file):
        for indx, item in enumerate(list_img_file):
             out_file_loc = list_cordinate_file[indx].replace(cordinate_loc, out_dir)
             if os.path.exists(out_file_loc):
                 os.remove(out_file_loc)
             print out_file_loc
             convertToZeroOne(list_img_file[indx], list_cordinate_file[indx], out_file_loc)
    count = count + 1
             
print count
