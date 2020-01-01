from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--folder", required=True,
	help="path to input directory of faces + images")
args = vars(ap.parse_args())
# python encode_faces.py --folder
# grab the paths to the input images in our dataset

imagePaths = list(paths.list_images(args["folder"]))
print (imagePaths)

# for (i, imagePath) in enumerate(imagePaths):
# extract the person name from the image path
name = imagePaths[2].split(os.path.sep)[-2]
print (name)
image = cv2.imread(imagePaths[2]) #get the image
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convert to rgb
boxes = face_recognition.face_locations(rgb,)
encodings = face_recognition.face_encodings(rgb, boxes)
print(encodings)
print(encodings[0])
