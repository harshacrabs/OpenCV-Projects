import cv2
import numpy as np


# Create a gray image
image = np.zeros((512, 512))


# Create a color image
image = np.zeros((512, 512, 3))

# Add color to the image
image[:] = 255,0,0

# Draw a line on the image
cv2.line(image, (0, 0), (image.shape[1] ,image.shape[0]), (0, 255, 0), 3) # (start, end, color, thickness)

# Draw a rectangle on the image
cv2.rectangle(image, (0, 0), (400, 250), (0, 255, 255), 3) # (start, end, color, thickness)

# Draw a circle on the image
cv2.circle(image, (256, 256), 50, (255, 255, 255), cv2.FILLED) # (center, radius, color, thickness)
 
# Add text to the image
cv2.putText(image, 'Hello, World!', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) # (text, position, font, fontScale, color, thickness)


cv2.imshow('Output Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()