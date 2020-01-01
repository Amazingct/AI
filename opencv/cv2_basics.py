import cv2 #import cv2 package
import imutils

pic=cv2.imread('messi5.jpg') 
print(pic) 
cv2.imshow('image',pic) 
key=cv2.waitKey() 
(h,w,d) = pic.shape #returns height, width and No of channels
print("w={},h={},d={}".format(w,h,d))
(b,g,r) =pic[100,50] #accessing a particular pixel (y,x)
print("b={},g={},r={}".format(b,g,r))
#extracting ROI [ystart:ystop, xstart:xstop]:array slicing
roi =pic[100:150, 50:100]
cv2.imshow('roi',roi)
key=cv2.waitKey()
#resizing image
#1. ignoring aspect ratio (w,h)
resized =cv2.resize(pic, (100,200))
cv2.imshow("resized", resized)
key=cv2.waitKey()
print(resized.shape)
#2. considering aspect ratio
r = w/h #first we get the aspect ratio
dim = (int(300*r),300) #chose the height, then multiply the height by the ratio to get the width
resized2=cv2.resize(pic,dim)
cv2.imshow("resized2", resized2)
key=cv2.waitKey()
print(resized2.shape)
#3. using imutils module(automatically retaining the aspect ratio)
resized3 =imutils.resize(pic, height=300)
cv2.imshow("resized3", resized3)
key=cv2.waitKey()
print(resized3.shape)
#rotating an image
#1. using cv2
print(h/2,w/2) #normal division
print(h//2,w//2) #division ignoring floating points
center =(w//2,h//2)
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated =cv2.warpAffine(pic,M,(w,h))
cv2.imshow("rotated", rotated)
key=cv2.waitKey()
#2.using imutils
rotated2=imutils.rotate(pic,-90)
cv2.imshow("rotated2", rotated2)
key=cv2.waitKey()
#.3 keeping the whole picture after rotation
rotated3=imutils.rotate_bound(pic,-90)
cv2.imshow("rotated3", rotated3)
key=cv2.waitKey()

