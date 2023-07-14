import cv2 
import random

img = cv2.imread('assets/sky.jpg', -1)
print(img.shape)

tag = img[900:1100, 500:700] #copy from 500 to 700 rows then #copy from 600 to 900 columns
img[100:300, 300:500] = tag #past the image in this section

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

