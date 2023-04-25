import cv2
import numpy as np

''' Öffnen einer Kamera und Initialisierung von Variablen '''
cap = cv2.VideoCapture(0)
mode = "RGB"  # CHROMINANZ, LUMINANZ
window_name = "Ergebnis mit %s" % mode

''' Auslesen, Modifizieren und Ausgeben von Bildern'''
while True:
    ret, frame = cap.read()

    if mode == "LUMINANZ":
        # Farbinformationen entfernen
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == "CHROMINANZ":
        # Normalisieren: p_r / (p_r + p_g + p_b), p_g / (p_r + p_g + p_b), p_b / (p_r + p_g + p_b)
        pixel_sum = np.sum(frame, keepdims=True, axis=2)
        frame = frame.astype(np.float32) / pixel_sum
    elif mode == "RGB":
        pass
    else:
        raise Exception("FALSCHER MODE!!!")

    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

''' Fenster schließen, nachdem q gedrückt wurde'''''
cap.release()
cv2.destroyAllWindows()
