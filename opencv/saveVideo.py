import cv2
#this is a simple code to use the webcam to capture video

cap=cv2.VideoCapture(0) # u can pass the file nane as parameter or 0 for the computer camera
fourcc=cv2.VideoWriter_fourcc(*'XVID') #google more abot fourcc. its basically format of video
out=cv2.VideoWriter('capturedVid.avi',fourcc,20.0,(640,480) )
#the first arg(parameter) above is the name to save the video, 2nd is the fourcc format
#3rd is the frame per sec value, last is the frame size, these are all defualt values
print(cap.isOpened()) #this print 1 or 0 dependending on if the capture has begun or not
while(1):
    ret, frame = cap.read() 
    if ret==1:
    
        #ret is varaiable that saves true or false
        #depending on if a frame is available or not
        #while variable frame saves the frame
        out.write(frame) #write each frame to out
        cv2.imshow('Webcam', frame) #display each frame
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #save each frame in gray color into variable gray
        cv2.imshow('Webcam_gray', gray) #display the gray frame in a new window
        #the first parameter 'Webcam' is just name of the opened window while the second is the variable holding the frame
        if cv2.waitKey(1)==ord('q'): #quit window when q is pressed
            break
    else:
        break
cap.release() #release the cap variable
cv2.destroyAllWindows()

