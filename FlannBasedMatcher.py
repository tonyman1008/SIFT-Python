import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
import json

DATA_SET_NAME = "lv24p"
IMG_PATH = "assets/"+DATA_SET_NAME+"/"
IMG1_NAME = "LV_01.png"
IMG2_NAME = "LV_02.png"

img1 = cv2.imread(IMG_PATH + IMG1_NAME, cv2.IMREAD_COLOR)
img2 = cv2.imread(IMG_PATH + IMG2_NAME, cv2.IMREAD_COLOR)
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# find the keypoints and descriptors with SIFT
sift = cv2.xfeatures2d.SURF_create(800)
# sift = cv.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1_gray, None)
kp2, des2 = sift.detectAndCompute(img2_gray, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 2
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)  # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

outputData = {}
outputData["matchPoints"] = []

# ratio test as per Lowe’s paper
for i, (m, n) in enumerate(matches):
    # 如果第一個鄰近距離比第二個鄰近距離的0.7倍小，則保留
    if m.distance < 0.7 * n.distance:
        pt1 = kp1[m.queryIdx].pt  # trainIdx    是匹配之后所对应关键点的序号，第一个载入图片的匹配关键点序号
        pt2 = kp2[m.trainIdx].pt  # queryIdx  是匹配之后所对应关键点的序号，第二个载入图片的匹配关键点序号
        distY = abs(pt1[1] - pt2[1])
        distX = abs(pt1[0] - pt2[0])
        # print(distY)
        if distY < 15 and distX < 80:
            matchesMask[i] = [1, 0]
            # cv2.circle(img1, (int(pt1[0]), int(pt1[1])), 5, (255, 0, 255), -1)
            # cv2.circle(img2, (int(pt2[0]), int(pt2[1])), 5, (255, 0, 255), -1)
            # cv2.imshow("img1", img1)
            # cv2.imshow("img2", img2)
            # print(i, pt1, pt2)

            # dist = math.hypot(pt1[0] - pt2[0], pt1[1] - pt2[1])
            # print(dist)

            matchPoint = {
                "keyPointOne": pt1,
                "keyPointTwo": pt2,
            }
            outputData["matchPoints"].append(matchPoint)

            with open("MatchPointsData/SIFT/MatchPoints.json", "w") as jsonfile:
                json.dump(outputData, jsonfile)

    # Anchor (0,0), (x,y) is (left,top)
draw_params = dict(
    matchColor=(0, 255, 0),
    singlePointColor=(255, 0, 0),
    matchesMask=matchesMask,
    flags=0,
)
res = cv2.drawMatchesKnn(img1_gray, kp1, img2_gray,
                         kp2, matches, None, **draw_params)

# plt.imshow(res), plt.show()
cv2.imshow("Result", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
