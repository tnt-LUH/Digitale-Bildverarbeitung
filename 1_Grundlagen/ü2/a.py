import cv2
import numpy as np

''' Öffnen einer Kamera und Initialisierung von Variablen '''
cap = cv2.VideoCapture(0)
mode = "CHROMINANZ"  # CHROMINANZ, LUMINANZ
window_name = "Ergebnis mit %s" % mode

''' Auslesen, Modifizieren und Ausgeben von Bildern'''
while True:
    ret, frame = cap.read()

    if mode == "CHROMINANZ":
        frame = ...
    elif mode == "LUMINANZ":
        frame = ...
    else:
        raise Exception("FALSCHER MODE!!!")

    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

''' Fenster schließen, nachdem q gedrückt wurde '''
cap.release()
cv2.destroyAllWindows()