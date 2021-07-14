import cv2
import numpy as np

img = cv2.imread("../../data/car.png")
cv2.imshow("Car", img)

print("Image Shape:", img.shape)

print("\nForward-Mapping")

print("\nBackward-Mapping")

cv2.waitKey(0)