import numpy as np
import cv2


# Einlesen des Bildes
filepath = "../../data/balls.png"


''' a) Manuelles Konvertieren '''
img_norm = img.astype(np.float32) / 255.0
height, width, channels = img.shape
hsv_img = np.zeros_like(img_norm)

for x in range(width):
    for y in range(int(height)):


hsv_img = np.round(hsv_img * 255)
hsv_img = hsv_img.astype(np.uint8)

''' b) Konvertieren mit OpenCV '''
hsv_img2 =


''' Das Ergebnis überprüfen '''
img2 = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
img3 = cv2.cvtColor(hsv_img2, cv2.COLOR_HSV2BGR)

difference = np.sum(np.abs(img2 - img3))
print("Totale Differenz zwischen den Ergebnissen:", difference)
max_difference = np.max(np.abs(img2 - img3))
print("Maximale Abweichung pro Pixel/Kanal:", max_difference)
example_differences = img2[0:10, 0:10] - img3[0:10, 0:10]
print("Beispiel Differenzen:\n", example_differences)

cv2.imshow("ORIGINAL", img)
cv2.imshow("MANUELL", img2)
cv2.imshow("OPENCV", img3)
cv2.waitKey(0)
