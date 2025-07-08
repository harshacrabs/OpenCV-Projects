import cv2

image = cv2.imread('images/lambo.png')

image_blur = cv2.GaussianBlur(image, (37, 37), 0) #kerneal should be odd and positive

cv2.imshow('Original', image)
cv2.imshow('Blurred', image_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()