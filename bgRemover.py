import cv2
import numpy as np

IMG_PATH = "assets/lv24p/"
IMG1_NAME = "LV_01.png"

img = cv2.imread(IMG_PATH + IMG1_NAME, cv2.IMREAD_COLOR)


## (1) Convert to gray, and threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

## (2) Morph-op to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)


## (3) Find the max-area contour
cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
cnt = sorted(cnts, key=cv2.contourArea)[-1]


## (4) Crop and save it
x, y, w, h = cv2.boundingRect(cnt)
dst = img[y : y + h, x : x + w]
cv2.imwrite("001.png", dst)
cv2.imshow("dst", dst)

cv2.waitKey()