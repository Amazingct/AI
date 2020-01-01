import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('my_face_recongnition/cascades/data/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)  # u can pass the file nane as parameter or 0 for the computer camera

while cap.isOpened():
    ret, frame = cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,15) #returns a list containing cordinate(x,y) and the size(w,h) of the face detected
                                       #image,scalefactor,minNeigbours

    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0),) #simply create a retangle on the ROi(face)
                    #picture,starting cordinate,end cordinates, color,thickness
    

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(10) == ord('q'):  
        break
cap.release()  
cv2.destroyAllWindows()