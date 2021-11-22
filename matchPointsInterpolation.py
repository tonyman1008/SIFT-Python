import json
import os

with open('car-unity-output-matchPoints/PotionData_60vertices_72view_5degDiff.json') as f:
    data = json.load(f)

outputJSON = {}
outputJSON["matchPointSeqData"] = []

for matchPointSeqDataAry in data["matchPointSeqData"]:
    for i in range(5):
        matchPointsAry = {}
        matchPointsAry["matchPoints"] = []
        for pointsPair in matchPointSeqDataAry["matchPoints"]:
            interFactor = i/5

            point1X = pointsPair["keyPointOne"][0]
            point1Y = pointsPair["keyPointOne"][1]
            point2X = pointsPair["keyPointTwo"][0]
            point2Y = pointsPair["keyPointTwo"][1]

            pointInterX = point1X * (1-interFactor) + point2X*interFactor
            pointInterY = point1Y * (1-interFactor) + point2Y*interFactor

            interPointsPair = {}
            interPointsPair["keyPointOne"] = []
            interPointsPair["keyPointTwo"] = []

            interPointsPair["keyPointOne"].append(pointInterX)
            interPointsPair["keyPointOne"].append(pointInterY)
            interPointsPair["keyPointTwo"].append(pointInterX)
            interPointsPair["keyPointTwo"].append(pointInterY)
            matchPointsAry["matchPoints"].append(interPointsPair)

        outputJSON["matchPointSeqData"].append(matchPointsAry)


outputPath = (
    "InterpolationMatchPoints/"
)

with open(
    outputPath + "InterpolationMatchPoints.json",
    "w",
) as jsonfile:
    json.dump(outputJSON, jsonfile)
