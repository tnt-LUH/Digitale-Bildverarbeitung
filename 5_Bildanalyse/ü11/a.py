import numpy as np
import cv2


''' Load images '''
img1 = cv2.imread("data/mensch.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("data/mensch2.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("data/kasten.png", cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread("data/kasten2.png", cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread("data/ball.png", cv2.IMREAD_GRAYSCALE)
img6 = cv2.imread("data/ball2.png", cv2.IMREAD_GRAYSCALE)

''' Define features '''


''' Show parameter '''
for name, img in [("img1", img1), ("img2", img2), ("img3", img3), ("img4", img4), ("img5", img5), ("img6", img6)]:
    print("Image:", name)
    print("    feature =", ...)

