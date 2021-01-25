import cv2
import numpy as np


img = cv2.imread("data/flower.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = img.shape

M1 = np.float32([
    [1, 0, 0],
    [0, -1, rows]
])

M2 = np.float32([
    [-1, 0, cols],
    [0, 1, 0]
])

M3 = np.float32([
    [2, 0, -int(cols/2)],
    [0, 2, -int(rows/2)]
])


dst1 = cv2.warpAffine(img, M1 ,(cols,rows))
dst2 = cv2.warpAffine(img, M2 ,(cols,rows))
dst3 = cv2.warpAffine(img, M3 ,(cols,rows))


cv2.imshow("A", img)
cv2.imshow("1", dst1)
cv2.imshow("2", dst2)
cv2.imshow("3", dst3)

cv2.waitKey(0)

cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/flower_original.png", img)
cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/flower_1.png", dst1)
cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/flower_2.png", dst2)
cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/flower_3.png", dst3)
