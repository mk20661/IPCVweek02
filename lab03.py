import numpy as np
import cv2

image = cv2.imread("car2.png")

kernel_size = 7
outImage = cv2.medianBlur(image,kernel_size)

cv2.imshow("processed image",outImage)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("fixed image_lab03",outImage)