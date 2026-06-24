import cv2
import numpy as np

I = np.asarray([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
], dtype=np.uint8)

s = np.asarray([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
], dtype=np.uint8)


# Opening
I_opening = cv2.erode(I, s)
I_opening = cv2.dilate(I_opening, s)

# Closing
I_closing = cv2.dilate(I, s)
I_closing = cv2.erode(I_closing, s)

# Resize image
I = np.repeat(I, 50, axis=1)
I = np.repeat(I, 50, axis=0)
I_opening = np.repeat(I_opening, 50, axis=1)
I_opening = np.repeat(I_opening, 50, axis=0)
I_closing = np.repeat(I_closing, 50, axis=1)
I_closing = np.repeat(I_closing, 50, axis=0)

cv2.imshow("Original", I * 255)
cv2.imshow("Opening", I_opening * 255)
cv2.imshow("Closing", I_closing * 255)

cv2.waitKey(0)

