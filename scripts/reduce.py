#!/usr/bin/env python

import json
from pprint import pprint

with open('/Users/meeshbhoombah/Desktop/burnt/data/man_face.json') as f:

    data = json.load(f)

    for entry in data:
        point_array = entry["point"]
        point_array[0] = point_array[0] / 4
        point_array[2] = point_array[2] / 4

    with open('/Users/meeshbhoombah/Desktop/burnt/data/man_face_reduced.json', 'w') as outfile:
        json.dump(data, outfile)
    

