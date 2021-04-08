import numpy as np
import cv2

''' Einlesen des Bildes '''
I_in = cv2.imread("data/edge_01.png")
I_in = cv2.cvtColor(I_in, cv2.COLOR_BGR2GRAY)
cv2.imshow("Bild Schritt 0", I_in)


''' Operation 1: Median-Filter'''
I_in = cv2.medianBlur(I_in, 9)
cv2.imshow("Bild Schritt 1", I_in)

''' Operation 2: Kantenfilter'''
edge = [
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
]
edge = np.asarray(edge)
I_in = cv2.filter2D(I_in, cv2.CV_64F, edge, borderType=cv2.BORDER_REPLICATE)
cv2.imshow("Bild Schritt 2", I_in)

''' Operation 3: Glättung / Tiefpass mit Boxfilter'''
edge = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
edge = np.asarray(edge) / 9
I_in = cv2.filter2D(I_in, cv2.CV_64F, edge, borderType=cv2.BORDER_REPLICATE)
I_in = I_in / np.max(I_in)
cv2.imshow("Bild Schritt 3", I_in)

''' Bilder anzeigen, Bis Taste gedrückt wird '''
cv2.waitKey(0)