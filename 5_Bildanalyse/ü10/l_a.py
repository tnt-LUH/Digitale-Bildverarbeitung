import numpy as np
import cv2

# Load images and template
original_img = cv2.imread("../../data/flasche_rechteckig.png")
original_img = cv2.resize(original_img, (int(original_img.shape[1]/ 2), int(original_img.shape[0] / 2)))
cv2.imshow("original_img", original_img)

# The original canny edge code wascode was:
# img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(img, 10, 100)

edges = cv2.imread("data/edges.png")[:, :, 0] / 255
cv2.imshow("canny-edges", edges.astype(np.float32) * 255)
template = cv2.imread("data/template.png")[:, :, 0] / 255
cv2.imshow("template", template.astype(np.float32) * 255)

# Sliding window over the edge image
h_edge, w_edge = edges.shape
h_template, w_template = template.shape
offset_h, offset_w = int(h_template / 2), int(w_template / 2)
print("Shape of edge image:", edges.shape)
print("Shape of template:", template.shape)
print("Offset of template:", offset_h, offset_w)

heatmap = np.zeros_like(edges).astype(np.float32)
for x in range(0, w_edge - w_template):
    for y in range(0, h_edge - h_template):
        overlapping_pixel = edges[y:y+h_template, x:x+w_template] * template
        num_overlapping_pixel = np.sum(overlapping_pixel)
        heatmap[y + offset_h, x + offset_w] = num_overlapping_pixel

heatmap = heatmap / np.max(heatmap)
cv2.imshow("heatmap", heatmap)

# Find maximum and print it so the original image
max_pos = np.unravel_index(heatmap.argmax(), heatmap.shape)
print("The maximal position is:", max_pos)
red = [0, 0, 255]
original_img[max_pos[0]-5:max_pos[0]+5, max_pos[1]-5:max_pos[1]+5] = red
cv2.imshow("best_match", original_img)


cv2.waitKey(0)
