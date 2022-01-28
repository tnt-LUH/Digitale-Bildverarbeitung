import numpy as np
import cv2


''' Load image '''
img = cv2.imread("data/bild.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", img)

''' Iterate over rows / colums'''
label_map = np.zeros_like(img)
next_id = 1
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] != 0:
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

''' Rename labels (not necessary, but for visualisation) '''
labels = sorted(np.unique(label_map))
next_id = 1
for l in labels:
    if l == 0:
        continue
    label_map[label_map == l] = next_id
    next_id += 1



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