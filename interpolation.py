#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import numpy as np

# sys.argv[1] is input file
# sys.argv[2] is output file
data = json.load(open(sys.argv[1]))

# array of dict {"x" : 1.23, "y": 4.56}
points = data['points']

# array of x
predict = data['predict']

# TODO: construct matrix A and vector b
A = np.array([[]])
b = np.array([])

# TODO: get coefficients
x = np.array([])

# TODO: predict points
y = np.array([1, 2, 3, 4])

# write result to output file
json.dump([float(n) for n in y], open(sys.argv[2], 'w'))
