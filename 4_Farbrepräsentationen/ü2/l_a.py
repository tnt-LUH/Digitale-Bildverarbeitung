import numpy as np
import cv2

camera = cv2.VideoCapture(0)

signum = 1
factor = 0.3
while True:
    ''' Aufgabe a) '''
    ret, bgr = camera.read()

    ''' Aufgabe b) '''
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = np.round(hsv[:, :, 2] * factor)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    ''' Aufgabe c) '''
    if factor == 0:
        signum = 1
    elif factor == 1:
        signum = -1
    factor += signum * 0.02
    factor = min(1, factor)
    factor = max(0, factor)

    ''' Visualisierung  '''
    # Display the resulting frame
    cv2.imshow('frame', bgr)
    if 27 == cv2.waitKey(1):  # Taste "q"
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()