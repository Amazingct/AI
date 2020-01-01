import cv2
import numpy as np

img1 = np.zeros((5,5),np.uint8)
print(img1)


cv2.imshow('image1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()