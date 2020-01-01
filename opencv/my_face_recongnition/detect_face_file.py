import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('my_face_recongnition/cascades/data/haarcascade_frontalface_default.xml')


 # u can pass the file nane as parameter or 0 for the computer camera
frame = cv2.imread('my_face_recongnition/dan1.jpeg')
gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,8)


for(x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0),3)

    
cv2.imshow('Webcam', frame)

key=cv2.waitKey() #wait for a key to be pressed

if key==27: #if escape(27) key is pressed close image window
    cv2.destroyAllWindows()