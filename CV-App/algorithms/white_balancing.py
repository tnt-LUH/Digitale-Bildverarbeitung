import cv2
import numpy as np

from . import Algorithm


class WhiteBalancing(Algorithm):
    """ White Balancing """

    def __init__(self):
        """ Define Reference RGB values to (255, 255, 255) """
        self.max_b, self.max_g, self.max_r = 255, 255, 255
        self.last_image = None

    def process(self, img):
        """ Performs white balancing based on the reference RGB values """
        self.last_image = img
        img = img.astype(np.float32)
        img[:, :, 0] = np.clip(img[:, :, 0], 0, self.max_b) * 255 / max(1, self.max_b)
        img[:, :, 1] = np.clip(img[:, :, 1], 0, self.max_g) * 255 / max(1, self.max_g)
        img[:, :, 2] = np.clip(img[:, :, 2], 0, self.max_r) * 255 / max(1, self.max_r)
        img = img.astype(np.uint8)
        return img

    def mouse_callback(self, event, x, y, flags, param):
        """ Selects new reference RGB values, if left mouse button is clicked and self.last_image is defined """
        if self.last_image is None:
            return
        if event == cv2.EVENT_LBUTTONUP:
            self.max_b, self.max_g, self.max_r = \
                self.last_image[y, x, 0], self.last_image[y, x, 1], self.last_image[y, x, 2]
