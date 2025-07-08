import cv2
import numpy as np

# img = cv2.imread('images/cards.jpg')

img = cv2.imread('images/cards2.jpg')
width, height = 500, 500

# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) # (x, y)
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # (x, y)

cv2.imshow('Original Image', img)

pts1 = np.float32([[702,150],[1129,417],[286,694],[720,996]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])


matrix = cv2.getPerspectiveTransform(pts1, pts2) # (source points, destination points)

img_output = cv2.warpPerspective(img, matrix, (width, height)) # (image, matrix, (width, height))

cv2.imshow('Output Image', img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()