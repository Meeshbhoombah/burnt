#!/usr/bin/env python

"""burnt.py"""


import cv2
import sys

def rename(filename, type = None):
    """Takes in a filepath and outputs the filepath with the renamed output file"""
    output_elements = filename.split('.')

    if type is None:
        print("-*- BUILDING OUTPUT FILEPATH -*-")
        output_elements.insert(1, "_resized")
        output_elements.insert(2, ".")
        return ''.join(output_elements) 


def main(args):

    # TODO -: fix index for executeables
    filename = args[1]

    # CLI arguments passed in as string
    grid_X = int(args[2])
    grid_Y = int(args[3])
  
    cap = cv2.VideoCapture(filename)
    # open video at filepath and attempt to read first
    # frame of the video
    success, image = cap.read()

    if not success:
        print("Could not read file at given file path.")
    
    # file exists and could read, create output path to
    # release resized image as a sequence
    out_path = rename(filename)
    out = cv2.VideoWriter(out_path)
        
    while success:
        resized = cv2.resize(image, (grid_X, grid_Y), interpolation = cv2.INTER_LINEAR)
        out.write(resized) 


if __name__ == "__main__":
    args = sys.argv
    main(args)

