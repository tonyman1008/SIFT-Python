import cv2
import numpy as np

GT_PATH = "./car-gt/"
IMG_PATH = "./20211125_GraphCut_SIFT_CustomMatch_DT255_ST150_OLP500/"
resizeFactor = 1.5

IS_RESIZE = False


def preLoadImg():
    imgAry = []
    gtImgAry = []
    labelImgAry = []
    sourceImgAry = []
    sinkImgAry = []
    concatImgAry = []

    for index in range(0, 360):
        img = cv2.imread(IMG_PATH+str(index) +
                         "/stitchImage.png", cv2.IMREAD_COLOR)
        gtImg = cv2.imread(GT_PATH+str(index)+".png", cv2.IMREAD_COLOR)
        label = cv2.imread(IMG_PATH+str(index)+"/label.png", cv2.IMREAD_COLOR)
        # source = cv2.imread(IMG_PATH+str(index) +
        #                     "/source.png", cv2.IMREAD_COLOR)
        # sink = cv2.imread(IMG_PATH+str(index)+"/sink.png", cv2.IMREAD_COLOR)

        if IS_RESIZE:
            img = resizeImg(img)
            gtImg = resizeImg(gtImg)
            label = resizeImg(label)
            # source = resizeImg(source)
            # sink = resizeImg(sink)

        imgAry.append(img)
        gtImgAry.append(gtImg)
        labelImgAry.append(label)
        # sourceImgAry.append(source)
        # sinkImgAry.append(sink)

        concatImg = cv2.hconcat([gtImg, img])

        cv2.putText(concatImg, str(index), (100, 150), cv2.FONT_HERSHEY_DUPLEX,
                    5, (255, 0, 0), 5, cv2.LINE_AA)
        concatImgAry.append(concatImg)

    return imgAry, gtImgAry, labelImgAry, concatImgAry
    # return imgAry, gtImgAry, labelImgAry, sourceImgAry, sinkImgAry, concatImgAry


def resizeImg(img):
    height, width = img.shape[0], img.shape[1]
    width_new = width / resizeFactor
    height_new = height / resizeFactor

    resizeImg = cv2.resize(img, (int(width_new), int(height_new)),
                           interpolation=cv2.INTER_AREA)
    return resizeImg


frameIndex = 0

imgAry = []
gtImgAry = []
labelImgAry = []
sourceImgAry = []
sinkImgAry = []
concatImgAry = []

cv2.namedWindow("Frame Viewer")

# imgAry, gtImgAry, labelImgAry, sourceImgAry, sinkImgAry, concatImgAry = preLoadImg()
imgAry, gtImgAry, labelImgAry, concatImgAry = preLoadImg()

while True:
    cv2.imshow('Frame Viewer', concatImgAry[frameIndex])

    keyDown = cv2.waitKey(0) & 0xff

    if keyDown == ord("z") and frameIndex-1 >= 0:
        frameIndex -= 1

    elif keyDown == ord("c") and frameIndex+1 < 360:
        frameIndex += 1

    elif keyDown == ord("q"):
        break
