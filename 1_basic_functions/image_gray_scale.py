import cv2

image  = cv2.imread('images/image.jpg')

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imgOriginal = cv2.imread('images/image.jpg')

# if imgGray is None or imgOriginal is None:
#     print('Error: Could not read the image')
# else:
cv2.imshow('Gray Scale', imgGray)
cv2.imshow('Original', imgOriginal)
cv2.waitKey(0)
cv2.destroyAllWindows()

