import cv2  # Import OpenCV
import numpy as np
import os
import json
from numpy.core.numeric import count_nonzero  # Import NumPy

DATA_SET_NAME = "car_1000x1000"
IMG_PATH = "assets/"+DATA_SET_NAME+"/"
IMG1_NAME = "0.png"

img_origin = cv2.imread(IMG_PATH + IMG1_NAME, cv2.IMREAD_UNCHANGED)
img = cv2.imread(IMG_PATH + IMG1_NAME, cv2.IMREAD_UNCHANGED)
rows, cols = img.shape[:2]
for i in range(rows):
    for j in range(cols):
        intensity = img[i, j][3]
        if intensity < 250:
            img[i, j][:3] = [0, 0, 0]
        else:
            img[i, j][:3] = [255, 255, 255]


img2 = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# Run findContours - Note the RETR_EXTERNAL flag
# Also, we want to find the best contour possible with CHAIN_APPROX_NONE
_, contours, hierarchy = cv2.findContours(
    img2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)

outputPath = (
    "Contour2DPoints/" + DATA_SET_NAME + "/" +
    IMG1_NAME.split(".")[0] + "/"
)
outputJSON = {}
outputJSON["contourPoints"] = []

# Create an output of all zeroes that has the same shape as the input
# image
out = np.zeros_like(img2)
outLineContour = np.copy(contours[0])
print("all contour len", len(contours))
print("specific contour len", len(outLineContour))
for i in range(len(outLineContour)):
    x = outLineContour[i][0][0]
    y = outLineContour[i][0][1]
    if i % 15 == 0:
        cv2.circle(img_origin, (x, y), 3, (0, 0, 255), -1)
        contourPoint = {
            "x": int(x),
            "y": int(y)
        }
        outputJSON["contourPoints"].append(contourPoint)

if not os.path.exists(outputPath):
    os.makedirs(outputPath)

with open(
    outputPath + "ContourPoints.json",
    "w",
) as jsonfile:
    json.dump(outputJSON, jsonfile)

# On this output, draw all of the contours that we have detected
# in white, and set the thickness to be 3 pixels
cv2.drawContours(out, contours, 0, 255, 3)

# Spawn new windows that shows us the donut
# (in grayscale) and the detected contour

cv2.namedWindow("gray")

cv2.imshow("origin", img_origin)
cv2.imshow("gray", img2)
cv2.imshow("Output Contour", out)


def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        _intensity = img2[y, x]
        print(_intensity[3])


cv2.setMouseCallback("gray", mouse_callback, 1)

# Wait indefinitely until you push a key.  Once you do, close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
