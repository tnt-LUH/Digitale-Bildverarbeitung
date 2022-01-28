import numpy as np
import cv2


''' Load image and apply histogramm equalization '''
img = cv2.imread("data/students_checklist.jpg").astype(np.float32)
img[:, :, 0] = 255 * (img[:, :, 0] - np.min(img[:, :, 0])) / (np.max(img[:, :, 0]) - np.min(img[:, :, 0]))
img[:, :, 1] = 255 * (img[:, :, 1] - np.min(img[:, :, 1])) / (np.max(img[:, :, 1]) - np.min(img[:, :, 1]))
img[:, :, 2] = 255 * (img[:, :, 2] - np.min(img[:, :, 2])) / (np.max(img[:, :, 2]) - np.min(img[:, :, 2]))
cv2.imshow("img", img.astype(np.uint8))

''' Binary segmentation '''
mask = (img[:, :, 0] > 100) * (img[:, :, 1] > 100) * (img[:, :, 2] > 100) *\
       (img[:, :, 2] - img[:, :, 1] < 20) * (img[:, :, 2] - img[:, :, 0] < 20)
mask = 1 - mask

''' Morphologigcal operations '''
kernel = np.ones((3, 3))
mask = cv2.erode(mask.astype(np.uint8) * 255, kernel, iterations=15)
mask = cv2.dilate(mask, kernel, iterations=15)

cv2.imshow("mask", mask)

''' Finding seed point '''
seeds = cv2.erode(mask, kernel, iterations=70)
cv2.imshow("seeds", seeds)

''' Labeling seeds '''
label_map = np.zeros_like(seeds)
next_id = 1
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if seeds[i, j] != 0:
            upper_label = label_map[i - 1, j] if i > 0 else 0
            left_label = label_map[i, j - 1] if j > 0 else 0
            if upper_label == 0 and left_label == 0:
                label_map[i, j] = next_id
                next_id += 1
            elif upper_label == 0 and left_label != 0:
                label_map[i, j] = left_label
            elif upper_label != 0 and left_label == 0:
                label_map[i, j] = upper_label
            elif upper_label != 0 and left_label != 0:
                if upper_label == left_label:
                    label_map[i, j] = upper_label
                else:
                    new_label = min(upper_label, left_label)
                    old_label = max(upper_label, left_label)
                    label_map[label_map == old_label] = new_label
                    label_map[i, j] = new_label
labels = sorted(np.unique(label_map))
next_id = 1
for l in labels:
    if l == 0:
        continue
    label_map[label_map == l] = next_id
    next_id += 1

''' Create distance labels for all labels '''
mask = mask != 0

while np.sum(mask > 0):
    for l in np.unique(label_map):
        if l == 0:
            continue
        kernel = np.ones((3, 3))
        current_label = label_map == l
        current_label = cv2.dilate(current_label.astype(np.uint8), kernel, iterations=1)
        current_label = current_label * mask
        mask[current_label != 0] = 0
        label_map[current_label != 0] = l


''' Visualize label map '''
color_map = {
    1: [255, 0, 0],
    2: [255, 255, 0],
    3: [255, 255, 255],
    4: [0, 255, 0],
    5: [0, 255, 255],
    6: [0, 0, 255],
    7: [100, 100, 100],
    8: [50, 200, 80],
    9: [200, 140, 88],
    10: [120, 0, 190],
}
colored_image = np.zeros((img.shape[0], img.shape[1], 3))
for c, value in color_map.items():
    colored_image[label_map == c] = value
cv2.imshow("colored_image", colored_image.astype(np.uint8))
cv2.waitKey(0)
