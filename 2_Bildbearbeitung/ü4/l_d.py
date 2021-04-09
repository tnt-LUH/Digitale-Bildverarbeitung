import cv2
import numpy as np

img = cv2.imread("../../data/cameraman.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

k1 = (1 / (33 * 33)) * np.ones((33, 33), dtype=np.uint8)

border_types = [
    ("cv2.BORDER_REFLECT", cv2.BORDER_REFLECT, 255),
    ("cv2.BORDER_REPLICATE", cv2.BORDER_REPLICATE, 255),
    ("cv2.BORDER_CONSTANT", cv2.BORDER_CONSTANT, 0),
    ("cv2.BORDER_CONSTANT", cv2.BORDER_CONSTANT, 255),

]

cv2.imshow("img", img)

for name, border, value in border_types:
    img_border = cv2.copyMakeBorder(img, 50, 50, 50, 50, borderType=border, value=value)
    img_k1 = cv2.filter2D(img, -1, k1, borderType=border)
    cv2.imshow("img_k1_" + name + str(value), img_k1)
    cv2.imshow("img_border_" + name + str(value), img_border)

cv2. waitKey()