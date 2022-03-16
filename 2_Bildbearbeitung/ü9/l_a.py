import cv2
import numpy as np

img = cv2.imread("../../data/car.png")
img = cv2.resize(img, (500, 500))
cv2.imshow("Original", img)


def gamma_correction(img, gamma):
    img = img.astype(np.float)
    img = 255 * np.power(img, gamma) / np.power(255, gamma)
    print(np.max(img))
    img = img.astype(np.uint8)
    return img


for gamma in [0.5, 1, 2]:
    cv2.imshow("%s" % gamma, gamma_correction(img, gamma))

cv2.waitKey(0)

