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

rotation = [
    [..., ...],
    [..., ...]
]
translation = [
    ...,
    ...
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

cv2.waitKey(0)

