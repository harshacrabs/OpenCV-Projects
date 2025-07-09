import cv2
import numpy as np

img = cv2.imread('images/lambo.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = (0,13,75)
upper_range = (18,255,255)

mask = cv2.inRange(hsv_img, lower_range, upper_range)

color_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Color Detected', color_img)

cv2.waitKey(0)
cv2.destroyAllWindows()