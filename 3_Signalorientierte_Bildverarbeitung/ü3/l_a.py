import cv2
import numpy as np

img = cv2.imread("../../data/lena.png", cv2.IMREAD_GRAYSCALE)

''' Rauschen hinzufügen '''
h, w = img.shape
saltpepper_noise = np.zeros((h, w), dtype=np.uint8)
saltpepper_noise = cv2.randu(saltpepper_noise, 0, 255)
black = saltpepper_noise < 15
white = saltpepper_noise > 240
img_noise = np.copy(img)
img_noise[white] = 255
img_noise[black] = 0

''' FFT '''
visual_factor = 100000
IMG = np.fft.fftshift(np.fft.fft2(img))
IMG_magnitude = np.abs(IMG)
cv2.imshow("IMG_magnitude", IMG_magnitude / visual_factor)

IMG_NOISE = np.fft.fftshift(np.fft.fft2(img_noise))
IMG_NOISE_magnitude = np.abs(IMG_NOISE)
cv2.imshow("IMG_NOISE_magnitude", IMG_NOISE_magnitude / visual_factor)

''' Bild anzeigen '''
cv2.imshow("img", img)
cv2.imshow("img_noise", img_noise)
cv2. waitKey()