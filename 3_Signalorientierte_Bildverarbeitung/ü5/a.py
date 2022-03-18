import numpy as np
import cv2

''' Bild laden und in den Frequenzraum transformieren '''
img = cv2.imread("../../data/car2.png", cv2.IMREAD_GRAYSCALE)
img = img.astype(float)
i_max, i_min = np.max(img), np.min(img)
img = (img - i_min) / (i_max - i_min)

cv2.imshow("Original", img )

''' 1. Logarithmieren '''

''' 2. in den Frequenzbereich transformieren '''

''' 3. Niedrige mit H(k,l)Frequenzen unterdrücken '''

''' 4. Rücktransformation '''

''' 5. Umkehrfunktion der Logarithmierung '''

''' Ergebnis anzeigen '''
i_max, i_min = np.max(img_filtered), np.min(img_filtered)
img_filtered = (img_filtered - i_min) / (i_max - i_min)
cv2.imshow("Homomorphe Filterung", img_filtered)
cv2.waitKey()