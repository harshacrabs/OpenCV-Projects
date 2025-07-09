import cv2
import numpy as np

img = cv2.imread('images/shapes.png')

# Step-1: Convert to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Step-2 : Canny Edge Detection

lower_threshold = 100
upper_threshold = 200

canny_img = cv2.Canny(gray_img, lower_threshold, upper_threshold)

# Step-3: Find Contours
contours, hierarchy = cv2.findContours(canny_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step-4: Find length of contours

print(f'Number of contours: {len(contours)}')

# Step-5: Draw Contours

img_copy = img.copy()

cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 3)


cv2.imshow('Original Image', img)
cv2.imshow('Gray Image', gray_img)
cv2.imshow('Edge Detector', canny_img)
cv2.imshow('Contours', img_copy)






cv2.waitKey(0)
cv2.destroyAllWindows()