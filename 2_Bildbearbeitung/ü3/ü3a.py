import numpy as np
import cv2

''' Einlesen des Bildes '''
img = cv2.imread("data/normal.jpg")

''' 
Schritt 1: Geben Sie eine Transformationvorschrift T an, die das Eingangsbild
    - mit dem Faktor s_x ungleich 0 in x-Richtung skaliert 
    - mit dem Faktor s_y ungleich 0 in y-Richtung skaliert 
'''
s_x = 2
s_y = 2

''' 
Schritt 2: Geben Sie geben sie die Inverse T_inv zu T an
'''


'''
Schritt 3: Implementieren Sie eine Funktion scale(img, sx, sy), welche das Bild nach der Skalierung wiedergibt.
Verwenden Sie für die Transformation das Backward-Mapping und für die Interpolation Nearest-Neighbour Interpolation.
'''


def scale(img, s_x, s_y):

    return new_img


''' Ausgabe des Bildes '''
new_img = scale(img, 2, 2)
cv2.imshow('img', new_img)
cv2.waitKey(0)
