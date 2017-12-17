#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0039

https://projecteuler.net/problem=39

Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math
import sys

PROBLEM = 39
SOLVED = True
SPEED = 5.74
TAGS = ['pythagorean']


def triangles(perimeter):
    """Calculate how many different right triangles can be made with integral length sides."""
    solutions = 0
    for left in xrange(1, int(perimeter / (2 + math.sqrt(2))) + 1):
        for right in xrange(left, (perimeter - left) / 2 + 1):
            if left ** 2 + right ** 2 == (perimeter - left - right) ** 2:
                solutions += 1
                # print 'Perimeter=%d, a=%d, b=%d, c=%d' % (perimeter, left, right, perimeter-left-right)
    return solutions

def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])
    maximum += 1
    solutions = []
    for target in xrange(12, maximum):
        solutions.append(triangles(target))
    largest = max(solutions)
    print solutions.index(largest) + 12, largest


if __name__ == '__main__':
    main()
