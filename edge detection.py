import cv2
import numpy as np
from matplotlib import pyplot as plt
cap =cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    #img = cv2.imread('frame',0)
    edges = cv2.Canny(frame,200,200)

    plt.subplot(121),plt.imshow(frame,cmap = 'gray')
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('edges',edges)
    cv2.imshow('normal',frame)
    
   # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    #plt.show('edges',gray)
    if cv2.waitKey(1) & 0xFF == (ord('q')):
        break
    #plt.show()
cap.release()
cv2.destroyAllWindows()
