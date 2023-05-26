import cv2

img1 = cv2.imread("Pika.jpg")

bgrgray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
bgrhsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
brightlab = cv2.cvtColor(img1,cv2.COLOR_BGR2LAB)

cv2.imshow("Bgr to Gray",bgrgray)
cv2.imshow("Bgr to HSV",bgrhsv)
cv2.imshow("Bgr to lab",brightlab)

# cmyk in printers for cheapness cyan magenta pink Half toning used 
# hsv is hue (color) saturation (amt of gray) value (brightness or intensity)
# lab for l = lightness a = green to magenta b = blue to yellow 
# Drawback of RGB is no intensity like bright or dark 

cv2.waitKey(0)
cv2.destroyAllWindows()