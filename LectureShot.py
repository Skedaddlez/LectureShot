from PIL import Image
import cv2
import os
import ffmpeg
import glob
import sys
import numpy as np
import argparse
import imutils
from skimage.measure import compare_ssim
import math


videoname = input("Video filename (include extension) = ")
vidcap = cv2.VideoCapture(videoname)
success, image = vidcap.read()
cv2.imwrite("temp/frame1.png", image)  # save frame as JPEG file
count = 1
wait = 0
while success:
    success, image2 = vidcap.read()
    print('Read frame', success)
    wait+=1
    if wait == 125:
        ssimval = compare_ssim(image, image2, multichannel=True)
        print("SSIM: {}".format(ssimval))
        if ssimval < 0.95:
            count += 1
            cv2.imwrite("temp/frame%d.png" % count, image2)  # save frame as JPEG file
            image = image2
        wait = 0
