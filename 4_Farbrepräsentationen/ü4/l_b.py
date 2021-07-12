import cv2
import numpy as np

white_balancing_factor = np.asarray([[[0.5, 0.3, 0.95]]])

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img_balanced = img * white_balancing_factor
    img_balanced = np.clip(img_balanced, 0, 255)
    img_balanced = img_balanced.astype(np.uint8)
    cv2.imshow("Normal", img)
    cv2.imshow("Abgeglichen", img_balanced)
    cv2.waitKey(1)

