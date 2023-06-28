

class Algorithm:
    """ An abstract class to create custom algorithms """
    def process(self, img):
        """ Processes the input image"""
        return img

    def mouse_callback(self, event, x, y, flags, param):
        """ Reacts on mouse callbacks """
        return


''' Import algorithms to use'''
from .image_to_gray import ImageToGray
from .image_to_hue import ImageToHue
from .motion_detector import MotionDetector
from .white_balancing import WhiteBalancing
from .spin import Spin
from .segmentation_tracker import SegmentationTracker
#from .object_detection import ObjectDetector
#from .bottle_detection import BottleDetector
from .invis_cloak import InvisCloak
from .canny_edges import CannyEdgeDetector

''' Link Algorithms to keys '''
algorithms = dict()
algorithms["0"] = Algorithm
algorithms["1"] = ImageToGray
algorithms["2"] = ImageToHue
algorithms["3"] = MotionDetector
algorithms["4"] = WhiteBalancing
algorithms["5"] = Spin
algorithms["6"] = SegmentationTracker
algorithms["7"] = InvisCloak
#algorithms["7"] = ObjectDetector
#algorithms["8"] = BottleDetector
algorithms["9"] = CannyEdgeDetector
