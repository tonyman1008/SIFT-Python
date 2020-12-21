import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread("assets/dragon_noLight02.png", 0)
img2 = cv.imread("assets/dragon_noLight03.png", 0)

# Initiate SIFT detector
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches.
img3 = cv.drawMatches(
    img1,
    kp1,
    img2,
    kp2,
    matches[:10],
    None,
    flags=cv.DrawMatchesFlags_DEFAULT,
)

plt.imshow(img3), plt.show()
cv.waitKey(0)
