import cv2 #import cv2 package

pic=cv2.imread('pic.jpg',-1) #read given image original copy and save into variable pic
print(pic) #print image in matric format (representing each pixels in the image)
cv2.imshow('image',pic) #show image in picture format , the first paramter is just the window name
key=cv2.waitKey() #wait for a key to be pressed

if key==27: #if escape(27) key is pressed close image window
    cv2.destroyAllWindows()
elif key==ord('s'): #else if s is pressedc create a png copy of image then close window
    cv2.imwrite('pic2.png', pic)
    cv2.destroyAllWindows()
