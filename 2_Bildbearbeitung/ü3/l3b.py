import numpy as np
import cv2

''' Einlesen des Bildes '''
img = cv2.imread("data/normal.jpg")
rows, cols, channels = img.shape


''' Transformation t1: Implementierung mit OpenCV  '''

t_1 = np.float32(
    [
        [ np.cos(np.pi / 4), np.sin(np.pi / 4), 0],
        [-np.sin(np.pi / 4), np.cos(np.pi / 4), 0]]
)
dst = cv2.warpAffine(img, t_1, (cols, rows))
cv2.imshow('img',dst)
cv2.waitKey(0)

''' Transformation t2: Implementierung ohne CV2  '''
c1, c2, c3, c4 = np.cos(np.pi / 4), np.sin(np.pi / 4), -np.sin(np.pi / 4), np.cos(np.pi / 4)
c_y, c_x = rows / 2, cols / 2


def new_pos(x, y):
    new_x = round(c1 * (x - c_x) + c2 * (y - c_y) + c_x)
    new_y = round(c3 * (x - c_x) + c4 * (y - c_y) + c_y)
    return new_x, new_y


def old_pos(new_x, new_y):
    x = (new_x/c1) - (c_x / c1) + c_x - c3 * c2 * c_x / (c4 * c1) - (c2 * new_y / (c1 * c4)) + (c_y * c2 / (c1 * c4))
    x = x / (1 - c3*c2/(c4*c1))
    y = c_y + (new_y - (c3 * (x - c_x)) - c_y) / c4
    x = round(x)
    y = round(y)
    return x, y


# Forwardmapping
new_img = np.zeros_like(img)
for x in range(cols):
    for y in range(rows):
        new_x, new_y = new_pos(x, y)
        # Überstpringen, wenn ausserhalb des Bildes
        if not 0 <= new_x < cols or not 0 <= new_y < rows:
            continue
        new_img[new_y, new_x] = img[y, x]
cv2.imshow('img', new_img)
cv2.waitKey(0)

# Backwardmapping
new_img = np.zeros_like(img)
for x in range(cols):
    for y in range(rows):
        old_x, old_y = old_pos(x, y)
        # Überstpringen, wenn ausserhalb des Bildes
        if not 0 <= old_x < cols or not 0 <= old_y < rows:
            continue
        new_img[y, x] = img[old_y, old_x]
cv2.imshow('img', new_img)
cv2.waitKey(0)

''' Transformation t3: Implementierung ohne CV2  '''
c1, c2, c3, c4 = 1, 0.8, 0, 1
c_y, c_x = rows / 2, cols / 2


def new_pos(x, y):
    new_x = round(c1 * (x - c_x) + c2 * (y - c_y) + c_x)
    new_y = round(c3 * (x - c_x) + c4 * (y - c_y) + c_y)
    return new_x, new_y


def old_pos(new_x, new_y):
    x = (new_x/c1) - (c_x / c1) + c_x - c3 * c2 * c_x / (c4 * c1) - (c2 * new_y / (c1 * c4)) + (c_y * c2 / (c1 * c4))
    x = x / (1 - c3*c2/(c4*c1))
    y = c_y + (new_y - (c3 * (x - c_x)) - c_y) / c4
    x = round(x)
    y = round(y)
    return x, y


# Forwardmapping
new_img = np.zeros_like(img)
for x in range(cols):
    for y in range(rows):
        new_x, new_y = new_pos(x, y)
        # Überstpringen, wenn ausserhalb des Bildes
        if not 0 <= new_x < cols or not 0 <= new_y < rows:
            continue
        new_img[new_y, new_x] = img[y, x]
cv2.imshow('img', new_img)
cv2.waitKey(0)

# Backwardmapping
new_img = np.zeros_like(img)
for x in range(cols):
    for y in range(rows):
        old_x, old_y = old_pos(x, y)
        # Überstpringen, wenn ausserhalb des Bildes
        if not 0 <= old_x < cols or not 0 <= old_y < rows:
            continue
        new_img[y, x] = img[old_y, old_x]
cv2.imshow('img', new_img)
cv2.waitKey(0)