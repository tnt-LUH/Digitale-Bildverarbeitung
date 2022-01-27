import numpy as np
import cv2

''' Load images '''
img1 = cv2.imread("data/mensch.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("data/mensch2.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("data/kasten.png", cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread("data/kasten2.png", cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread("data/ball.png", cv2.IMREAD_GRAYSCALE)
img6 = cv2.imread("data/ball2.png", cv2.IMREAD_GRAYSCALE)

''' Define features '''


def height_and_width(img):
    rows, cols = np.where(img != 0)
    x1, x2, y1, y2 = np.min(cols), np.max(cols), np.min(rows), np.max(rows)
    h = y2 - y1
    w = x2 - x1
    return h, w


def height_over_width(w, h):
    return h / w


def perimeter(img):
    kernel = np.asarray([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
    small_img = cv2.erode(img, kernel)
    edges = img - small_img
    peri = np.sum(edges / np.max(edges))
    return peri


def area(img):
    return np.sum(img / np.max(img))


def roundness(perimeter, area, h, w):
    # (2 pi r) / (pi r^2) = perimeter / area = 2 / r           for round objects
    # r = h / 2 = w / 2
    r = 0.5 * (h / 2 + w / 2)
    round = r * perimeter / (2 * area)
    return round


''' Show parameter '''
for name, img in [("img1", img1), ("img2", img2), ("img3", img3), ("img4", img4), ("img5", img5), ("img6", img6)]:
    print("Image:", name)
    object_height, object_width = height_and_width(img)
    print("    h =", object_height)
    print("    w =", object_width)
    object_height_over_width = height_over_width(object_width, object_height)
    print("    height_over_width =", object_height_over_width)
    object_perimeter = perimeter(img)
    print("    perimeter =", object_perimeter)
    object_area = area(img)
    print("    area =", object_area)
    object_roundness = roundness(object_perimeter, object_area, object_height, object_width)
    print("    roundness =", object_roundness)