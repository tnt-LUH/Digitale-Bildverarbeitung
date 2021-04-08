import cv2
import numpy as np

from . import Algorithm


class SegmentationTracker(Algorithm):
    """ Tracks a point by re-identify a suitable segmentation  """

    def __init__(self):
        """ Init some values and set seed point to None """
        self.pos = None
        self.distance_threshold = 80
        self.reference_pixel = None

    def process(self, img):
        """
        Tries to segment a region around the seed point and calculates a new seed point by finding the segments center
        """
        if self.pos is None:
            result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            result = np.stack([result, result, result], axis=2)
            return result
        h, w, c = img.shape

        if self.reference_pixel is None:
            self.reference_pixel = np.copy(img[self.pos[1], self.pos[0]])
        pixel_low,  pixel_high = \
            np.maximum(0, self.reference_pixel-self.distance_threshold),\
            np.minimum(255, self.reference_pixel+self.distance_threshold)
        binary = cv2.inRange(img, pixel_low, pixel_high)

        element = np.ones((5, 5), dtype=np.uint8)
        binary = cv2.erode(binary, element)
        binary = cv2.dilate(binary, element)
        sure_background = binary
        sure_foreground = np.zeros_like(sure_background)
        x, y = max(2, self.pos[0]), max(2, self.pos[1])
        sure_foreground[y-2:y+2, x-5:x+2] = 1
        unknown = np.maximum(0, sure_background - sure_foreground)

        ret, markers = cv2.connectedComponents(sure_foreground)
        # Add one to all labels so that sure background is not 0, but 1
        markers = markers + 1
        # Now, mark the region of unknown with zero
        markers[unknown == 255] = 0
        markers = cv2.watershed(img, markers)

        try:
            contours, hierarchy = cv2.findContours(((markers == 2) * 1).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            c = contours[0]
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            self.pos = (min(cX, w-1), min(cY, h-1))
        except:
            pass

        result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = np.stack([result, result, result], axis=2)
        random_noise = np.random.randint(0, 255, (h, w), dtype=np.uint8)
        random_noise = cv2.applyColorMap(random_noise, colormap=cv2.COLORMAP_INFERNO)
        result[markers == 2] = random_noise[markers == 2]
        return result

    def mouse_callback(self, event, x, y, flags, param):
        """ Selects a new seed point"""
        if event == cv2.EVENT_LBUTTONUP:
            self.pos = (x, y)
            self.reference_pixel = None

