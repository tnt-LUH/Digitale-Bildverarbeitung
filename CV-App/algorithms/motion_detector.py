import cv2
import numpy as np


from . import Algorithm


class MotionDetector(Algorithm):
    """ Converts a BGR image to grayscale"""
    def __init__(self):
        self.image_count = 0
        self.background = None
        self.motion_field = None
        self.background_update_rate = 0.5
        self.motion_update_rate = 0.3
        self.threshold = 50

    def process(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = img_gray.shape
        blurred_img = cv2.resize(img_gray, (int(w/2), int(h/2)), interpolation=cv2.INTER_NEAREST)
        blurred_img = cv2.GaussianBlur(blurred_img, (15, 15), 0)

        if self.background is None:
            self.background = blurred_img
            self.motion_field = np.zeros_like(blurred_img)

        self.background = (1 - self.background_update_rate) * self.background + self.background_update_rate * blurred_img

        diff = blurred_img - self.background
        diff_abs = np.abs(diff)
        diff_rel = np.clip(diff_abs, 0, self.threshold) / self.threshold
        self.motion_field = (1 - self.motion_update_rate) * self.motion_field + self.motion_update_rate * diff_rel

        motion_field = cv2.resize(self.motion_field, (w, h), interpolation=cv2.INTER_NEAREST)
        motion_field = np.expand_dims(motion_field, 2)

        colormap = cv2.applyColorMap((motion_field * 255).astype(np.uint8), cv2.COLORMAP_HOT)
        img_gray = np.stack([img_gray, img_gray, img_gray], axis=2)
        final_image = 0.5 * img_gray * (1 - motion_field) + colormap * motion_field
        final_image = final_image.astype(np.uint8)

        self.image_count += 1

        return final_image
