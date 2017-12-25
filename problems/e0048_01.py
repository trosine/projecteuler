#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0048

https://projecteuler.net/problem=48

Self powers

The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.

Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
"""

import sys

PROBLEM = 48
SOLVED = False
SPEED = float('inf')
TAGS = ['large_integers']


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])
    total = 0
    for number in xrange(1, maximum+1):
        total += number ** number
    print str(total)[-10:]


if __name__ == '__main__':
    main()
