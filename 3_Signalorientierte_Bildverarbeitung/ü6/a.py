import cv2
import numpy as np

normal = cv2.imread("../../data/lena.png", cv2.IMREAD_GRAYSCALE)


def valid_rows(N):
    n = np.log2(N)
    n = np.ceil(n)
    N = np.power(2, n)
    return N


def create_H(m, N):
    ...

''' Reshape to valid resolution '''
N, m = normal.shape
new_N = valid_rows(N)
print("Original Resolution:", m, "x", N)
print("New Resolution:", m, "x", new_N)
if N != new_N:
    _ = np.zeros((new_N, m))
    _[:N, :m] = normal
    normal = _




''' Show images '''
cv2.imshow("normal", normal)

cv2.waitKey()
