#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import numpy as np

# sys.argv[1] is input file
# sys.argv[2] is output file
data = json.load(open(sys.argv[1]))

# TODO: get array of known points data
points = data[?]

# TODO: get array of points to predict
predict = data[?]

# TODO: construct matrix A and vector b
A = np.array([[]])
b = np.array([])

# TODO: calculate coefficients of the 4-order curve wth least square method
x = np.array([])

# TODO: predict points
y = np.array([1, 2, 3, 4])

# write result to output file
json.dump([float(n) for n in y], open(sys.argv[2], 'w'))
