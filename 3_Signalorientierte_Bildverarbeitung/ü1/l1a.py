import numpy as np
import cv2
import math


def remove_dft(img, rate):
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
            block_freq = np.fft.fft2(block)
            # Hochfrequente Anteile löschen
            values_to_delete = 8 * 8 * rate
            values_deleted = 0
            for m in range(0, 16):
                for n in range(0, m + 1):
                    if values_deleted >= values_to_delete:
                        break
                    if 7 - m + n < 0 or 7 - n < 0:
                        continue
                    block_freq[7 - m + n, 7 - n] = 0. + 0.j
                    values_deleted += 1

            # Rücktransformation in den Bildbereich
            block = np.fft.ifft2(block_freq)
            # Einfügen in Ursprungsbild
            img[j * 8: (j * 8) + vertical_pixel, i * 8: (i * 8) + horizontal_pixel] = \
                block[0:vertical_pixel, 0:horizontal_pixel]

    return img


''' Bild laden '''
img = cv2.imread("../../data/cameraman.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = (img / 256).astype(np.float32)

''' Funktion anwenden '''
img = remove_dft(img, 0.9)

''' Bild anzeigen '''
cv2.imshow("IMG", img)
cv2.waitKey(0)