import numpy as np
import cv2


''' Load image '''
img = cv2.imread("data/bild.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", img)

cv2.waitKey(0)