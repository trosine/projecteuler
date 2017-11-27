#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0009

https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c , for which,

a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

import math
import sys

PROBLEM = 9
SOLVED = True
SPEED = 0.06
TAGS = ['pythagorean']


def main():
    """Solve problem."""
    # pylint: disable=locally-disabled, invalid-name
    print 'Project Euler: %04d' % PROBLEM
    target = 1000
    if len(sys.argv) > 1:
        target = int(sys.argv[1])
    result = 0
    for a in xrange(1, target-2):
        for b in xrange(a+1, target-1):
            c = math.sqrt(a*a + b*b)
            if a + b + c == target:
                print '%d**2 + %d**2 == %d == %d**2' % (a, b, c*c, c)
                result = a * b * c
                break
        if result:
            break
    print int(result)


if __name__ == '__main__':
    main()
