import cv2
import numpy as np

from . import Algorithm


class Spin(Algorithm):
    """ Rotates an image """

    def __init__(self):
        self.current_angle = 0  # between 0 and 2 pi
        self.anlge_per_image = 360 / 100

    def process(self, img):
        self.current_angle = (self.current_angle + self.anlge_per_image) % 360
        w, h = img.shape[1], img.shape[0]
        image_center = (w / 2, h / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, self.current_angle, 1.0)
        img = cv2.warpAffine(img, rot_mat, (w, h), flags=cv2.INTER_LINEAR)
        return img

