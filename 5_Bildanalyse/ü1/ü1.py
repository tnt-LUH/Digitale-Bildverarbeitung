import numpy as np
import cv2

KERNEL_SIZE = 20

# Einlesen des Bildes
filepath = "../../data/text_%s.jpg"
images = list()
for i in [1, 2, 3]:
    img = cv2.imread(filepath % i)
    img = cv2.resize(img, (500, 500))
    images.append(img)

