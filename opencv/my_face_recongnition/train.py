import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('my_face_recongnition/cascades/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('my_face_recongnition/cascades/data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)  # u can pass the file nane as parameter or 0 for the computer camera

while cap.isOpened():
    ret, frame = cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,8) #returns a list containing cordinate(x,y) and the size(w,h) of the face detected
                                       #image,scalefactor,minNeigbours
    eyes=eye_cascade.detectMultiScale(gray,1.1,8)
    #print(faces)
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h,x:x+w] #get the roi[face] in gray
        roi_color=frame[y:y+h,x:x+w] #get the roi[face] in  color
        cv2.imwrite('my face.jpg',roi_color)#save the face

    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0),) #simply create a retangle on the ROi(face)
                    #picture,starting cordinate,end cordinates, color,thickness
    
    #eyes
        for(ex,ey,ew,eh) in eyes:
            roi_gray=gray[ey:ey+h,ex:ex+ew] #get the roi[face] in gray
        roi_color=frame[ey:ey+eh,ex:ex+ew] #get the roi[face] in  color
        #cv2.imwrite('my face.jpg',roi_color)#save the face

    
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh), (255,0,0),) #simply create a retangle on the ROi(face)
                    #picture,starting cordinate,end cordinates, color,thickness
    




    cv2.imshow('Webcam', frame)
    if cv2.waitKey(10) == ord('q'):  
        break
cap.release()  
cv2.destroyAllWindows()