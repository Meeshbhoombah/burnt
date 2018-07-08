#!/usr/bin/env python

"""burnt.py"""


import cv2
import sys


GRID_X = 12
GRID_Y = 12 # ratio of the y to the x
# make it scaleable


def main(args):

    # TODO -: fix index for executeable
    filename = args[1]
  
    cap = cv2.VideoCapture(filename)
    # reads first frame of video if it exists
    success, image = cap.read()

    if not success:
        print("Could not read file at given file path.")

    while success:
        resized = cv2.resize(image, (GRID_X, GRID_Y) interpolation=cv2.LINEAR)
   
    output_filename = filename.split('.')
    output_filename.insert(1, "_resized")
    
    #output = cv2.VideoWriter(


if __name__ == "__main__":
    args = sys.argv
    main(args)

