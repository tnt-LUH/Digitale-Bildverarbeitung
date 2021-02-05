import numpy as np
import cv2

# Hiermit kann die Methode für die Berechnung ausgewählt werden
METHOD = "MANUELL"  # OpenCV

# Einlesen des Bildes
filepath = "../../data/flower.jpeg"
img = cv2.imread(filepath)

h, w, c = img.shape
print("Originale Breite:", w)
print("Originale Höhe:", h)

scales = [4, 8, 13.5]
images = []

# todo Methode MANUELL implementieren und 'images' mit diskretisierten Bildern füllen

# todo Methode OpenCV implementieren und 'images' mit diskretisierten Bildern füllen

# todo Bilder darstellen
