# Apply_Lipstick_on_lip_using_dib_Opencv_and_Pyhon3.

## Libraries used:
--> dlib
--> OpenCV
--> Numpy

## This project has three main part as follow:
1) Face Detection from given input Image.
2) Extract ROI (Lip part) from the face.
3) Apply the RGB values on lip region. 

### 1. Detection of face region:
- To detect face region from an input image. Here I used shape predictor method which pre-trained in dlib library. Shape predictor uses HOG and linear SVM object detector to localize the face in the image, and facial landmark method to detect the facial structures on the face region. 

- Facial landmark is a trained detector, it gives structural coordinates of the face. Using iBUG 300-W data set it to give 1 to 68 coordinates face region.

- "shape_predictor_68_face_landmarks.dat" this is the training file taken from dlib. It is available on official Dlib website.

```bash
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
```

### 2. Extracting the lip region from face:
- Facial landmarks give 68 coordinates of face, out of the 48 to 68 represents lip part. So, extract that point from shape predictor for a given input image. 

### 3. applying RGB values on lip region:
- For connecting that points and to create a region "Convex Hull" method is used. Using the convex set represented the lip region on the face. then applied RGB values on that same region.
#### Note: Python takes BGR values not RGB. 

## Program Flow:
- Using "shape_predictor_68_face_landmarks.dat" file extract the facial structure coordinates (using predictor) and rectangle for face region (using detector).
```bash
dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
```

- Detector gives only (x,y) coordinates of rectangle but to represent rectangle using cv2 need 4 values(x,y,width,height). for the same Rectangle_to_Bounding_Box() function is created.
```bash
dlib.get_frontal_face_detector() 
```

- Also predictor gives 68 (x,y) coordinates of face region. For our conveniance converted in array using FaceShape_to_CoOrd() function.

- Take an input image, resize it into the standard format.

- Using for loop represent that point on the input image(48 to 68). Apply convex hull for that points and create a region for lip using cv2.circle().

- Apply BGR values on that region. and show a final output image with applied lipstick.
