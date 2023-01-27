# Just shifting the image a little bit down

# import numpy as np
# import cv2 as cv
# img = cv.imread('./shapes.png', 0)
# rows, cols = img.shape
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv.warpAffine(img, M, (cols, rows))
# cv.imshow('img', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# In the first argument, we passed the image, in the second argument it takes a matrix as a parameter in the matrix we 
# give x = 100, which means we are telling the function to shift the image 70 units on the right side and y= 50, which 
# means we are telling the function to shift the image 50 units downwards.  In the third argument, where we mentioned 
# the cols and rows, we told the function to do not to crop the image from both the x and y sides.


# Reflection of an image or flipping

# import numpy as np
# import cv2 as cv
# img = cv.imread('./meme.jpeg', 0)
# rows, cols = img.shape
# M = np.float32([[1, 0, 0],
# 				[0, -1, rows],
# 				[0, 0, 1]])

# To flip horizontally 
# M = np.float32([[1, 0, 0], [0, -1, rows],[0,  0, 1]])

# vertically 
# M = np.float32([[-1, 0, cols], [0, 1, 0], [0, 0, 1]])


# reflected_img = cv.warpPerspective(img, M,
# 								(int(cols),
# 									int(rows)))
# cv.imshow('img', reflected_img)
# cv.imwrite('reflection_out.jpg', reflected_img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# Shrinking and enlarging the image 

import numpy as np
import cv2 as cv
img = cv.imread('./meme.jpeg', 0)
rows, cols = img.shape
img_shrinked = cv.resize(img, (250, 200),
						interpolation=cv.INTER_AREA)
img_enlarged = cv.resize(img_shrinked, None,
						fx=1.5, fy=1.5,
						interpolation=cv.INTER_CUBIC)
cv.imshow('img1', img_shrinked)
cv.imshow('img2', img_enlarged)

cv.waitKey(0)
cv.destroyAllWindows()
