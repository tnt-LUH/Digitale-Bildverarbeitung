"""
Many thanks to https://github.com/vardanagarwal/Proctoring-AI/blob/master/coco models/tflite mobnetv1 ssd
"""


import cv2
import numpy as np
import multiprocessing
import threading
import os
from copy import copy
from time import sleep

from . import Algorithm

""" Check if neural network accelerator is existing """
try_edgetpu = True
try:
    if not try_edgetpu:
        raise Exception()
    from pycoral.adapters import common
    from pycoral.adapters import detect
    from pycoral.utils.dataset import read_label_file
    from pycoral.utils.edgetpu import make_interpreter, list_edge_tpus
    if len(list_edge_tpus()) == 0:
        raise Exception()
    engine = "edgetpu"
except Exception as e:
    import tensorflow as tf
    engine = "tflite"


class Detector:
    def __init__(self):
        self.category_index = self.create_category_index()
        if engine == "tflite":
            self.num_threads = int(multiprocessing.cpu_count())
            print("Self using %s threads for object detection" % self.num_threads)
            self.interpreter = tf.lite.Interpreter(
                model_path="data" + os.sep + "ssd_mobilenet_v2_coco_quant_postprocess.tflite", num_threads=self.num_threads
            )
            self.interpreter.allocate_tensors()
            # Get input and output tensors.
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()
        elif engine == "edgetpu":
            print("Running with edge tpu")
            self.interpreter = make_interpreter("data" + os.sep + "ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite")
            self.interpreter.allocate_tensors()
            # Get input and output tensors.
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()

    def create_category_index(self, label_path='data' + os.sep + 'labelmap.txt'):
        f = open(label_path)
        category_index = {}
        for i, val in enumerate(f):
            if i != 0:
                val = val[:-1]
                category_index.update({(i - 1): {'id': (i - 1), 'name': val}})
        f.close()
        return category_index

    def get_output_dict(self, nms=True, iou_thresh=0.5, score_thresh=0.5):
        output_dict = {
            'detection_boxes': self.interpreter.get_tensor(self.output_details[0]['index'])[0],
            'detection_classes': self.interpreter.get_tensor(self.output_details[1]['index'])[0],
            'detection_scores': self.interpreter.get_tensor(self.output_details[2]['index'])[0],
            'num_detections': self.interpreter.get_tensor(self.output_details[3]['index'])[0]
        }
        output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
        output_dict["detection_classes_name"] = [self.category_index[x] for x in output_dict["detection_classes"]]
        if nms and engine == "tflite":
            output_dict = self.apply_nms(output_dict, iou_thresh, score_thresh)
        if nms and engine == "edgetpu":
            valid = np.where(output_dict["detection_scores"] >= score_thresh)[0]
            if valid.size == 0:
                output_dict = {}
            elif valid.size == 1:
                output_dict = {
                    'detection_boxes': output_dict["detection_boxes"][valid[0]:valid[0] + 1],
                    'detection_classes': output_dict["detection_classes"][valid[0]:valid[0] + 1],
                    'detection_scores': output_dict["detection_scores"][valid[0]:valid[0] + 1],
                    'detection_classes_name': output_dict["detection_classes_name"][valid[0]:valid[0] + 1],
                    'num_detections': 1,
                }
            else:
                output_dict = {
                    'detection_boxes': output_dict["detection_boxes"][valid],
                    'detection_classes': output_dict["detection_classes"][valid],
                    'detection_scores': output_dict["detection_scores"][valid],
                    'detection_classes_name': [x for i,x in enumerate(output_dict["detection_classes_name"]) if i in valid],
                    'num_detections': valid.size,
                }
        return output_dict

    def apply_nms(self, output_dict, iou_thresh=0.5, score_thresh=0.5):
        q = 90  # no of classes
        num = int(output_dict['num_detections'])
        boxes = np.zeros([1, num, q, 4])
        scores = np.zeros([1, num, q])
        # val = [0]*q
        for i in range(num):
            # indices = np.where(classes == output_dict['detection_classes'][i])[0][0]
            boxes[0, i, output_dict['detection_classes'][i], :] = output_dict['detection_boxes'][i]
            scores[0, i, output_dict['detection_classes'][i]] = output_dict['detection_scores'][i]
        nmsd = tf.image.combined_non_max_suppression(
            boxes=boxes, scores=scores, max_output_size_per_class=num, max_total_size=num, iou_threshold=iou_thresh,
            score_threshold=score_thresh, pad_per_class=False, clip_boxes=False
        )
        valid = nmsd.valid_detections[0].numpy()
        output_dict = {
            'detection_boxes': nmsd.nmsed_boxes[0].numpy()[:valid],
            'detection_classes': nmsd.nmsed_classes[0].numpy().astype(np.int64)[:valid],
            'detection_scores': nmsd.nmsed_scores[0].numpy()[:valid],
            'detection_classes_name': output_dict["detection_classes_name"][:valid]
        }
        return output_dict

    def make_inference(self, img, nms=True, score_thresh=0.5, iou_thresh=0.5):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb = cv2.resize(img_rgb, (300, 300), cv2.INTER_AREA)
        img_rgb = img_rgb.reshape([1, 300, 300, 3])
        self.interpreter.set_tensor(self.input_details[0]['index'], img_rgb)
        self.interpreter.invoke()
        output_dict = self.get_output_dict(nms, iou_thresh, score_thresh)
        return output_dict


class ObjectDetector(Algorithm):
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
                box = objects["detection_boxes"][i]
                score = objects["detection_scores"][i]
                name = cls["name"]
                y1, x1, y2, x2 = round(box[0] * h), round(box[1] * w), round(box[2] * h), round(box[3] * w)
                img = cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 0, 0), thickness=2)
                img = cv2.putText(img, "%s: %.2f" % (name, score), (x1, y1), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0))

        return img

    def _detect(self):
        detector = Detector()
        while True:
            with self.lock:
                img = self.detection_image
            if img is None:
                sleep(.033)
                continue
            objects = detector.make_inference(img)
            with self.lock:
                self.objects = objects
                self.detection_image = None

    def mouse_callback(self, event, x, y, flags, param):
        """ Selects a new seed point"""
        if event == cv2.EVENT_LBUTTONUP:
            pass

