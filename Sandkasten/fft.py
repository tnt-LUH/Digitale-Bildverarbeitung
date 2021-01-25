import cv2
import numpy as np
from matplotlib import pyplot as plt


images = ["data/1.png", "data/2.png", "data/3.png", "data/4.png", "data/5.png"]

lena = cv2.imread(images[0])

lena = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)

grauwerte, beugungen = list(), list()
for image in images:
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grauwerte.append(gray)
    f = np.fft.fft2(gray)  # Fouriertransformation
    fshift = np.fft.fftshift(f)  # Umsortieren
    FT = np.abs(fshift)
    FT = np.log(np.abs(fshift))  # mit log() wird der Kontrast angehoben
    beugungen.append(FT)

i = 0
for gray, FT in zip(grauwerte, beugungen):
    i += 1
    plt.figure(figsize=(12, 12))
    plt.subplot(121)
    plt.xticks([]), plt.yticks([])
    plt.imshow(gray, cmap = 'gray')
    plt.title('Lena')

    plt.subplot(122)
    plt.xticks([]), plt.yticks([])
    plt.imshow(FT, cmap=plt.cm.gray)
    plt.title('Fouriertransformierte von Lena')
    #plt.show()
    FT = np.round( 255 * (FT + np.min(FT)) / (np.abs(np.max(FT)) + np.abs(np.min(FT))))
    cv2.imwrite(f"/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/fft/{i}_grau.png", gray)
    cv2.imwrite(f"/home/kaiser/Schreibtisch/ownCloud/Vorlesung/DigitaleBildverarbeitung/Klausuren/Klausur_WS2021/images/fft/{i}_fft.png", FT)
    #print(np.max(FT), np.min(FT))