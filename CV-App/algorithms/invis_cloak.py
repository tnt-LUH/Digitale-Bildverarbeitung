import cv2
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

from . import Algorithm


class InvisCloak (Algorithm):

    """ init function """
    def __init__(self):
        pass

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


        """ 2.2 Farbanalyse """
        """ 2.2.1 RGB """
        self._221_RGB(img)
        """ 2.2.2 HSV """
        self._222_HSV(img)


        """ 2.3 Segmentierung und Bildmdifikation """
        img = self._23_SegmentUndBildmodifizierung(img)

        return img

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

    def _221_RGB(self, img):
        """
            Hier steht Ihr Code zu Aufgabe 2.2.1 (RGB)
            - Histogrammberechnung und Analyse
        """
        pass


    def _222_HSV(self, img):
        """
            Hier steht Ihr Code zu Aufgabe 2.2.2 (HSV)
            - Histogrammberechnung und Analyse im HSV-Raum
        """
        pass


    def _23_SegmentUndBildmodifizierung (self, img):
        """
            Hier steht Ihr Code zu Aufgabe 2.3.1 (StatischesSchwellwertverfahren)
            - Binärmaske erstellen
        """


        """
            Hier steht Ihr Code zu Aufgabe 2.3.2 (Binärmaske)
            - Binärmaske optimieren mit Opening/Closing
            - Wahl größte zusammenhängende Region
        """


        """
            Hier steht Ihr Code zu Aufgabe 2.3.1 (Bildmodifizerung)
            - Hintergrund mit Mausklick definieren
            - Ersetzen des Hintergrundes
        """


        return img