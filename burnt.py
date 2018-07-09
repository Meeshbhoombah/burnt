#!/usr/bin/env python

"""burnt.py"""


import cv2
import sys


class Burnt:
    """Creates a """

def rename(filename, type = None):
    """Takes in a filepath and outputs the filepath with the renamed output file"""
    output_elements = filename.split('.')

    if type is None:
        print("-*- BUILDING OUTPUT FILEPATH -*-")
        output_elements.insert(1, "_resized.")
        return ''.join(output_elements) 


def main(args):

    # TODO -: fix index for executeables
    filename = args[1]

    # CLI arguments passed in as string
    grid_X = int(args[2])
    grid_Y = int(args[3])
    

    # open video at filepath
    cap = cv2.VideoCapture(filename)
    # attempt to read first frame of the video
    success, image = cap.read()

    if not success:
        print("Could not read file at given file path.")
    
    # if file exists and read is success, create output 
    # path to release resized image as a sequence
    out_path = rename(filename)

    
    out = cv2.VideoWriter(out_path, 0, 0x415A5052, 1, (grid_X, grid_Y))
        
    while success:
        resized = cv2.resize(image, fx=0.5, fy=0.5, interpolation = cv2.INTER_LANCZOS4)
        out.write(resized) 


if __name__ == "__main__":
    args = sys.argv
    main(args)

