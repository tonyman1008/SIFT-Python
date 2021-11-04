import os
import shutil


for i in range(256, 257):
    if i % 5 != 0:
        shutil.move("./test/{}-result/backward0.wrapped.png".format(i),
                    "./RenameSource/{}.png".format(i))
        shutil.move("./test/{}-result/backward1.wrapped.png".format(i),
                    "./RenameSink/{}.png".format(i))
