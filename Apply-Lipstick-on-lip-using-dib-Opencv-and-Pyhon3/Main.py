# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:57:03 2019

@author: Sushant
"""

import numpy as np
import cv2
import dlib

#img = cv2.imread('Img1.jpg',0)
#cv2.imshow('Input_Image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

def Rectangle_to_Bounding_Box(Rectangle):
    
    x=Rectangle.left()
    y=Rectangle.top()
    w=Rectangle.right() - x
    h=Rectangle.bottom() - y
    
    return(x,y,w,h)
    
    
def FaceShape_to_CoOrd(FaceShape,datype="int"):
    CoOrd=np.zeros((68,2),dtype=datype)
    
    for Index in range(0,68):
        CoOrd[Index]=(FaceShape.part(Index).x,FaceShape.part(Index).y)     
    return CoOrd


#initializing dlib’s pre-trained face detector based on
# the standard Histogram of Oriented Gradients and Linear SVM method for object detection...
Detector=dlib.get_frontal_face_detector()   
Predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

### Preprocessing...
image=cv2.imread("Img1.jpg") #Reading the input image...
image=cv2.resize(image,(500,500)) #Resize the input image in standard 500*500    
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Convert RGB image into Gray...

### Extracting the ROI...
### For lip coordinates are from 48 to 68 
Rectangles=Detector(gray,1)

lip_Coord={48,68}

for (i,Rectangle) in enumerate(Rectangles):
    FaceShape=Predictor(gray,Rectangle)
    Face_CoOrdinates=FaceShape_to_CoOrd(FaceShape)  # Extract the Coordinates of ROI from shape...
    	
    clone = image.copy()
    for (x, y) in Face_CoOrdinates[48:68]:
        cv2.circle(clone, (x, y), 1, (0, 0, 255), -1)  #(I/P Image,center_coordinates,color,thickness)
        # extract the ROI of the face region as a separate image
    (x, y, w, h) = cv2.boundingRect(np.array([Face_CoOrdinates[48:68]]))
    roi = image[y:y + h, x:x + w]
    ROI = cv2.resize(roi, (250,250), cv2.INTER_CUBIC)
    
    (X,Y,W,H)=Rectangle_to_Bounding_Box(Rectangle)  # to covert 2 parameter of rectangle into 4 parameter of bounding box
    cv2.rectangle(clone,(X,Y),(X+W,Y+H),(0,255,0),2) #Write Rectangle on Input image...
    
#    cv2.imshow("ROI", ROI)   # Extracted ROI of lip..
#    cv2.imshow("Image", clone)  # Image with face detected and lip points...

    
    Temp_Image=image.copy()
    Image_With_Lipstick=image.copy()
    	
    lipStick_Color=[(0,0,255)]
    points=Face_CoOrdinates[48:68]
    
    hull = cv2.convexHull(points)   #  TO join the lip points.... 
    cv2.drawContours(Temp_Image, [hull], -1, lipStick_Color[i], -1)
    cv2.addWeighted(Temp_Image,0.2,Image_With_Lipstick,1-0.1,0,Image_With_Lipstick) # represnt that region on image...
    
    cv2.imshow("Output_Image",Image_With_Lipstick)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    