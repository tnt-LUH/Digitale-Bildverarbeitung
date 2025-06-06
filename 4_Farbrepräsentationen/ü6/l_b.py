import numpy as np

from color_code import subtractive_color_plot

img = np.zeros((300, 500, 3), dtype=np.uint8)

img[0:50, 0:500] = [255, 255, 0]
img[50:100, 0:500] = [255, 119, 0]
img[100:150, 0:500] = [255, 0, 0]
img[150:200, 0:500] = [255, 0, 255]
img[200:250, 0:500] = [0, 255, 255]
img[250:300, 0:500] = [0, 255, 119]

subtractive_color_plot(img)
