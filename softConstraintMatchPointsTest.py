import json
import os

outputJSON = {}
outputJSON["matchPointSeqData"] = []

for k in range(0, 360):

    # skip
    if k % 5 == 0:
        outputJSON["matchPointSeqData"].append({"matchPoints": []})
        continue

    with open('softConstraintTest/forward/{}.json'.format(k)) as forwardFile:
        dataForward = json.load(forwardFile)
    with open('softConstraintTest/backward/{}.json'.format(k)) as backwardFile:
        dataBackward = json.load(backwardFile)

    matchPointsAry = {}
    matchPointsAry["matchPoints"] = []

    for i in range(0, len(dataForward)):
        keyPointOneX = dataForward[i]["x"]
        keyPointOneY = dataForward[i]["y"]

        keyPointTwoX = dataBackward[i]["x"]
        keyPointTwoY = dataBackward[i]["y"]

        newMatchPoint = {}

        newMatchPoint["keyPointOne"] = []
        newMatchPoint["keyPointOne"].append(keyPointOneX)
        newMatchPoint["keyPointOne"].append(keyPointOneY)

        newMatchPoint["keyPointTwo"] = []
        newMatchPoint["keyPointTwo"].append(keyPointTwoX)
        newMatchPoint["keyPointTwo"].append(keyPointTwoY)

        matchPointsAry["matchPoints"].append(newMatchPoint)

    outputJSON["matchPointSeqData"].append(matchPointsAry)

outputPath = (
    "softConstraintTest/"
)

with open(
    outputPath + "softConstraintMatchPointsTest.json",
    "w",
) as jsonfile:
    json.dump(outputJSON, jsonfile)
