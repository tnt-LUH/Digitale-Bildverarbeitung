import cv2
import numpy as np

img = cv2.imread("../../data/lena.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

''' Rauschen hinzufügen '''
h, w = img.shape
saltpepper_noise = np.zeros((h, w), dtype=np.uint8)
saltpepper_noise = cv2.randu(saltpepper_noise, 0, 255)
black = saltpepper_noise < 15
white = saltpepper_noise > 240
img[white] = 255
img[black] = 0

cv2.imshow("img", img)

''' Median Filter anwenden '''
sizes = [3, 5, 9]
for kernel_size in sizes:
    img_filtered = cv2.medianBlur(img, kernel_size)
    cv2.imshow("img_filtered_" + str(kernel_size), img_filtered)

cv2. waitKey()
