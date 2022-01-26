import numpy as np
import cv2
from matplotlib import pyplot as plt


def n1(hist, s):
    return np.sum(hist[0:s+1])


def n2(hist, s):
    return np.sum(hist[s+1:256])


def mean(hist):
    k = np.arange(0, 256)
    return np.sum((hist * k)) / np.sum(hist)


def mu1(hist, s, n):
    k = np.arange(0, 256)
    return (1 / n) * np.sum((hist * k)[0:s+1])


def mu2(hist, s, n):
    k = np.arange(0, 256)
    return (1 / n) * np.sum((hist * k)[s+1:256])


def sigma1(hist, s, n, mu):
    k = np.arange(0, 256)
    return np.sqrt((1 / n) * np.sum((hist * np.power(k - mu, 2))[0:s+1]))


def sigma2(hist, s, n, mu):
    k = np.arange(0, 256)
    return np.sqrt((1 / n) * np.sum((hist * np.power(k - mu, 2))[s+1:256]))


def Q(hist, s):
    n_1, n_2 = n1(hist, s), n2(hist, s)
    if n_1 == 0 or n_2 == 0:
        return 0
    mu_1, mu_2 = mu1(hist, s, n_1), mu2(hist, s, n_2)
    sigma_1, sigma_2 = sigma1(hist, s, n_1, mu_1), sigma2(hist, s, n_2, mu_2)
    _mean = mean(hist)

    sigma_zw = n_1 * np.power(mu_1 - _mean, 2) + n_2 * np.power(mu_2 - _mean, 2)
    sigma_in = n_1 * np.power(sigma_1, 2) + n_2 * np.power(sigma_2, 2)
    q = np.power(sigma_zw, 2) / np.power(sigma_in, 2)
    return q

''' Load data '''
# Load images and template
img = cv2.imread("../../data/cameraman.png", cv2.IMREAD_GRAYSCALE)

histr = cv2.calcHist([img], [0], None, [256], [0, 256])
histr = histr[:, 0]
plt.plot(histr)
plt.xlim([0, 256])

''' Iterate over all s '''
q_list = list()

for s in range(1, 255):
    q_list.append(Q(histr, s))

optimal_s = np.argmax(np.asarray(q_list))
print("Threshold:", optimal_s)

''' Visualize result '''
mask = img >= optimal_s

cv2.imshow("img", img)
cv2.imshow("mask", mask.astype(np.uint8) * 255)

plt.show()
cv2.waitKey(0)