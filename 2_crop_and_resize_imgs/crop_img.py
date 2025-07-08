import cv2

image = cv2.imread('images/lambo.png')

print('Original image shape:', image.shape)


img_cropped = image[0:200, 200:500] # (height, width)

print('Cropped image shape:', img_cropped.shape)

cv2.imshow('Original image', image)
cv2.imshow('Cropped image', img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()