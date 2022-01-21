import cv2
import numpy as np

img = cv2.imread("../../data/teppich.png", cv2.IMREAD_GRAYSCALE)


''' FFT '''
IMG = np.fft.fft2(img)
MAGNITUDE = np.abs(IMG)
ANGLE = np.angle(IMG)

''' Filter out frequencies '''



''' IFFT '''
IMG = MAGNITUDE * np.exp(1j * ANGLE)
filtered_image = np.fft.ifft2(IMG).astype(np.float32)

''' Bild anzeigen '''
cv2.imshow("img", img)
cv2.imshow("filtered", filtered_image / np.max(filtered_image))

cv2.waitKey(0)
