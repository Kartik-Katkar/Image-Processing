import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./Pika.jpg',0)
cv.imshow("orignal image",img)
cv.waitKey()

print(img.shape)
print(img.size)
print(type(img))

edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


# noise reduction Gaussian filter blurs image but not that much 
# Finding Intensity Gradient of the Image 
# Non-maximum Suppression 
# Hysteresis Thresholding 