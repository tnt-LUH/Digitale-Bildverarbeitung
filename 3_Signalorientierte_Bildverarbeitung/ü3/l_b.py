import cv2
import numpy as np

car = cv2.imread("../../data/car.png", cv2.IMREAD_GRAYSCALE)
dog = cv2.imread("../../data/dog.png", cv2.IMREAD_GRAYSCALE)

''' FFT '''
CAR = np.fft.fft2(car)
CAR_magnitude = np.abs(CAR)
CAR_angle = np.angle(CAR)

DOG = np.fft.fft2(dog)
DOG_magnitude = np.abs(DOG)
DOG_angle = np.angle(DOG)

mix1 = CAR_magnitude * np.exp(1j * DOG_angle)
mix2 = DOG_magnitude * np.exp(1j * CAR_angle)

mix1 = np.fft.ifft2(mix1).astype(np.float32)
mix2 = np.fft.ifft2(mix2).astype(np.float32)

''' Bild anzeigen '''
cv2.imshow("car", car)
cv2.imshow("dog", dog)
cv2.imshow("mix1", mix1 / np.max(mix1))
cv2.imshow("mix2", mix2 / np.max(mix2))

cv2.waitKey()
