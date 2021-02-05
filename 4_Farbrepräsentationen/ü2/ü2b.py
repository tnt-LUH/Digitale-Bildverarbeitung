import numpy as np
import cv2

# Hiermit kann die Methode für die Berechnung ausgewählt werden
METHOD = "MANUELL"  # OpenCV

# Einlesen des Bildes
filepath = "../../data/lena.png"
img = cv2.imread(filepath)

h, w, c = img.shape

# todo Schritte 1-3 implementieren!