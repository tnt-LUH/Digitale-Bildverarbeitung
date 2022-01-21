import cv2

""" Read images """
img1 = cv2.imread("data/kitti1.png")
img2 = cv2.imread("data/kitti2.png")
img3 = cv2.imread("data/kitti3.png")

cv2.imshow("Global-Shutter", img3)

cv2.waitKey(0)