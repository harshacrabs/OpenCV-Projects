import cv2

image = cv2.imread('images/lambo.png')

#setting the threshold

	# Lower both thresholds → more edges (and noise)
	# Increase both thresholds → fewer, stronger edges
t_lower = 100 
t_upper = 120

# Apply Canny Edge Detection

edge = cv2.Canny(image, t_lower, t_upper)

cv2.imshow('Original', image)
cv2.imshow('Canny Edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()