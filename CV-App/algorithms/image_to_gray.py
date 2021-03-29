import cv2

from . import Algorithm


class ImageToGray(Algorithm):
    def process(self, img):
        """ Converts a BGR image to grayscale"""
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img
