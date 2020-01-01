import cv2 #import cv2 package
import numpy as np
events =[i for i in dir(cv2) if 'EVENT' in i]
print(events)
#code to join to points clicked together by a line
#interrupt handler for mouse click events###########
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(pic,(x,y), 3, (25,33,55),-1)
            #image,cordinte,radiius,color, the minus 1 is to fill the circle with the color
        points.append((x,y)) #append cordinates, so it holds previous and new cordinates
        if len(points)>=2:
            cv2.line(pic,points[-1],points[-2],(3,44,55),5) # -1 for last point, -2 for point bfor the last
        cv2.imshow('image', pic)

    
#////////////////////////////////////////////////////////////#

pic=cv2.imread('lena.jpg',-1)
cv2.imshow('image',pic)
points=[] #array to hold points cordinates

#this is like attaching the interrupt nd directing it to the handler
cv2.setMouseCallback('image', click_event) #this calls the clic_event function and pass some prameters; the event which has happened, the mouse cordinate etc


key=cv2.waitKey() 
if key==27: #escape(27) 
    cv2.destroyAllWindows()

