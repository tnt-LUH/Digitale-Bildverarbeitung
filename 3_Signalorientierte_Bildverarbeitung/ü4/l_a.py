import cv2
import numpy as np

raster = cv2.imread("../../data/lena_raster.png", cv2.IMREAD_GRAYSCALE)
normal = cv2.imread("../../data/lena.png", cv2.IMREAD_GRAYSCALE)

''' FFT '''
RASTER = np.fft.fftshift(np.fft.fft2(raster))
RASTER_magnitude = np.abs(RASTER)
RASTER_angle = np.angle(RASTER)

NORMAL = np.fft.fftshift(np.fft.fft2(normal))
NORMAL_magnitude = np.abs(NORMAL)
NORMAL_angle = np.angle(NORMAL)

''' Maskieren '''
centroids = [
    [85, 85],
    [255, 85],
    [425, 85],
    [85, 255],
    [255, 425],
    [425, 255],
    [85, 425],
    [425, 425]
]

s = 10
for x, y in centroids:
    RASTER[np.maximum(0, y - s):y + s, np.maximum(0, x - s):x + s] = 0
FILTERED_magnitude = np.abs(RASTER)

''' Inverse fft '''
filtered = np.fft.ifft2(np.fft.ifftshift(RASTER)).astype(np.uint8)

''' Bild anzeigen '''
cv2.imshow("raster", raster)
cv2.imshow("normal", normal)
cv2.imshow("RASTER_magnitude", 255 * RASTER_magnitude / np.max(RASTER_magnitude))
cv2.imshow("NORMAL_magnitude", 255 * NORMAL_magnitude / np.max(NORMAL_magnitude))
cv2.imshow("FILTERED_magnitude", 255 * FILTERED_magnitude / np.max(FILTERED_magnitude))
cv2.imshow("filtered", filtered)

cv2.waitKey()
