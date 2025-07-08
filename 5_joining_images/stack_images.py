# Note: All images should have the same size and same number of channels to be stacked horizontally or vertically

import cv2
import numpy as np

img_1 = cv2.imread('images/cards.jpg')

print('Image 1 shape:', img_1.shape)

img_1_resized = cv2.resize(img_1, (500, 500))   # (width, height)

img_2 = cv2.imread('images/image2.jpg')

print('Image 2 shape:', img_2.shape)

img_2_resized = cv2.resize(img_2, (500, 500)) # (width, height)

img_horizontal_stack = np.hstack((img_1_resized, img_2_resized)) # (image1, image2)

cv2.imshow('Horizontal Stacked Images', img_horizontal_stack) # (window_name, image)    

img_vertical_stack = np.vstack((img_1_resized, img_2_resized)) # (image1, image2)

cv2.imshow('Vertical Stacked Images', img_vertical_stack) # (window_name, image)


cv2.waitKey(0)
cv2.destroyAllWindows()