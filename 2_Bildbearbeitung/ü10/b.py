import cv2
import numpy as np

img = cv2.imread("../../data/car.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (500, 500))
# Do some preprocessing
img = img.astype(float)
img = 50 + (105 * img / 255)
cv2.imshow("Original", img.astype(np.uint8))

# Implement AHE


cv2.waitKey(0)

