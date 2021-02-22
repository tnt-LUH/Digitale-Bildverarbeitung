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
T = np.asarray(
    [
        [s_x, 0],
        [0, s_y]
    ]
)

''' 
Schritt 2: Geben Sie geben sie die Inverse T_inv zu T an
'''

T_inv = np.linalg.inv(T)

'''
Schritt 3: Implementieren Sie eine Funktion scale(img, sx, sy), welche das Bild nach der Skalierung wiedergibt.
Verwenden Sie für die Transformation das Backward-Mapping und für die Interpolation Nearest-Neighbour Interpolation.
'''


def scale(img, s_x, s_y):
    rows, cols, channels = img.shape
    new_rows, new_cols = int(rows * s_y), int(cols * s_x)
    T = np.asarray([[s_x, 0], [0, s_y]])
    T_inv = np.linalg.inv(T)

    new_img = np.zeros((new_rows, new_cols, channels))
    for x in range(new_cols):
        for y in range(new_rows):
            position = np.asarray([x, y])
            old_position = np.matmul(position, T_inv)
            old_position = np.round(old_position).astype(int)
            old_x, old_y = old_position[0], old_position[1]
            # Überstpringen, wenn ausserhalb des Bildes
            if not 0 <= old_x < cols or not 0 <= old_y < rows:
                continue
            new_img[y, x] = img[old_y, old_x]
    return new_img.astype(np.uint8)


''' Ausgabe des Bildes '''
new_img = scale(img, 2, 2)
cv2.imshow('img', new_img)
cv2.waitKey(0)
