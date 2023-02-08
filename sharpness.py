from PIL import Image
import cv2 as cv
import numpy as np
import os
import csv
import pandas as pd 

def calculateSharpness(path):
    res = []
    dir_list = os.listdir(path)

    for image in dir_list:
        img = cv.imread(path + "//" + image)
        img_HLS = cv.cvtColor(img, cv.COLOR_BGR2HLS)
        L = img_HLS[:, :, 1]
        u = np.mean(L)
        LP = cv.Laplacian(L, cv.CV_64F).var()
        s = np.sum(LP/u)
        res.append(s)
    return res


#path1 = "E://Download//64x64"
path1 = ""

res1 = calculateSharpness(path1)
pd.DataFrame({'64x64':res1}).to_csv('res.csv')

# You can also combine several results together and store them into csv file


#path2 = ""
#path3 = ""
# res2 = calculateSharpness(path2)
# res3 = calculateSharpness(path3)
#pd.DataFrame({'64x64':res1,'256-HAT':res2,'256-NAFSSR':res3}).to_csv('res.csv')