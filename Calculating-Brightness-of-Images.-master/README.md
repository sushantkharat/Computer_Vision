
# README file for detecting the brightness of Images code.

# Image Brightness Detection:
## Problem statement:

Develop a generalized algorithm to detect the brightness of any image. Your algorithm should take an image as input and give a score between (0-10) as output (zero being low bright and 10 being high bright). You will not be provided with data for training.

## Introduction:
Brightness is one of the most significant pixel characteristics. For this assignment I used Matlab platform. Folder Sushant_Assignment contain all files as following: 
#### 1.Main.m → Program file developed in matlab.
#### 2.Dataset → It contain Images (Which used for testing the output) as a dataset.
#### 3.README.md
 
## Working:
In the initial step, the RGB or Grayscale image picked up from the folder which contains all image files. Then the algorithm takes all the images present in that folder.

### The step-by-step procedure of the proposed system:
#### -> Image Acquisition.
#### -> Convert Image into HSV format if image is RGB.
#### -> In HSV format V(Value is Brightness). So Extract that value.
#### -> If GrayScale Image then take Mean of pixel values present in the that Image.
#### -> Mapped that Brightness values to range of 0 to 10. 0 is the lowest brightness and 10 is the highest.

### Colour Transformation:
HSV (hue, saturation, value) color model is a popular color model because it is based on human perception.
After transformation, only the V (Brightness) component of HSV colour space is taken into account since it provides us with the required information.

### Mapping Of Brightness Values:
This program gives output( Brightness of image based on gray values) between 0 to 10 only. Actually brightness of image is not in between 0 to 10 every time. It's varies between minimun intensity value to maximum intensity value. So, for getting desired output mapping needs. According to that mapping was done. 

## Note :  This program get all images present in the folder and gives output at one time. If you want to find out any particular image output. You need to put the breakpoint at mentioned in program.








