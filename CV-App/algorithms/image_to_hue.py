import cv2
import numpy as np

from . import Algorithm


class ImageToHue(Algorithm):
    """ Normalizes a BGR image with color information"""
    def process(self, img):
        channel_sum = np.sum(img.astype(np.float32), axis=2, keepdims=True)
        img_normalized = img.astype(np.float32) * 255 / channel_sum
        img_normalized = img_normalized.astype(np.uint8())
        return img_normalized
