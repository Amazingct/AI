#HSV

import cv2
import numpy as np


#cv2.namedWindow('window')
cap=cv2.VideoCapture(0)

while (1):
    _,frame=cap.read()
    #frame=cv2.imread('sample_pics/smarties.png')
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    lower_blue=np.array([10,100,20])
    upper_blue=np.array([20,255,100])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)



    if cv2.waitKey(10)==ord('q'):
        break
cap.Realease()
cv2.destroyAllWindows()