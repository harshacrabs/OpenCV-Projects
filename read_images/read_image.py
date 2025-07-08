# Import necessary libraries

import cv2

# read images

image = cv2.imread('images/image.jpg')

# Display the output Image

if image is None:
    print("Image not found or unable to load.")
else:
    cv2.imshow('Output Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()