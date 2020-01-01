import cv2
import datetime
cap = cv2.VideoCapture(0)  
font=cv2.FONT_HERSHEY_SIMPLEX



while 1:
    date_time=str(datetime.datetime.now())
    ret, frame = cap.read()
    frame=cv2.putText(frame,date_time,(10,50),font,0.5,(255,0,0))
    cv2.imshow('Webcam', frame)   


    if cv2.waitKey(1) == ord('q'):  
        break



cap.release()  
cv2.destroyAllWindows()
