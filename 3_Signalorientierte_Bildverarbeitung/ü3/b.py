import cv2
import numpy as np

car = cv2.imread("../../data/car.png", cv2.IMREAD_GRAYSCALE)
dog = cv2.imread("../../data/dog.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("car", car)
cv2.imshow("dog", dog)

cv2. waitKey()
