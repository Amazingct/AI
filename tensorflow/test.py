import cv2

pic = cv2.imread("/home/amazing/Desktop/PYTHON/AI/tensorflow/boy_girl/boy/IMG-20190826-WA0022.jpeg", -1)
pic = cv2.resize(pic, (200, 200))
cv2.imshow("picture", pic)
cv2.waitKey(2000)
cv2.imwrite("/home/amazing/Desktop/dan.png", pic)
cv2.destroyAllWindows()