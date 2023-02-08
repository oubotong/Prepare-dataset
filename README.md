# Prepare-dataset

## cut.py
This is the file for cutting off 64x64 sub-images out of large original images (e.g. Gaofen-2).
```python
# Put absoluate path of the input high-resolution into input variable
# Put absoluate path of the output folder into output variable for storing the 64x64 images
input = "" 
out = ""
```

## resize.py
This is the file for resizing images to a different resolution (e.g. 64x64x -> 256x256).
```python
# Put absoluate path of the input 64x64 low-resolution into input variable
# Put absoluate path of the output folder into output variable for storing the 256x256 or resized images
input = "" 
out = ""
```

## sharpness.py
This is the file used to calculate the sharpness of all images in a folder and store them into a `.csv` file

```python
# Put absoluate path of the image folder into path1 variable
path1 = ""
```

## HAT-L_SRx4.yml

This is the configuration file for running test.

```yml
# The field below is used to store your testing dataset HR and LR
# Adjust them according to your LR and HR images location
dataroot_gt: #HR
dataroot_lq: #LR

# This is the field used to store your pre-trained model location
pretrain_network_g: ./experiments/pretrained_models/HAT-L_SRx4_ImageNet-pretrain.pth
```

Then after setting this up, run the following command to test:

```SHELL
python hat/test.py -opt HAT-L_SRx4.yml
```

