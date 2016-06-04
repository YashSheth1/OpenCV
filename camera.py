import cv2
import numpy as np

"""def contrast(r):
    l=255-r
    m=255-r
    n=255-r

    return (l,m,n)
"""
cap =cv2.VideoCapture(0)
while (cap.isOpened()):
    #BGR image feed from camera
    ret,img =cap.read()
    #
    #BGR to gray conversion
    img2 =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale',img2)

    k=cv2.waitKey(10)
    checking for an esc key press
    if k== 27:
        break

"""
    r,g,b=contrast(img2[200,200])
    cv2.circle(img,(200,200),24, (r,g,b),-1)
    cv2.imshow('output',img)
"""

               
    #BGR to binary (RED)thresholded image
    imgthreshold=cv2.inRange(img,cv2.cv.Scalar(3,3,125),cv2.cv.Scalar(40,40,255),)
    cv2.imshow('thresholded',imgthreshold)
                             
    


cap.release()
cv2.destroyAllWindows()

