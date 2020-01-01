import cv2
import numpy as np

def nothing(x):
    print (x)

cv2.namedWindow('image')
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('switch','image',0,1,nothing)
pic=np.zeros((300,512,3), np.uint8)

while(1):
    cv2.imshow('image',pic)
    key = cv2.waitKey(10)
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos('switch','image')
    print(b,g,r)
    if s==0:
        pic[:]=0
    else:
        pic[:]=[b,g,r]

    if key == ord('q'):
        break

cv2.destroyAllWindows()