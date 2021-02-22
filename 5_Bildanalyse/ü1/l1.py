import numpy as np
import cv2

KERNEL_SIZE = 20

''' Schritt 1: Einlesen der Bilder '''
surv1 = cv2.imread("../../data/surv_01.png")
surv2 = cv2.imread("../../data/surv_02.png")

''' Schritt 2: Konvertieren in den Grauwertbereich '''
surv1 = cv2.cvtColor(surv1, cv2.COLOR_BGR2GRAY)
surv2 = cv2.cvtColor(surv2, cv2.COLOR_BGR2GRAY)

''' Schritt 3: Erzeugen des Differenzbildes '''
print("Minimam und Maximum bevor Transformation:", np.min(surv1), np.max(surv1))
print("   -> Wertebereich ist {0, ..., 255}")
surv1 = surv1 / 255
surv2 = surv2 / 255
print("Minimam und Maximum nach Transformation:", np.min(surv1), np.max(surv1))
print("   -> Wertebereich ist [0, 1]")

diff1 = surv1 - surv2
diff1 = np.abs(diff1)  # Absolutwertbildung für die Darstellellung (OpenCV kennt nur positive Werte!)

''' Schritt 4: Darstellen des Differenzbildes '''
cv2.imshow("Differenz ohne Schwellwert ", diff1)

''' Schritt 5: Darstellen des Differenzbildes mit Schwellwert '''
diff2 = np.copy(diff1)
diff2[diff2 < 0.5] = 0
cv2.imshow("Differenz mit Schwellwert ", diff2)

cv2.waitKey(0)  # Dieser Befehl ist nötig, um die Darstellung auf dem Bildschirm zu behalten

