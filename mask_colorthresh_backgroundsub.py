"""Try to detect the skin color, detect our entire body so as to find a human in the camera feed."""
import cv2 as cv
import cv2
import numpy as np

r,h,c,w = 250,90,400,125  # simply hardcoded the values
track_window = (c,r,w,h)

cap = cv2.VideoCapture(0)
#background subtracted image
fgbg = cv2.BackgroundSubtractorMOG()
while(1):

    # Take each frame
    _, frame = cap.read()
    
    

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([0,30,60])
    upper_blue = np.array([50,150,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(frame,frame, mask= mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
    res = cv2.morphologyEx(res1,cv2.MORPH_OPEN,kernel)
    #cv.Erode(res,res,None,1)
    
    fgmask = fgbg.apply(res)

    # set up the ROI for tracking
    roi = frame[r:r+h, c:c+w]
    hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi],[0],mask2,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    

    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('background subtracted',fgmask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
