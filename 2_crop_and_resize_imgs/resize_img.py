import cv2

img = cv2.imread('images/image.jpg')

print('Original image shape:', img.shape)

resized_img = cv2.resize(img, (1000, 650)) # (width, height)

print('Resized image shape:', resized_img.shape)

cv2.imshow('Original image', img)
cv2.imshow('Resized image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()