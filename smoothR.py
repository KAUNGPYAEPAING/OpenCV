import cv2
import numpy as np

img = cv2.imread('lena.png')

kernel = np.ones((5, 5), np.float32) / 25
img[:, :, 0] = cv2.filter2D(img[:, :, 0], -1, kernel)

cv2.imwrite('lena_smoothed.jpg', img)


cv2.imshow('Smooth Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
