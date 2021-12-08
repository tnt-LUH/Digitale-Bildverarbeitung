"""
Many thanks to https://github.com/vardanagarwal/Proctoring-AI/blob/master/coco models/tflite mobnetv1 ssd
"""


import cv2
import numpy as np
import threading
from copy import copy
from time import sleep

from . object_detection import Detector
from . import Algorithm


class BottleDetector(Algorithm):
    """ Detects objects """

    def __init__(self):
        """ Init some values and set seed point to None """
        self.objects = dict()
        self.detection_image = None
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self._detect, args=[], daemon=True)
        self.thread.start()

    def process(self, img):
        """
        Tries to segment a region around the seed point and calculates a new seed point by finding the segments center
        """
        with self.lock:
            if self.detection_image is None:
                self.detection_image = np.copy(img)
        with self.lock:
            objects = copy(self.objects)
        h, w, c = img.shape

        if "detection_classes_name" in objects.keys():
            for i, cls in enumerate(objects["detection_classes_name"]):
                name = cls["name"]
                if name in ["bottle", "cup"]:
                    box = objects["detection_boxes"][i]
                    score = objects["detection_scores"][i]
                    y1, x1, y2, x2 = \
                        max(round(box[0] * h) - 20, 0), round(box[1] * w) - 20 ,\
                        max(round(box[2] * h) + 20, 0), round(box[3] * w) + 20
                    if img[y1:y2, x1:x2].size > 0:
                        img[y1:y2, x1:x2] = cv2.medianBlur(img[y1:y2, x1:x2], 31)

        return img.astype(np.uint8)

    def _detect(self):
        detector = Detector()
        while True:
            with self.lock:
                img = self.detection_image
            if img is None:
                sleep(.033)
                continue
            objects = detector.make_inference(img, score_thresh=0.1)
            with self.lock:
                self.objects = objects
                self.detection_image = None

    def mouse_callback(self, event, x, y, flags, param):
        """ Selects a new seed point"""
        if event == cv2.EVENT_LBUTTONUP:
            pass

