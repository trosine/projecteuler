#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0018

https://projecteuler.net/problem=18

Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

  75
95  64
...

NOTE:

As there are only 16384 routes, it is possible to solve this problem by trying
every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""

import sys

PROBLEM = 18
SOLVED = True
SPEED = 0.02
TAGS = ['max_path_sum']


def load_data(filename):
    """Returns the triangular dataset *inverted* and converted to integers"""
    data = []
    with open(filename) as datafile:
        for line in datafile.readlines():
            data.insert(0, map(int, line.strip().split()))
    return data


# Starting from the bottom of the triangle, each data point calculates its own
# result which is self + max(the two below me). This way, there's no need to
# calculate all of the possible paths
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    filename = 'fixtures/d%04d.txt' % (PROBLEM)
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    data = load_data(filename)
    for row in xrange(1, len(data)):
        for col in xrange(len(data[row])):
            data[row][col] += max(data[row-1][col:col+2])
    print data[-1][0]


if __name__ == '__main__':
    main()
