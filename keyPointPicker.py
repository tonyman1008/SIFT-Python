import cv2
import json
import os
import numpy as np

DATA_SET_NAME = "bag4"
IMG_PATH = "assets/"+DATA_SET_NAME+"/"
IMG1_NAME = "frame0.png"
IMG2_NAME = "frame2.png"

img1 = cv2.imread(IMG_PATH + IMG1_NAME, cv2.IMREAD_COLOR)
img2 = cv2.imread(IMG_PATH + IMG2_NAME, cv2.IMREAD_COLOR)

# resize
resizeFactor = 2
height, width = img1.shape[0], img1.shape[1]

width_new = width / resizeFactor
height_new = height / resizeFactor

img1 = cv2.resize(img1, (int(width_new), int(height_new)),
                  interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2, (int(width_new), int(height_new)),
                  interpolation=cv2.INTER_AREA)

# create 2 windows
cv2.namedWindow("img1")
cv2.namedWindow("img2")

ImgPickingIndex = 1
tempKeyPointOne = []
tempKeyPointTwo = []

outputData = {}
outputData["matchPoints"] = []
onePairMatchComplete = False

outputPath = (
    "MatchPointsData/" + DATA_SET_NAME + "/" +
    IMG1_NAME.split(".")[0] + "&" + IMG2_NAME.split(".")[0] + "/"
)

# this function will be called whenever the mouse is right-clicked


def mouse_callback(event, x, y, flags, params):

    # right-click event value is 2
    if event == cv2.EVENT_LBUTTONDOWN:
        global outputData
        global onePairMatchComplete
        global ImgPickingIndex
        global tempKeyPointOne
        global tempKeyPointTwo

        # check the picking index now
        if params != ImgPickingIndex:
            return

        print(ImgPickingIndex)

        if params == 1:
            cv2.circle(img1, (x, y), 4, (255, 0, 0), 2)
            print([x, y])

            tempKeyPointOne = [x*resizeFactor, y*resizeFactor]
            ImgPickingIndex = 2
        elif params == 2:
            # visualize
            cv2.circle(img2, (x, y), 4, (255, 0, 0), 2)
            print([x, y])

            # store a record
            tempKeyPointTwo = [x*resizeFactor, y*resizeFactor]
            ImgPickingIndex = 1

            # a pair data complete
            matchPoint = {
                "keyPointOne": list(tempKeyPointOne),
                "keyPointTwo": list(tempKeyPointTwo),
            }
            tempKeyPointTwo.clear()
            tempKeyPointOne.clear()
            outputData["matchPoints"].append(matchPoint)

            if not os.path.exists(outputPath):
                os.makedirs(outputPath)

            with open(
                outputPath + "MatchPoints.json",
                "w",
            ) as jsonfile:
                json.dump(outputData, jsonfile)

            img_concat = cv2.hconcat([img1, img2])
            cv2.imwrite(outputPath + "MatchPoints.jpg", img_concat)


# set mouse callback function for window
cv2.setMouseCallback("img1", mouse_callback, 1)
cv2.setMouseCallback("img2", mouse_callback, 2)

while True:
    # both windows are displaying the same img
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
