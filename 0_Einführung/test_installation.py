import cv2
import matplotlib
import numpy as np
import platform

if cv2.__version__ and np.__version__ and matplotlib.__version__:
    print("Digital Image Processing is fun!")
    print("OpenCV version:", cv2.__version__)
    print("NumPy version:", np.__version__)
    print("Matplotlib version:", matplotlib.__version__)
    print("Python version:", platform.python_version())
else:
    print("OpenCV, NumPy and/or Matplotlib are not installed.")
