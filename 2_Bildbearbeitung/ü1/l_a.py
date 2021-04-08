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


def balance(img):
    kernel = np.ones((KERNEL_SIZE, KERNEL_SIZE)) / (KERNEL_SIZE * KERNEL_SIZE)
    blurred = cv2.filter2D(img, -1, kernel=kernel)
    img = img / blurred
    img = 255 * (img - np.min(img)) / (np.max(img) - np.min(img))  # Normieren auf Wertebereich {0, ..., 255}
    img = img.astype(np.uint8)
    print(np.max(img), np.min(img))
    return img


balanced_images = list()
for img in images:
    balanced_image = balance(img)
    balanced_images.append(balanced_image)

for i, (image, balaced_image) in enumerate(zip(images, balanced_images)):
    cv2.imshow("Text%s" % (i + 1), image)
    cv2.imshow("AusgeglichenerText%s" % (i + 1), balaced_image)

cv2.waitKey(0)
