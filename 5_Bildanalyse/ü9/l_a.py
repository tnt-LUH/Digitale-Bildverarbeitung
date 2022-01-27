import numpy as np
import cv2

# Load image
original_img = cv2.imread("../../data/headphones.jpg")
original_img = cv2.resize(original_img, (int(original_img.shape[1]/ 2), int(original_img.shape[0] / 2)))

img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("original_img", original_img)

# Binary image
threshold = 80
binary_mask = np.copy(img)
binary_mask[img < threshold] = 1
binary_mask[img >= threshold] = 0
cv2.imshow("binary_mask", binary_mask.astype(np.float32))

# Morphing
kernel = np.ones((9, 9))
eroded_mask = cv2.erode(binary_mask, kernel, iterations=1)
cv2.imshow("eroded_mask", eroded_mask.astype(np.float32))

# Subtraction
edges = binary_mask - eroded_mask
cv2.imshow("edges", edges.astype(np.float32))

# Modify original image
original_img[:, :, 2] = np.maximum(original_img[:, :, 2], edges * 255)
cv2.imshow("modified_image", original_img)

cv2.waitKey(0)
