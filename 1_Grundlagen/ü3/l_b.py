import numpy as np
import cv2

# Einlesen des Bildes
filepath = "../../data/lena.png"
img = cv2.imread(filepath)

'''
Anwendung der Schritte:
    0. Für die Berechnung werden die Bilder in das kontinuierliche np.float64 konvertiert. 
    1. In Wertebereich {0, ..., 127}
    2. In Wertebereich {0, ..., 3}
    3. In Wertebereich {0, ..., 255}
'''

img_step0 = img.astype(np.float64)
img_step1 = np.round(127 * np.copy(img_step0) / 255)
img_step2 = np.round(3 * np.copy(img_step1) / 127)
img_step3 = np.round(255 * np.copy(img_step2) / 3)

'''
Für die Darstellung von np.float64 Bildern wird der Wertebereich von {0,  ..., n_max} in [0, 1] projeziert.
Dabei entspricht der Wert 1 dem ehemaligen Maximum n_max.
'''

img_step0 = img_step0 / 255
img_step1 = img_step1 / 127
img_step2 = img_step2 / 3
img_step3 = img_step3 / 255

cv2.imshow("Schritt 0", img_step0)
cv2.imshow("Schritt 1", img_step1)
cv2.imshow("Schritt 2", img_step2)
cv2.imshow("Schritt 3", img_step3)

cv2.waitKey(0)
