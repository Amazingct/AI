import imutils as im
import cv2 as cv
import argparse as apa

#program will require user to input an image path as an argument when running this script

#create an argumentparser object
ap = apa.ArgumentParser()
#use the method add_arguement("option","--the variable to hold the arg", properties e'g if it is required or not or additional info)
ap.add_argument("-i","--image", required=True, help="path to inpute image")
args=vars(ap.parse_args())
#pass image path to imread methode
image=cv.imread(args["image"])
cv.imshow("image", image)
cv.waitKey(0)
#convert image to gray
gray =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("gray_image", gray)
cv.waitKey(0)
#detecting image edges 
edged=cv.Canny(image,30,150)
cv.imshow("edged", edged)
cv.waitKey(0)
#thresholding
#here, we changing anycolor (the blocks)less than 230 (recall white=255, black=0) to 255
#and anything (the gray image bckground) greater or equal to 255 to 0
thresh =cv.threshold(gray,230,255,cv.THRESH_BINARY_INV)[1]

cv.imshow("thresh", thresh)
cv.waitKey(0)
#finding contours (outlines) of the block in the thershld image
con=cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
con=im.grab_contours(con) #this will return a list containing 
output =image.copy()
print(con)
#loop over the contours
for c in con:
    #draw ech contour on the output image with 3px thick purple
    #outline, then display coutours one at a time
    cv.drawContours(output, [c], -1,(240,0,159),3)
                    #image, contour, contour index, color, thickness
    cv.imshow("contours", output)
    cv.waitKey(0)
    

    txt= "i found {} objects!".format(len(con))
    cv.putText(output,txt,(10,25),cv.FONT_HERSHEY_SIMPLEX,0.7,(240,0,159),2)
    cv.imshow("conturs found", output)
    cv.waitKey(0)


