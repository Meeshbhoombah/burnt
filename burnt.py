#!/usr/bin/env python

"""burnt.py"""


import cv2
import sys


def main(args):

    filename = args[0]

    # convert the video input to a workable OpenCV object
    cap = cv2.VideoCapture(filename)


if __name__ == "__main__":
    print(sys.argvs)

