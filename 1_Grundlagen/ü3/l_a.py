import numpy as np
import cv2

# Hiermit kann die Methode für die Berechnung ausgewählt werden
METHOD = "MANUELL"  # OpenCV, MANUELL

# Einlesen des Bildes
filepath = "../../data/flower.jpeg"
img = cv2.imread(filepath)

h, w, c = img.shape
print("Originale Breite:", w)
print("Originale Höhe:", h)

scales = [4, 8, 13.5]
images = []

for scale in scales:
    new_w, new_h = round(w / scale), round(h / scale)

    if METHOD == "OpenCV":
        new_image = cv2.resize(img, (new_w, new_h))
        # Frage 1: Welche Interpolations-Methode wird hier verwendet?

    elif METHOD == "MANUELL":
        new_image = np.zeros((new_h, new_w, c), dtype=np.uint8)
        for x in range(new_w):
            for y in range(new_h):
                x_projected, y_projected = min(w - 1, round(x * scale)), min(h - 1, round(y * scale))
                new_image[y, x] = img[y_projected, x_projected]
                # Frage 1: Welche Interpolations-Methode wird hier verwendet?
                # Frage 2: Welches Mapping wird hier verwendet (For- oder Backwardmapping)?

    else:
        raise Exception("Da ist wohl ein Fehler unterlaufen!")

    images.append(new_image)

# Bilder darstellen
show_w, show_h = 1200, 1200
img = cv2.resize(img, (show_w, show_h))
cv2.imshow("Original", img)
for scale, image in zip(scales, images):
    image = cv2.resize(image, (show_w, show_h))
    cv2.imshow("Scale %s" % scale, image)
cv2.waitKey(0)
