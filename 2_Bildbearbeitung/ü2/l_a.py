import numpy as np
import cv2

''' Einlesen des Bildes '''
I_in = [
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
    [100, 100, 100, 100, 100],
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
]

I_in = np.asarray(I_in, dtype="uint8")

print("Bild vor der Bearbeitung:")
print(I_in)
print()
print(I_in.dtype)

''' Operation 1: Kantenfilter '''
edge = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]
edge = np.asarray(edge)
edge_conv = np.flip(edge)
I_in = cv2.filter2D(I_in, cv2.CV_64F, edge, borderType=cv2.BORDER_REPLICATE)
print("Operation 1: Kantenfilter")
print(I_in)
print()

''' Operation 2: Absolutwertbildung '''
I_in = np.abs(I_in)
print("Operation 2: Absolutwertbildung")
print(I_in)
print()

''' Operation 3: Medianfilter'''
I_in = cv2.medianBlur(I_in.astype("float32"), 3)
print("Operation 3: Medianfilter")
print(I_in)
print()

''' Operation 4: Schwellwert '''
I_in = np.copy(I_in)
ret, I_out = cv2.threshold(I_in, 127, 255, cv2.THRESH_BINARY)
print("Operation 4: Schwellwert")
print(I_out)
print()