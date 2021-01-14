import cv2
import numpy as np
from matplotlib import pyplot as plt


a = [
    [220, 0, 150, 3, 100, 0],
    [0, 250, 3, 160, 0, 100],
    [150, 0, 203, 0, 165, 5],
    [2, 145, 5, 205, 0, 150],
    [99, 0, 150,  0, 255, 2],
    [1, 105, 0, 160, 0, 250],
]

b = [
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0],
]


a = np.array(a, dtype=np.uint8)
a = cv2.resize(a, (200,200), interpolation=cv2.INTER_NEAREST)
b = np.array(b, dtype=np.uint8)
b = 255 * b
b = cv2.resize(b, (200,200), interpolation=cv2.INTER_NEAREST)

cv2.imshow("A", b)
cv2.waitKey(0)

cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/filter_chess.png", a)
cv2.imwrite("/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/filter_chess_final.png", b)