from PIL import Image
import os
import cv2 as cv
import numpy as np

def center_crop(img, dim, center):
    width, height = img.shape[1], img.shape[0]

    crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
    crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
	# mid_x, mid_y = int(width/2), int(height/2)
    mid_x, mid_y = center[0], center[1]
    cw2, ch2 = int(crop_width/2), int(crop_height/2) 
    crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
    return crop_img

def resize(img, dim):
    return cv.resize(img, dim)


#input = "C://Users//Richa//Desktop//HAT//datasets//planet//original"
input = ""
output = ""

dir_list = os.listdir(input)
center = (500, 500)
i = 0
j = 0
for image in dir_list:
    i += 1
    j += 1
    for row in range(0, 5):
        for col in range(0, 5):
            img = cv.imread(input + "//" + image)
            crop = (center[0]+ row*64, center[1]+col*64)
            #img = cv.resize(img, (896, 896)) 
            img = center_crop(img, (64, 64), crop)
            cv.imwrite(output + str(i) + "-" + str(j) + "-" + image, img)
            j += 1