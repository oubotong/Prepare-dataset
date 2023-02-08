# Prepare-dataset

## cut.py
This is the file for cutting off 64x64 sub-images out of large original images (e.g. Gaofen-2).
```
# Put absoluate path of the input high-resolution into input variable
# Put absoluate path of the output folder into output variable for storing the 64x64 images
input = "" 
out = ""
```

## resize.py
This is the file for resizing images to a different resolution (e.g. 64x64x -> 256x256).
```
# Put absoluate path of the input 64x64 low-resolution into input variable
# Put absoluate path of the output folder into output variable for storing the 256x256 or resized images
input = "" 
out = ""
```

##sharpness.py
This is the file used to calculate the sharpness of all images in a folder and store them into a `.csv` file
```
# Put absoluate path of the image folder into path1 variable
path1 = ""
```
