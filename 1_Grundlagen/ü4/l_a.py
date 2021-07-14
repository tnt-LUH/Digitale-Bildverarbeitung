import cv2

''' Öffnen einer Kamera und Initialisierung von Variablen '''
img = cv2.imread("./data/Mauer.png")
cv2.imshow("Original", img)

downscaled2 = cv2.resize(img, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
downscaled2_original_size = cv2.resize(downscaled2, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Abgetastet mit Faktor 2", downscaled2_original_size)

downscaled4 = cv2.resize(img, dsize=None, fx=0.25, fy=0.25, interpolation=cv2.INTER_NEAREST)
downscaled4_original_size = cv2.resize(downscaled4, dsize=None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Abgetastet mit Faktor 4", downscaled4_original_size)

downscaled10 = cv2.resize(img, dsize=None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
downscaled10_original_size = cv2.resize(downscaled10, dsize=None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Abgetastet mit Faktor 10", downscaled10_original_size)

cv2.waitKey(0)