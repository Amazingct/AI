import cv2 #import cv2 package
import numpy as np
#pic=np.zeros([512,512,3],np.uint8) #use numpy to create black image
pic=cv2.imread('pic.jpg',-1) #read given image original copy and save into variable pic
print(pic) #print image in matric format (representing each pixels in the image)
#draw over image
pic =cv2.line(pic,(0,0), (255,255),(255,0,0), 5)
            #image, start cordinate , end cordinate, color(RGB), thickness
pic =cv2.rectangle(pic,(384,0),(510,128),(0,0,255),5) 
pic =cv2.circle(pic,(447,63),63,(0,255,0),-1)
#writing text
font=cv2.FONT_HERSHEY_SIMPLEX
pic=cv2.putText(pic,'hit oo',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)

cv2.imshow('image',pic) #show image in picture format
key=cv2.waitKey() #wait for a key to be pressed

if key==27: #if escape(27) key is pressed close image window
    cv2.destroyAllWindows()
elif key==ord('s'): #else if s is pressedc create a png copy of image then close window
    cv2.imwrite('pic2.png', pic)
    cv2.destroyAllWindows()
