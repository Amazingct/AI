import cv2 #import cv2 package
import numpy as np
events =[i for i in dir(cv2) if 'EVENT' in i]
print(events)

#interrupt handler for mouse click events###########
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy_val=str(x)+','+str(y)
        print(xy_val)
        font =cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,xy_val,(x,y),font,0.5,(255,0,50),1)
        cv2.imshow('image', pic)

    if event == cv2.EVENT_RBUTTONDOWN:
        #get the rgb value of the pointed cordinate
        blue=pic[y,x,0]
        green=pic[y,x,1]
        red=pic[y,x,2]
        bgr=str(blue)+','+str(green)+','+str(red)
        print(bgr)
        font =cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,bgr,(x,y),font,0.5,(111,50,50),1)
        cv2.imshow('image', pic)
#////////////////////////////////////////////////////////////#

pic=cv2.imread('messi5.jpg',-1)
cv2.imshow('image',pic)

#this is like attaching the interrupt nd directing it to the handler
cv2.setMouseCallback('image', click_event) #this calls the clic_event function and pass some prameters; the event which has happened, the mouse cordinate etc


key=cv2.waitKey() 
if key==27: #escape(27) 
    cv2.destroyAllWindows()

