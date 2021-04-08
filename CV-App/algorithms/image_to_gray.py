import cv2

from . import Algorithm


class ImageToGray(Algorithm):
    """ Converts a BGR image to grayscale"""
    def process(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img
