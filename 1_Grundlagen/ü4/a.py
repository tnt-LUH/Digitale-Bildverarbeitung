import cv2

''' Öffnen einer Kamera und Initialisierung von Variablen '''
img = cv2.imread("./data/Mauer.png")
cv2.imshow("Original", img)

cv2.waitKey(0)