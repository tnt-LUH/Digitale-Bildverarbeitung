import cv2
import numpy as np

normal = cv2.imread("../../data/lena.png", cv2.IMREAD_GRAYSCALE)


def valid_rows(N):
    n = np.log2(N)
    n = np.ceil(n)
    N = np.power(2, n)
    return N


def create_H(m, N):
    """
    m: Columns
    n: Rows
    """
    H = np.zeros((int(N), int(m)))
    for i in range(1, int(N) + 1):
        for j in range(1, int(m) + 1):
            if i <= (N/2):
                if j == (2*i -1) or j == 2*i:
                    H[i-1,j-1] = 1 / np.sqrt(2)
            else:
                #print(j, i)
                if j == (2 * (i - N/2) - 1):
                    H[i-1,j-1] = 1 / np.sqrt(2)
                elif j == (2 * (i - N/2)):
                    H[i-1,j-1] = -1 / np.sqrt(2)
    return H

''' Reshape to valid resolution '''
N, m = normal.shape
new_N = valid_rows(N)
print("Original Resolution:", m, "x", N)
print("New Resolution:", m, "x", new_N)
if N != new_N:
    _ = np.zeros((new_N, m))
    _[:N, :m] = normal
    normal = _

''' Get Haar-Matrix '''
H = create_H(m, new_N)
print(H[0:5, 0:5])
print(H[256:261, 0:5])

''' Filter with HxI'''
haar = np.matmul(H, normal)

''' Invert Filter '''
haar_inv = np.matmul(np.transpose(H), haar)

''' Show images '''
cv2.imshow("normal", normal)
cv2.imshow("haar", haar / 255)
cv2.imshow("haar_inv", haar_inv / 255)
print("Difference:", np.sum(np.abs(normal-haar_inv)))

cv2.waitKey()
