import cv2
import numpy as np

img = cv2.imread("../../data/car.png")
img = cv2.resize(img, (500, 500))
cv2.imshow("Car", img)

print("Image Shape:", img.shape)


def T(pos, rotation, translation):
    """ Transformation Matrix """
    new_pos = np.matmul(rotation, pos) + translation

    return new_pos


new_image = np.zeros_like(img)

alpha = -0.5 * np.pi
rotation = [
    [np.cos(alpha), -np.sin(alpha)],
    [np.sin(alpha), np.cos(alpha)]
]
translation = [
    [0],
    [img.shape[1]]
]


for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        old_pos = np.asarray([[x], [y]])
        new_pos = T(old_pos, rotation, translation)
        new_pos = new_pos.astype(int)
        if 0 <= new_pos[0] < img.shape[1] and 0 <= new_pos[1] < img.shape[0]:
            new_image[new_pos[1], new_pos[0]] = img[y, x]

print(new_image.shape)
cv2.imshow("After Transformation", new_image)

""" 
Naive Solution
 
1. Rotate the image with 90°  -> alpha=90°
2. Translate in y axis with image length -> [ [0], [height] ] 
 
"""

"""
Mathematical solution

1. Find correspondences

x,y      -->   x',y'

0,0      -->   0,1
1,0      -->   0,0
0,1      -->   1,1
1,1      -->   1,0
0.5,0.5  -->   0.5,0.5


2. Solve system:
[a, b] * [x, y]^T  + [e, f]^T = [x', y']^T
[c, d]

ax + by + e = x'
cx + dy + f = y'


Translation (0,0 --> 0,1):
0 + 0 + e = 0   -->  e = 0
0 + 0 + f = 1   -->  f = 1

Rotation (1,0   --> 0,0):
a + 0 + 0 = 0   -->  a = 0
c + 0 + 1 = 0   -->  c = -1

Rotation (0,1 --> 1,1):
0 + b + 0 = 1  -->  b = 1
0 + d + 1 = 1  -->  d = 0

"""


cv2.waitKey(0)

