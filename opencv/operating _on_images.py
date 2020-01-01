import cv2
import numpy as np
picture=cv2.imread('messi5.jpg')#creating an object picture of class cv2.imread(),
#now picture can assess all the methods and attributes
picture2=cv2.imread('opencv-logo.png')
cv2.waitKey(2000)

print(picture.shape)#using the method .shape which returns a turple of number of rows,colum and channel
r,c,ch =picture.shape
print(picture.size)#returns number of pixels
print(r*c*ch)
#from this you will realize that the picture size(number of pixels) is simply the product of its no of rows, cols and channel
print(picture.dtype) #returns data type
b,g,r=cv2.split(picture)
picture=cv2.merge((b,g,r)) #note b,g,r is passed as a sigle argument in form of a turple

#getting a region of intreset
ball= picture[280:340,330:390]
picture[273:333,100:160] = ball

picture = cv2.resize(picture,(512,512))
picture2 = cv2.resize(picture2,(512,512))

#picture3=cv2.add(picture,picture2)
picture3=cv2.addWeighted(picture,.5,picture2,.5,0)
                        #first picture, the weight, 2nd picture and weight, gamma value = 0

cv2.imshow('messi',picture3)
key=cv2.waitKey() #wait for a key to be pressed

if key==27: #if escape(27) key is pressed close image window
    cv2.destroyAllWindows()
    

