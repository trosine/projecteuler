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
SPEED = 0.03
TAGS = ['pythagorean']


def triangles(perimeter):
    """Calculate how many different right triangles can be made with integral length sides."""
    solutions = 0
    maximum = int(perimeter / (2 + math.sqrt(2)))
    for side in xrange(1, maximum + 1):
        if perimeter * (perimeter - 2*side) % (2 * (perimeter - side)) == 0:
            solutions += 1
    return solutions


# This implementation is largely based on rayfil's post.
# First, only even perimeters are valid:
#   A even number * even number => even number (even² => even).
#   An odd number * odd number => odd number (odd² => odd).
#   even + even = even => even perimeter
#   even + odd = odd => even perimeter
#   odd + odd = even => even perimeter
# Second, we can remove the hypotenuse and simply calculate possible a, b sides.
#   a + b + c = P
#   c = P - a - b
#   a² + b² = (P - a - b)²   ; solve for b
#           = (P - a - b)(P - a - b)
#           = P² - aP - bP - aP + a² + ab - bP + ab + b²  ; a² and b² cancel
#   0 = P² - 2aP - 2bP + 2ab
#   2bP - 2ab = P² - 2aP
#   bP - ab = (P² - 2aP) / 2
#   b(P - a) = P(P - 2a) / 2
#   b = P (P - 2a) / 2(P-a)
# Third, from my own calculation, the maximum value for a is when a=b.
# when a = b, c² = 2a²
# P = a + a + √2*a
#   = 2a + √2a
#   = a(2 + √2)
# a = P / (2 + √2)
# Fourth, a 3,4,5 triangle is the smallest right triangle with integral sides.
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])
    solutions = []
    for perimeter in xrange(12, maximum+1, 2):
        solutions.append(triangles(perimeter))
    largest = max(solutions)
    # need to reverse calculate the indices, since we only create every other
    print sum(solutions)
    print solutions.index(largest)*2 + 12, largest


if __name__ == '__main__':
    main()
