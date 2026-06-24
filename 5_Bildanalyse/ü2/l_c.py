import cv2
import numpy as np

I = np.asarray([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
], dtype=np.uint8)

s = np.asarray([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
], dtype=np.uint8)


# Opening
I_erosion = cv2.erode(I, s)

# Closing
# Resize image
I = np.repeat(I, 50, axis=1)
I = np.repeat(I, 50, axis=0)
I_erosion = np.repeat(I_erosion, 50, axis=1)
I_erosion = np.repeat(I_erosion, 50, axis=0)


cv2.imshow("Original", I * 255)
cv2.imshow("Erosion", I_erosion * 255)

cv2.waitKey(0)

