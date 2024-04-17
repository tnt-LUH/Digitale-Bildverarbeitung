import numpy as np
import cv2

camera = cv2.VideoCapture(0)

signum = 1
factor = 0.3
while True:
    ret, bgr = camera.read()

    ''' Aufgabe a) '''
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = np.round(hsv[:, :, 2] * factor)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    ''' Visualisierung  '''
    # Display the resulting frame
    cv2.imshow('frame', bgr)
    if 27 == cv2.waitKey(1):  # Taste "q"
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
