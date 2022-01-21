import cv2

""" Read images """
img1 = cv2.imread("data/kitti1.png")
img2 = cv2.imread("data/kitti2.png")
img3 = cv2.imread("data/kitti3.png")

cv2.imshow("Global-Shutter", img3)

""" Simulate rolling shutter"""
img3[0::3, :, :] = img1[0::3, :, :]
img3[1::3, :, :] = img2[1::3, :, :]

cv2.imshow("Rolling-Shutter", img3)

cv2.waitKey(0)