import numpy as np
import cv2

line = np.asarray(
    [[1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]],
)
# Resize image
line = np.repeat(line, 50, axis=1)
line = np.repeat(line, 50, axis=0)
# Add seperators
line[0::2, ::50] = 1
line[1::2, ::50] = 0
# Show image
line = line.astype(np.float64)
cv2.imshow("Binaerbaum", line)
cv2.waitKey(0)