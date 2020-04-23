
#####################
import cv2
import numpy as np

def getTextOverlay(img):
    '''
    Parameters
    ----------
    img : Mat
        Input RGB image.
    mask : Mat
        text segmented from input image using HSV based thresholding..
    imagent : Mat
        text segmented from input image using binary thresholding to remove false positive..

    Returns
    -------
    output : Mat
        Text extracted overlay.

    '''
    # output = np.zeros(img.shape, dtype=np.uint8)
    # img = cv2.resize(img,(500,600)) 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0,0  , 0])
    upper = np.array([180, 255,30])
    mask = cv2.inRange(hsv, lower, upper)
    
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    min_width_of_char =35
    min_height_of_char =55
    for contour in contours:
            [x, y, w, h] = cv2.boundingRect(contour)
            if w < min_width_of_char and h < min_height_of_char:
                continue
            cv2.drawContours(mask, [contour], -1, (255,0,255), -1)
            # cropped = mask[y :y +  h , x : x + w]
    ###########################################################################
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray,(11,11),0)
    
    # edges = cv2.Canny(blur,18,76,L2gradient=True)   
    thresh_value = np.amax(gray)*0.13
    thresh = cv2.threshold(blur,thresh_value, 255, cv2.THRESH_BINARY)[1]
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,3))
    erode = cv2.erode(thresh, kernel, iterations=1)
    imagent=cv2.bitwise_not(erode)
    ###########################################################################
    
    output=cv2.bitwise_and(imagent,mask)  
    output=cv2.bitwise_not(output)    
    # cv2.imshow("out_img",mask)
    # cv2.waitKey(0) 

    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text1.png', output)
#####################

