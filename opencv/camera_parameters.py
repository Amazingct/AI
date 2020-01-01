import cv2
cap = cv2.VideoCapture(0)

#creating a function to keep showing video capture, function takes end_command which is key to press to exist function
def show_vid(end_command):
    while 1:
        ret, frame = cap.read()
        cv2.imshow('Webcam', frame) 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Webcam_gray', gray) 
        if cv2.waitKey(1) == ord(end_command):  
            break







print(cap.isOpened())
#print defualt video size
print("the frame width is", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("the frame height is", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#change video size
cap.set(cv2.CAP_PROP_FRAME_WIDTH,200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,200)

#keep showing video
show_vid('w')



cap.release()  
cv2.destroyAllWindows()
