# -*- encoding: utf-8 -*-

"""trimmer.py
"""

import json
from pprint import pprint

with open('freespace.json') as f:
	data = json.load(f)

	for entry in data:
	# iterate over each point
		pprint(entry)
