import cv2
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

from . import Algorithm


class SilhouetteGhost (Algorithm):

    """ init function """
    def __init__(self):
        self.image_count = 0
        self.background = None
        self.background_update_rate = 0.2
        self.threshold = 15

    """ Processes the input image"""
    def process(self, img):

        """ 2.1 Vorverarbeitung """
        """ 2.1.1 Rauschreduktion """
        plotNoise = False   # Schaltet die Rauschvisualisierung ein
        if plotNoise:
            self._plotNoise(img, "Rauschen vor Korrektur")
        img = self._211_Rauschreduktion(img)
        if plotNoise:
            self._plotNoise(img, "Rauschen nach Korrektur")
        """ 2.1.2 HistogrammSpreizung """
        img = self._212_HistogrammSpreizung(img)


        """ 2.2 Vordergrund-Detektion """
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = img_gray.shape
        resized_img_gray = cv2.resize(img_gray, (int(w/2), int(h/2)), interpolation=cv2.INTER_NEAREST)
        blurred_img = cv2.GaussianBlur(resized_img_gray, (15, 15), 0)

        if self.background is None:
            self.background = blurred_img
        self.background = (1 - self.background_update_rate) * self.background + self.background_update_rate * blurred_img

        diff = blurred_img - self.background
        diff_abs = np.abs(diff)
        binary_image = diff_abs > self.threshold

        """ 2.2.1 Opening und Closing """
        binary_image = self._221_OpeningClosing(binary_image)

        """ 2.3 Canny-Edge und Bildmodifizierung """
        canny_edges = self._231_CannyEdge(resized_img_gray)

        canny_edges = canny_edges * binary_image
        canny_edges = cv2.resize(canny_edges, (int(w), int(h)), interpolation=cv2.INTER_NEAREST)

        return canny_edges

    """ Reacts on mouse callbacks """
    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            print("A Mouse click happend! at position", x, y)


    def _plotNoise(self, img, name:str):
        height, width = np.array(img.shape[:2])
        centY = (height / 2).astype(int)
        centX = (width / 2).astype(int)

        cutOut = 5
        tmpImg = deepcopy(img)
        tmpImg = tmpImg[centY - cutOut:centY + cutOut, centX - cutOut:centX + cutOut, :]

        outSize = 500
        tmpImg = cv2.resize(tmpImg, (outSize, outSize), interpolation=cv2.INTER_NEAREST)

        cv2.imshow(name, tmpImg)
        cv2.waitKey(1)

    def _211_Rauschreduktion(self, img):
        """
            Hier steht Ihr Code zu Aufgabe 2.1.1 (Rauschunterdrückung)
            - Implementierung Mittelwertbildung über N Frames
        """


        return img

    def _212_HistogrammSpreizung(self, img):
        """
            Hier steht Ihr Code zu Aufgabe 2.1.2 (Histogrammspreizung)
            - Transformation HSV
            - Histogrammspreizung berechnen
            - Transformation BGR
        """

        return img

    def _221_OpeningClosing(self, binary_image):
        """
            Hier steht Ihr Code zu Aufgabe 2.2.1 (Opening and Closing)
            - Implementieren Sie das Closing
            - Speichern Sie das aktuelle Bild vor und nach der Funktion beim Mausklick
        """

        return binary_image

    def _231_CannyEdge (self, img_gray):
        """
            Hier steht Ihr Code zu Aufgabe 2.3.1 (Manuelle Canny Edge Implementierung)
            - Glättung
            - Gradienten berechnen
            - Nicht-Maximum Unterdrückung
            - Hysterese Unterdrückung
        """

        """ 1. Glättung """


        """ 2. Gradienten berechnen """


        """ 3. Nicht-Maximum Unterdrückung """


        """ 4. Hysterese Unterdrückung """
        #parameter:
        thresh1 = 50
        thresh2 = 100


        return np.ones_like(img_gray) * 255 # hier eigenes Edge-Bild ausgeben