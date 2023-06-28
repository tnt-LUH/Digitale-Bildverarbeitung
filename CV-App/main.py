"""
Main file for starting the CV-Application
More infos in the README.md file
"""

import argparse
import cv2
import platform
import numpy as np
import datetime

DEFAULT_CAMERA = 0
DEFAULT_MODE = "screen"  # "screen", "virtual_cam"
DEFAULT_VIDEO = "DEFAULT VIDEO TO SHOW"
WINDOW_NAME = "Output"
FRAMERATE = 30

'''
The following code is to setup the framework
'''
print("=== INITIALIZE FRAMEWORK === ")

# Read input arguments
parser = argparse.ArgumentParser(description='CV-App to demonstrate basic CV algorithms in a usefull application')
parser.add_argument(
    '--camera', type=int, default=DEFAULT_CAMERA, help='The camera to be opened by the app')
parser.add_argument(
    '--mode', type=str, default=DEFAULT_MODE, help="Either 'virtual_cam' for camera emulation or 'screen' for testing")
parser.add_argument(
    '--video', type=str, default=DEFAULT_VIDEO, help="The video to use if no camera is available")

args = parser.parse_args()

# Check if arguments are valid
available_cameras = list()
print("Availlable cameras:")
for i in range(3):
    temp = cv2.VideoCapture(i)
    is_opened = temp.isOpened()
    if is_opened:
        available_cameras.append(i)
        print("    camera with id", i)
    temp.release()
assert args.mode in ["screen", "virtual_cam"], "Wrong mode selected! '%s' is not existing!" % args.mode
assert args.camera in available_cameras or args.camera == -1, "Wrong cam selected! '%s' is not existing!" % args.camera

# Get current OS and import camera emulator software (skip if mode=='screen' is used)
current_os = platform.system()
print("Working on ", current_os)
if args.mode == "screen":
    def show(img):
        cv2.imshow(WINDOW_NAME, img)
elif current_os == "Darwin":
    raise NotImplementedError
elif current_os == "Linux":
    raise NotImplementedError
elif current_os == "Windows":
    import pyvirtualcam
    cam = None

    def show(img):
        global cam
        if cam is None:
            h, w, c = img.shape
            cam = pyvirtualcam.Camera(width=w, height=h, fps=20)
        if len(img.shape) == 2:
            img = np.stack([img, img, img], axis=2)
        cv2.imshow(WINDOW_NAME, img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cam.send(img)
        cam.sleep_until_next_frame()

else:
    raise Exception("OS %s not known!" % current_os)

# Define CV algorithms you want to use in the application
from algorithms import algorithms

current_algorithm_id = sorted(algorithms.keys())[0]
current_algorithm = algorithms[current_algorithm_id]()
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, current_algorithm.mouse_callback)

print("=== FINISHED INITIALIZING FRAMEWORK === \n\n")


'''
Following code runs the processing loop
'''
print("=== RUN PROCESSING LOOP === ")
input_source = args.camera if args.camera != -1 else args.video
print("Using input source", input_source)
cap = cv2.VideoCapture(input_source)
last_read = datetime.datetime.now()
auto_focus = True
auto_exposure = True
while True:
    # Measure time to last read out to avoid to fast readout in videos
    if datetime.datetime.now() - last_read < datetime.timedelta(milliseconds=int(1000 / FRAMERATE)):
        continue
    last_read = datetime.datetime.now()
    # Read, process and show image
    ret, img = cap.read()
    if not ret and type(input_source) == str:
        cap = cv2.VideoCapture(input_source)
        ret, img = cap.read()
    img = current_algorithm.process(img)
    show(img)
    # Check if a new
    key = cv2.waitKey(1)
    if key == -1:
        continue
    elif key == 27:
        cap.release()
        break
    elif chr(key) in algorithms.keys():
        current_algorithm_id = chr(key)
        current_algorithm = algorithms[current_algorithm_id]()
        print("Set algorithm to %s selected by key '%s'" % (type(current_algorithm), chr(key)))
        cv2.setMouseCallback(WINDOW_NAME, current_algorithm.mouse_callback)
    elif chr(key) == "e" and type(input_source) == int:
        auto_exposure = not auto_exposure
        print("Set auto exposure to", int(auto_exposure))
        cap.set(propId=cv2.CAP_PROP_AUTO_EXPOSURE, value=int(auto_exposure))
    elif chr(key) == "f" and type(input_source) == int:
        auto_focus = not auto_focus
        print("Set auto focus to", int(auto_focus))
        cap.set(propId=cv2.CAP_PROP_AUTOFOCUS, value=int(auto_focus))

print("=== FINISHED PROCESSING LOOP AND STOP APPLICATION === ")

