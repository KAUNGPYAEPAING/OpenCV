import cv2 
import random

img = cv2.imread('assets/sky.jpg', -1)

print(img[256][44])


#modifying image manually 
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for i in range(100): #first row
#     for j in range(img.shape[1]): #shape will give row,column,channel. 1 mean width. Loop through the whole image width



# print(img.shape)  #height width channel
# print(img)

#Standart color representation is Red Green and Blue (RGB)
#Open Cv Blue green and red (BGR)

#exampel 3-dim
# [
#     [0 0 0],[255 255 255], [0 0 0]
#     [],
#     []
# ]



# blue green red
# [0 0 0] [amount_of_blue_in_pixel amount_of_green_in_pixel amount_of_red_in_pixel] 
# * value always have 0-255 < 0 = none, 255 = all
#[228 0 0] slightly lighter blue