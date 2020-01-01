import cv2


cap = cv2.VideoCapture(0)  

while 1:
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)  
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('snap.png', frame)
        cv2.imshow('snap', frame)
        cv2.waitKey(1000)
        
    if cv2.waitKey(20) == ord('c'): 
        break


cap.release() 
cv2.destroyAllWindows()
