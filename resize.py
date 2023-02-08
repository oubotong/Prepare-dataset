from PIL import Image
import os
import cv2 as cv
import numpy as np

def resize(img, dim):
    return cv.resize(img, dim)


#intput = "C://Users//Richa//Desktop//HAT//datasets//planet//LR"
input = ""
output = ""
dir_list = os.listdir(path)
center = (500, 500)
for image in dir_list:
    img = cv.imread(input + "//" + image)
    img = resize(img, (256, 256))
    cv.imwrite(output + image, img)