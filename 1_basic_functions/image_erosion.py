
import cv2
import numpy as np

image = cv2.imread('images/lambo.png')

kernel = np.ones((5, 5), np.uint8) #kernel size should be odd and positive

# Threshold

t_lower = 100
t_upper = 120

imgCanny = cv2.Canny(image, t_lower, t_upper)


# Dilation of the image

image_dilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Erosion of the image

image_erosion = cv2.erode(image_dilation, kernel, iterations=1)


# cv2.imshow('Original', image)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilation Image', image_dilation) 
cv2.imshow('Erosion Image', image_erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()