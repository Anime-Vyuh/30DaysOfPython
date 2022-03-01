import cv2
import os

path = os.path.join("Pictures","Anime","aot_cast.jpg")

img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#find threshold: to convert gray image into binary image
#there are two ways: Sime Threshold and Adaptive Threshold
#we shall use adaptive threshold
manga = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,9)

#filter the color of main image and applying masking technique using the threshold value
color = cv2.bilateralFilter(img,9,250,250)
comic = cv2.bitwise_and(color,color,mask=manga)

cv2.imshow('Anime',img)
cv2.imshow("Manga",manga)
cv2.imshow("Comic",comic)

cv2.waitKey(0)
cv2.destroyAllWindows()