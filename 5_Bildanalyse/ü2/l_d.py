import cv2
import numpy as np

I = np.asarray([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
], dtype=np.uint8)

s = np.asarray([
    [0, 1, 0],
    [0, 1, 1],
    [0, 0, 0],
], dtype=np.uint8)

I_new = cv2.erode(I, s)
I_new = cv2.dilate(I_new, s)

# Resize image
I = np.repeat(I, 50, axis=1)
I = np.repeat(I, 50, axis=0)
I_new = np.repeat(I_new, 50, axis=1)
I_new = np.repeat(I_new, 50, axis=0)

cv2.imshow("Original", I * 255)
cv2.imshow("Opening", I_new * 255)
cv2.waitKey(0)
