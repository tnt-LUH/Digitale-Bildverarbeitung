import cv2


def additive_color_plot(img):
    cv2.imshow("Additive", img)
    cv2.waitKey(0)


def subtractive_color_plot(img):
    img = 255 - img
    cv2.imshow("Subtractive", img)
    cv2.waitKey(0)
