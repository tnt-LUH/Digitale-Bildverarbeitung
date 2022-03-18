import numpy as np
import cv2

''' Bild laden und in den Frequenzraum transformieren '''
img = cv2.imread("../../data/car2.png", cv2.IMREAD_GRAYSCALE)
img = img.astype(float)
i_max, i_min = np.max(img), np.min(img)
img = (img - i_min) / (i_max - i_min)

cv2.imshow("Original", img )

''' 1. Logarithmieren '''
img_log = np.maximum(img, 1/255)  # log(0) ist illegal!
img_log = np.log(img_log)

''' 2. in den Frequenzbereich transformieren '''
IMG = np.fft.fft2(img_log)

''' 3. Niedrige mit H(k,l)Frequenzen unterdrücken '''
gamma1, gamma2, gamma3 = 0.5, 0., 4
H = np.zeros_like(img_log)
for l in range(H.shape[0]):
    for k in range(H.shape[1]):
        if k < 1 and l < 1:
            H[l, k] = 1
        else:
            H[l, k] = gamma1 - (gamma1 - gamma2) * np.exp(-(k*k + l*l) / (gamma3 * gamma3))

IMG = IMG * H

''' 4. Rücktransformation '''
img_filtered = np.fft.ifft2(IMG)
img_filtered = img_filtered.astype(float)

''' 5. Umkehrfunktion der Logarithmierung '''
img_filtered = np.exp(img_filtered)

''' Ergebnis anzeigen '''
i_max, i_min = np.max(img_filtered), np.min(img_filtered)
img_filtered = (img_filtered - i_min) / (i_max - i_min)
cv2.imshow("Homomorphe Filterung", img_filtered)
cv2.waitKey()