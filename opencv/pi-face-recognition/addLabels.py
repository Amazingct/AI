import cv2
import os
import time
cap = cv2.VideoCapture(0)  # u can pass the file nane as parameter or 0 for the computer camera
print(cap.isOpened())  # this print 1 or 0 dependending on if the capture has begun or not
name=input("pls enter the new user name: ")
os.mkdir(name)
os.chdir(name)
picNo=0
font =cv2.FONT_HERSHEY_SIMPLEX
while 1:
    
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)  # display each frame
    key=cv2.waitKey(10) #wait for a key to be pressed
    if key == ord('q'):  # quit window when q is pressed
        break
    elif key==ord('s'): #else if s is pressedc create a png copy of image then close window
        picNo=picNo+1
        picName='0000'+ str(picNo) + '.jpg'
        cv2.imwrite(picName, frame)
        plane=cv2.putText(frame,picName,(3,4),font,3,(111,50,50),2)
        cv2.imshow('Webcam', plane)  # display each frame
        time.sleep(2)

        
    
cap.release()  # release the cap variable
cv2.destroyAllWindows()