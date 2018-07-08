# -*- encoding: utf-8 -*-

"""reduce.py"""

import json
from pprint import pprint

with open('/Users/meeshbhoombah/Desktop/burnt/data/man_face.json') as f:

    data = json.load(f)

    for entry in data:
        point_array = entry["point"]
        point_array[0] = point_array[0] / 4

    with open('/Users/meeshbhoombah/Desktop/burnt/data/man_face_reduce.json', 'w') as outfile:
        json.dump(data, outfile)
    

