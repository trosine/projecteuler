#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0016

https://projecteuler.net/problem=16

Power digit sum

2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000 ?
"""

PROBLEM = 16
SOLVED = False
SPEED = float('inf')
TAGS = []


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    print sum(map(int, str(pow(2, 1000))))


if __name__ == '__main__':
    main()
