import cv2
import numpy as np

img = cv2.imread("../../data/car.png")
img = cv2.resize(img, (500, 500))
cv2.imshow("Original", img)


cv2.waitKey(0)


