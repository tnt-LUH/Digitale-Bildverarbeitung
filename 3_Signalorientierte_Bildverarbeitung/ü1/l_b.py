import numpy as np
import cv2
import math


def dct(a: np.ndarray):
    a_freq = np.zeros_like(a)
    N, M = a_freq.shape[1], a_freq.shape[0]
    # Iteriere über jeden Koeffizienten
    for k in range(N):
        for m in range(M):
            dct_k_m = 0
            # Iteriere über jede Position im Ortsraum
            for x in range(N):
                for y in range(M):
                    dct_k_m += a[y, x] * np.cos(k*np.pi*(2*x+1)/(2*N)) * np.cos(m*np.pi*(2*y+1)/(2*M))
            dct_k_m = 4 * dct_k_m / (np.sqrt(2*N) * np.sqrt(2*M))
            a_freq[m, k] = dct_k_m
    return a_freq


def idct(a_freq: np.ndarray):
    a = np.zeros_like(a_freq)
    N, M = a_freq.shape[1], a_freq.shape[0]
    a_freq = (np.sqrt(2*N) * np.sqrt(2*M)) * a_freq / 16
    a_freq[0, :] = a_freq[0, :] / 2
    a_freq[:, 0] = a_freq[:, 0] / 2
    # Iteriere über jeden Koeffizienten
    for x in range(N):
        for y in range(M):
            f_x_y = 0 #a_freq[0, 0] / (4)# * np.sqrt(2))
            # Iteriere über jede Position im Ortsraum
            for k in range(N):
                for m in range(M):
                    f_x_y += a_freq[m, k] * np.cos(k*np.pi*(2*x+1)/(2*N)) * np.cos(m*np.pi*(2*y+1)/(2*M))
            f_x_y = f_x_y / 4
            a[y, x] = f_x_y
    return a


def remove_dct(img, rate):
    """
    Diese Implementierung wendet die diskrete Fourier Transformation auf das Bild img an. Daraufhin werden die hoch-
    frequenten Anteile anteilig der Rate rate entfernt. Am Ende wird das Bild wieder in den Bildbereich transformiert.
    :param img:
    :param rate:
    :return:
    """
    assert rate <= 1, "Die Rate muss kleiner gleich 1 sein!"

    height, width = img.shape
    for i in range(math.ceil(width / 8)):
        for j in range(math.ceil(height / 8)):
            # Block extrahieren
            block = np.zeros((8, 8))
            horizontal_pixel, vertical_pixel = min(8, width - i * 8), min(8, height - j * 8)
            block[0:vertical_pixel, 0:horizontal_pixel] = \
                img[j * 8: (j * 8) + vertical_pixel, i * 8: (i * 8) + horizontal_pixel]
            # In den Frequenzbereich tranformieren
            block_freq = dct(block)
            # Hochfrequente Anteile löschen
            values_to_delete = 8 * 8 * rate
            values_deleted = 0
            for m in range(0, 16):
                for n in range(0, m + 1):
                    if values_deleted >= values_to_delete:
                        break
                    if 7 - m + n < 0 or 7 - n < 0:
                        continue
                    block_freq[7 - m + n, 7 - n] = 0.
                    values_deleted += 1
            # Rücktransformation in den Bildbereich
            block = idct(block_freq)
            # Einfügen in Ursprungsbild
            img[j * 8: (j * 8) + vertical_pixel, i * 8: (i * 8) + horizontal_pixel] = \
                block[0:vertical_pixel, 0:horizontal_pixel]

    return img


''' Bild laden '''
img = cv2.imread("../../data/cameraman.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (160, 160))
img = (img.astype(np.float64) / 256)
cv2.imshow("ORIGINAL", img)

''' Funktion anwenden '''
img = remove_dct(img, 0.8)

''' Bild anzeigen '''
cv2.imshow("IMG", img)
cv2.waitKey(0)