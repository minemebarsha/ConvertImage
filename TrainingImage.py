#!/usr/bin/env python

import Image
import glob
from numpy import savetxt
import os
import re
import sys
import shlex
import subprocess

# function to take an image file and coordinate and output to given location
def convertToZeroOne(in_img_filename, cordinate, out_file_loc):

    im = Image.open(in_img_filename)
    imN = Image.new("L", im.size)
    cordinates = cordinate.split(" ")
    
    x = int(float(cordinates[2]))
    y = int(float(cordinates[3]))

    point = (x + 25, y + 35)

#     imageW = im.size[0]
#     imageH = im.size[1]
#      
#     for y in range(0, imageH):
#       for x in range(0, imageW):
#         xy = (x, y)
#         imN.putpixel(xy, 1)
#          print imN.getpixel(xy)

    imN.putpixel(point, 1)

    imN.save(out_file_loc)


# function to take an Directory name and read values from cache and return the list of the values
def getCordinates(Dir_Name):
    cmd = "/work/cv2/koller/executables/sprint/sprint-oscar-posterior2ndtry/archiver.linux-x86_64-standard --mode show --type feat /work/cv2/koller/features/phoenix-cont/all.20120120/magdalena-tracking-groundtrouth-newIds.20120626/data/01.Tracking-Groundtrouth-RH.TRAIN.features.cache RWTH-PHOENIX-v02-split01-CLEANED.compound/" + Dir_Name + "/1"
    args = shlex.split(str(cmd))
    try:
        a = subprocess.Popen(args, stdout=subprocess.PIPE)
        (stdoutdata, stderrdata2) = a.communicate()
    except:
        print stderrdata2
        raise
    stdoutdata_by_line = stdoutdata.split("\n")
    lines = list()
    for i in range(2, len(stdoutdata_by_line) - 2):
        lines.append(stdoutdata_by_line[i])
    return lines



# ==============================================Main============================================
img_top_loc = "/u/koller/work/signlanguage/setups/features/phoenix-cont/all.20120120/magdalena-orig/data/01.feature-extraction-orig-210-260-TRAIN-colorChannels3.dump/RWTH-PHOENIX-v02-split01-CLEANED.compound/"

out_dir = "/u/zaman/Documents/TraningImageOutput/"

sub_dir_with_img = "/1/u/signlanguage/phoenix/video/divx2pass/all-years"


list_img_dir = os.listdir(img_top_loc)

# list_cordinate_dir = os.listdir(cordinate_loc)


for index, it in enumerate(list_img_dir):
    print it
    full_img_dir = img_top_loc + it + sub_dir_with_img
    list_img_file = glob.glob(full_img_dir + "/*.png")
    list_img_file.sort()
    
    cordinates_for_dir = getCordinates(it)
    
    if(len(list_img_file) == len(cordinates_for_dir)):
        
        full_out_dir = out_dir + it
         
        if not os.path.exists(full_out_dir):
            os.mkdir(full_out_dir)
        
        for indx, item in enumerate(list_img_file):
             out_file_loc = list_img_file[indx].replace(img_top_loc, out_dir).replace(sub_dir_with_img, "")
             if os.path.exists(out_file_loc):
                 os.remove(out_file_loc)
#              print out_file_loc
             convertToZeroOne(list_img_file[indx], cordinates_for_dir[indx], out_file_loc)
             
