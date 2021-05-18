import cv2

from . import Algorithm


class TutorialAlgorithm(Algorithm):
    """ Writes the RGB values of an pixel to the output image """

    def __init__(self):
        """ Init reference point with None value """
        self.pos = None

    def process(self, img):
        """
        Reads out the RGB values of the reference point and writes it to the output image
        """
        if self.pos is not None:
            pixel = img[self.pos[1], self.pos[0]]
            text = "x:%s y:%s R:%s G:%s B:%s" % (self.pos[0], self.pos[1], pixel[2], pixel[1], pixel[0])
        else:
            text = "Click on the image!"
        font, org, font_scale, color, thickness = cv2.FONT_HERSHEY_SIMPLEX, (50, 50), 1, (0, 0, 0), 2
        image = cv2.putText(img, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

        return image

    def mouse_callback(self, event, x, y, flags, param):
        """ Selects a new reference position"""
        if event == cv2.EVENT_LBUTTONUP:
            self.pos = (x, y)

