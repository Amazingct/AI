import cv2

# this is a simple code to use the webcam to capture video

cap = cv2.VideoCapture(0)  # u can pass the file nane as parameter or 0 for the computer camera
print(cap.isOpened())  # this print 1 or 0 dependending on if the capture has begun or not
while 1:
    ret, frame = cap.read()

    # ret is varaiable that saves true or false
    # depending on if a frame is available or not
    # while variable frame saves the frameq

    cv2.imshow('Webcam', frame)  # display each frame
    # the first parameter 'Webcam' is just name of the opened window while the second is the variable holding the frame
    if cv2.waitKey(10) == ord('q'):  # quit window when q is pressed
        break
cap.release()  # release the cap variable
cv2.destroyAllWindows()