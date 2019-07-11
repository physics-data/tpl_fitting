#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import numpy as np

# sys.argv[1] is input file
# sys.argv[2] is output file
data = json.load(open(sys.argv[1]))

# [{"x": x, "y": y}, ...]
points = data["points"]

# [x, ...]
predict = data["predict"]

x = np.array([p["x"] for p in points])
y = np.array([p["y"] for p in points])

coeff = np.polyfit(x, y, 4)
curve = np.poly1d(coeff)

y_predict = [curve(x) for x in predict]

# write result to output file
json.dump([float(n) for n in y_predict], open(sys.argv[2], 'w'))
