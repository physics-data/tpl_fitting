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
matrix = []
b = []
for point in points:
    x = point['x']
    y = point['y']
    matrix.append([x ** 4, x ** 3, x ** 2, x ** 1, 1])
    b.append(y)

A = np.array(matrix)
b = np.array(b).T

ATA = A.T.dot(A)
ATb = A.T.dot(b)

x = np.linalg.inv(ATA).dot(ATb)

# TODO: predict points
y = []
for pre in predict:
    xx = np.array([pre ** 4, pre ** 3, pre ** 2, pre ** 1, 1])
    y.append(xx.dot(x))

# write result to output file
json.dump([float(n) for n in y], open(sys.argv[2], 'w'))
