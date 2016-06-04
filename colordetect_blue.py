import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def count (im):
    l=0
    print im.shape
    for i in range(0,480):
        for j in range(0,640):
            #print "op" +str(l)
            if(im[i,j].all()!=0):
                l+=1
            j+=1
        i+=1
    return l

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !
    
    lower_blue = np.array([30,100,100], dtype=np.uint8)
    upper_blue = np.array([255,160,160], dtype=np.uint8)
    lower_red = np.array([100,100,30], dtype=np.uint8)
    upper_red = np.array([160,160,255], dtype=np.uint8)
    lower_green = np.array([100,30,100], dtype=np.uint8)
    upper_green = np.array([160,255,160], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(frame,frame, mask= mask1)
    res2 = cv2.bitwise_and(frame,frame, mask= mask2)
    res3 = cv2.bitwise_and(frame,frame, mask= mask3)
    kernel = np.ones((2,2),np.uint8)
    res1=cv2.morphologyEx(res1,cv2.MORPH_OPEN, kernel)
    res2=cv2.morphologyEx(res2,cv2.MORPH_OPEN, kernel)
    res3=cv2.morphologyEx(res3,cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame',frame)
    #cv2.imshow('red',res1)
    #cv2.imshow('green',res2)
    cv2.imshow('blue',res3)
    """rc= count (res1)
    gc= count(res2)
    bc= count(res3)
    print rc
    print gc
    print bc"""
    
    #cv2.imshow('res',res1)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
