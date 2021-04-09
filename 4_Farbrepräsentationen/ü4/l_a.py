import cv2
import numpy as np

img = cv2.imread("../../data/model.png")

#white_balancing_factor = np.asarray([[[1, 1, 1]]])
white_balancing_factor = 255 / img[146, 127].astype(np.float32)
white_balancing_factor = np.expand_dims(white_balancing_factor, 0)
white_balancing_factor = np.expand_dims(white_balancing_factor, 1)

img_balanced = img * white_balancing_factor
img_balanced = np.clip(img_balanced, 0, 255)
img_balanced = img_balanced.astype(np.uint8)

cv2.imshow("Normal", img)
cv2.imshow("Abgeglichen", img_balanced)

cv2.waitKey()

