import numpy as np
import cv2

p_1 = (0, 1)
p_2 = (5, 4)
matrix = np.zeros((6, 6))
matrix[p_1[1], p_1[0]] = 1
matrix[p_2[1], p_2[0]] = 1

# Resize image
matrix = np.repeat(matrix, 50, axis=1)
matrix = np.repeat(matrix, 50, axis=0)

# Add seperators
matrix[0::2, ::50] = 1
matrix[1::2, ::50] = 0
matrix[::50, 0::2] = 1
matrix[::50, 1::2] = 0


def city_block(p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    return np.abs(dx) + np.abs(dy)


def euklidean(p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    return np.sqrt(dx * dx + dy * dy)


def tschebyschew(p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    return np.maximum(np.abs(dx), np.abs(dy))


print("City-Block:", city_block(p_1, p_2))
print("Euklidischer Abstand:", euklidean(p_1, p_2))
print("Schachbrett Distanz (Tschebyschew):", tschebyschew(p_1, p_2))

# Show image
matrix = matrix.astype(np.float64)
cv2.imshow("a", matrix)
cv2.imwrite("data/a.png", matrix * 255)
cv2.waitKey(0)
