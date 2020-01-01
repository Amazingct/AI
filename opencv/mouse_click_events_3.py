import cv2 #import cv2 package
import numpy as np
#events =[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue=pic[y,x,0]
        green=pic[y,x,1]
        red=pic[y,x,2]

        #cv2.circle(pic,(x,y),3,(0,0,255), -1)
        mycolor=np.zeros((512,512,3),np.uint8) #create a one color image using np
        mycolor[:] =[blue,green,red]
        cv2.imshow('color', mycolor)


        





pic=cv2.imread('lena.jpg',-1)
cv2.imshow('image',pic)

cv2.setMouseCallback('image', click_event)


key=cv2.waitKey() 

if key==27: #escape(27) 
    cv2.destroyAllWindows()

