import cv2
import numpy as np

img = cv2.imread("../../data/car.png")
cv2.imshow("Car", img)

print("Image Shape:", img.shape)


print("\nForward-Mapping")
new_image = np.zeros((int(img.shape[0] / 2), int(img.shape[1] / 2), img.shape[2]), dtype=np.uint8)

for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        new_image[int(y/2), int(x/2)] = img[y, x]

cv2.imshow("Forward-Mapping", new_image)
print("Pixel at position x=12, y=38", new_image[38, 12])


print("\nBackward-Mapping")
# Inverse Transformation:
# (x, y)^T  =  ([2, 0]  * (x', y')^T
#               [0, 2])

p_12_38 = img[38*2, 12*2]
print("Pixel at position x=12, y=38", p_12_38)

cv2.waitKey(0)