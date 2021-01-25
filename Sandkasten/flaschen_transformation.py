import cv2
import numpy as np
import math


img = cv2.imread("data/flasche.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x, y = 300, 270
img = img[y:y+900, x:x+900]
img = cv2.resize(img, (300, 300))
rows, cols = img.shape
print(rows, cols)
alpha = np.pi / 4
M1 = np.float32([
    [np.cos(alpha), -np.sin(alpha), 150],
    [np.sin(alpha), np.cos(alpha), 0]
])


dst1 = cv2.warpAffine(img, M1 ,(cols,rows))


cv2.imshow("A", img)
cv2.imshow("1", dst1)

cv2.waitKey(0)

#cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/flasche_original.png", img)
#cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/flasche_rotated.png", dst1)
