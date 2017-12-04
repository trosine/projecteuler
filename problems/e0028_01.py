#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0028

https://projecteuler.net/problem=28

Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.  What
is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in
the same way?
"""

import sys

PROBLEM = 28
SOLVED = True
SPEED = 0.02
TAGS = ['spiral']


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    size = 1001
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
        if not size % 2:
            size += 1
    tiers = size / 2
    total = 1
    diagonal = 1
    # index the tiers with the central `1` being t0
    for tier in xrange(1, tiers+1):
        offset = diagonal + tier*2  # the bottom corner
        # all 4 corners
        diagonals = range(offset, offset + tier*8, tier*2)
        diagonal = diagonals[-1]
        total += sum(diagonals)
        # print 'Tier=%d, sum=%d, diagonals=%s' % (tier, total, diagonals)
    print 'Sum=%d' % total


if __name__ == '__main__':
    main()
