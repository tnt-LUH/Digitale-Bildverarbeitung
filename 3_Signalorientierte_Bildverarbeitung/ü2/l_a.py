import numpy as np
import cv2


def get_motion_psf(kernel_size, motion_angle, motion_dis):
    """ "Point Spread Function" um Bewegung zu simulieren """
    psf = np.zeros(kernel_size)  # point spread function
    x_center = (kernel_size[0] - 1) / 2
    y_center = (kernel_size[1] - 1) / 2

    sin_val = np.sin(motion_angle * np.pi / 180)
    cos_val = np.cos(motion_angle * np.pi / 180)

    for i in range(motion_dis):
        x_offset = round(sin_val * i)
        y_offset = round(cos_val * i)
        psf[int(x_center - x_offset), int(y_center + y_offset)] = 1

    return psf / psf.sum()


''' Bild laden und in den Frequenzraum transformieren '''
img = cv2.imread("../../data/eth_blurred.png", cv2.IMREAD_GRAYSCALE)
IMG = np.fft.fft2(img)


''' Erstellen des Filterkernels und Transformation in den Frequenzraum '''
rows, cols = img.shape
h = get_motion_psf(kernel_size=(rows, cols), motion_angle=11, motion_dis=31)
h = np.fft.fftshift(h) # Muss gemacht werden, da der "Motion Blur Vector" mittig zentriert ist
H = np.fft.fft2(h)
H[np.abs(H) < 0.01] = 0.01  # Begrenzen der Degradationsfunktion um numerische Probleme zu verhindern

''' Inverses Filter anwenden '''
IMG_FILTERED = IMG / H
img_filtered = np.fft.ifft2(IMG_FILTERED).clip(0, 255).astype(np.uint8)

''' Ergebnis anzeigen '''
cv2.imshow("Original", img)
cv2.imshow("Inverses Filter", img_filtered)
cv2.waitKey()
