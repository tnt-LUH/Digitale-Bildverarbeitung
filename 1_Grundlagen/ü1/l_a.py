import cv2

''' Öffnen einer Kamera '''
cap = cv2.VideoCapture(0)
cv2.namedWindow("Ergebnis", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Ergebnis", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

''' Auslesen, Modifizieren und Ausgeben von Bildern'''
while True:
    ret, frame = cap.read()
    frame = frame[0:50, 0:50]
    cv2.imshow('Ergebnis', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

''' Fenster schließen, nachdem q gedrückt wurde'''''
cap.release()
cv2.destroyAllWindows()