import numpy as np
import cv2

obj1 = np.asarray([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
])

obj2 = np.asarray([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
])


intersection = obj1 * obj2


# Visualize images

# Resize image
obj1 = np.repeat(obj1, 50, axis=1)
obj1 = np.repeat(obj1, 50, axis=0)
obj2 = np.repeat(obj2, 50, axis=1)
obj2 = np.repeat(obj2, 50, axis=0)
intersection = np.repeat(intersection, 50, axis=1)
intersection = np.repeat(intersection, 50, axis=0)

# Add seperators
obj1[0::2, ::50] = 1
obj1[1::2, ::50] = 0
obj1[::50, 0::2] = 1
obj1[::50, 1::2] = 0
obj2[0::2, ::50] = 1
obj2[1::2, ::50] = 0
obj2[::50, 0::2] = 1
obj2[::50, 1::2] = 0
intersection[0::2, ::50] = 1
intersection[1::2, ::50] = 0
intersection[::50, 0::2] = 1
intersection[::50, 1::2] = 0

# Show image
obj1 = obj1.astype(np.float64)
obj2 = obj2.astype(np.float64)
intersection = intersection.astype(np.float64)

cv2.imshow("obj1", obj1)
cv2.imshow("obj2", obj2)
cv2.imshow("intersection", intersection)

cv2.waitKey(0)
