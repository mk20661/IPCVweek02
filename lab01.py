import cv2
import numpy as np



image = cv2.imread("mandrill.jpg")

kernel = np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]])

kernel_height = kernel.shape[0]
image_height = image.shape[0]
kernel_width = kernel.shape[1]
image_width =  image.shape[1]

outimage = np.zeros((image_height,image_width),dtype=np.uint8)


for i in range(image_height - kernel_height + 1):
    for j in range(image_width - kernel_width + 1):
       outimage[i, j] = 1/9 * np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)

cv2.imshow("processed image",outimage)

cv2.waitKey(0)
cv2.destroyAllWindows()