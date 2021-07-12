import numpy as np
import cv2

line = np.asarray(
    [
        [0,0,  0,0,  0,0,  0,0],
        [1,1,  1,0,  1,1,  1,0],
        [1,0,  0,1,  1,0,  0,1],
        [1,0,  0,0,  0,0,  1,1],
        [0,1,  0,1,  1,1,  1,0],
        [0,1,  1,0,  0,1,  0,0],
        [0,1,  1,0,  0,0,  0,0],
        [0,0,  0,0,  0,0,  0,0],
    ],
)

# Resize image
line = np.repeat(line, 50, axis=1)
line = np.repeat(line, 50, axis=0)

# Add seperators
line[0::2, ::50] = 1
line[1::2, ::50] = 0
line[::50, 0::2] = 1
line[::50, 1::2] = 0

# Show image
line = line.astype(np.float64)
cv2.imshow("1", line)
cv2.imwrite("./data/1.png", line*255)
cv2.waitKey(0)

chaincode = [0, 0, 7, 0, 2, 0, 0, 7, 6, 4, 6, 4, 6, 3, 4, 5, 6, 4, 2, 2, 3, 2]
print(chaincode)