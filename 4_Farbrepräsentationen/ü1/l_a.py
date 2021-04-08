import numpy as np
import cv2


# Einlesen des Bildes
filepath = "../../data/balls.png"
img = cv2.imread(filepath)

''' a) Manuelles Konvertieren '''
img_norm = img.astype(np.float32) / 255.0
height, width, channels = img.shape
hsv_img = np.zeros_like(img_norm)

for x in range(width):
    for y in range(int(height)):
        minimum = np.min(img_norm[y, x])
        b, g, r = img_norm[y, x, 0], img_norm[y, x, 1], img_norm[y, x, 2]
        # V Wert
        v = np.max(img_norm[y, x].copy())

        # S Wert
        if v == 0:
            s = 0
        else:
            s = (v - minimum) / v

        # H Wert
        max_channel_index = np.argmax(img_norm[y, x])
        if (v - np.min(img_norm[y, x])) == 0:
            h = np.zeros(1)
        elif max_channel_index == 2:  # Rot
            h = 60 * (g - b) / (v - minimum)
        elif max_channel_index == 1:  # Grün
            h = 120 + 60 * (b - r) / (v - minimum)
        else:  # Blau
            h = 240 + 60 * (r - g) / (v - minimum)
        if h < 0:
            h += 360
        h /= (2 * 255)

        hsv_img[y, x, 0] = h
        hsv_img[y, x, 1] = s
        hsv_img[y, x, 2] = v

hsv_img = np.round(hsv_img * 255)
hsv_img = hsv_img.astype(np.uint8)

''' b) Konvertieren mit OpenCV '''
hsv_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


''' Das Ergebnis überprüfen '''
img2 = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
img3 = cv2.cvtColor(hsv_img2, cv2.COLOR_HSV2BGR)

difference = np.sum(np.abs(img2 - img3))
print("Totale Differenz zwischen den Ergebnissen:", difference)
max_difference = np.max(np.abs(img2 - img3))
print("Maximale Abweichung pro Pixel/Kanal:", max_difference)
example_differences = img2[0:3, 0:3] - img3[0:3, 0:3]
print("Beispiel Differenzen:\n", example_differences)

cv2.imshow("ORIGINAL", img)
cv2.imshow("MANUELL", img2)
cv2.imshow("OPENCV", img3)
cv2.waitKey(0)
