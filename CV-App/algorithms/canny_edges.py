import cv2
import numpy as np


from . import Algorithm


class CannyEdgeDetector(Algorithm):
    """ Converts a BGR image to grayscale"""
    def __init__(self):
        self.image_count = 0
        self.background = None
        self.background_update_rate = 0.2
        self.threshold = 15

    def process(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = img_gray.shape
        resized_image = cv2.resize(img_gray, (int(w/2), int(h/2)), interpolation=cv2.INTER_NEAREST)
        blurred_img = cv2.GaussianBlur(resized_image, (15, 15), 0)

        if self.background is None:
            self.background = blurred_img
        self.background = (1 - self.background_update_rate) * self.background + self.background_update_rate * blurred_img

        diff = blurred_img - self.background
        diff_abs = np.abs(diff)
        binary_image = diff_abs > self.threshold

        canny_edges = canny(resized_image, 50, 100)

        canny_edges = canny_edges * binary_image
        canny_edges = cv2.resize(canny_edges, (int(w), int(h)), interpolation=cv2.INTER_NEAREST)

        return canny_edges


def canny(img, thresh1, thresh2):
    img = cv2.Canny(img, thresh1, thresh2)
    return img