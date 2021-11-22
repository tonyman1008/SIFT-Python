import os
import shutil


INPUT_PATH = "./20211110_NISwGSP_FineTuneTest/0_results/"
OUTPUT_BACKWARD_PATH = "./20211110_NISwGSP_FineTuneTest_Backward/"
OUTPUT_FORWARD_PATH = "./20211110_NISwGSP_FineTuneTest_Forward/"

# copy niswgsp stitching result
for i in range(0, 360):
    if i % 5 != 0:
        shutil.copy(INPUT_PATH+"{}-result/backward.warpped.png".format(i),
                    OUTPUT_BACKWARD_PATH+"{}.png".format(i))
        shutil.copy(INPUT_PATH+"{}-result/forward.warpped.png".format(i),
                    OUTPUT_FORWARD_PATH+"{}.png".format(i))

# copy ARAP result
for i in range(0, 360):
    if i % 5 == 0:
        shutil.copy("20211004_ARAP/backward/{}.png".format(i),
                    OUTPUT_BACKWARD_PATH+"{}.png".format(i))
        shutil.copy("20211004_ARAP/forward/{}.png".format(i),
                    OUTPUT_FORWARD_PATH+"{}.png".format(i))
