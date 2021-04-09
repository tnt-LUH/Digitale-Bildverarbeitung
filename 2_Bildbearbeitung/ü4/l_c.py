import cv2
import numpy as np

img = cv2.imread("../../data/cameraman.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

k1 = (1 / 25) * np.asarray([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
], dtype=np.uint8)

k2 = np.asarray([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1],
], dtype=np.float32)

k3 = np.asarray([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1],
], dtype=np.float32)

img_k1 = cv2.filter2D(img, -1, k1)
img_k2 = cv2.filter2D(img.astype(np.float32), -1, k2)
img_k2 = np.maximum(img_k2, 0).astype(np.uint8)
img_k3 = cv2.filter2D(img.astype(np.float32), -1, k3)
img_k3 = np.maximum(img_k3, 0).astype(np.uint8)

cv2.imshow("img", img)
cv2.imshow("img_k1", img_k1)
cv2.imshow("img_k2", img_k2)
cv2.imshow("img_k3", img_k3)
cv2. waitKey()