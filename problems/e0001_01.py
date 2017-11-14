#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0001

https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys

PROBLEM = 1
SOLVED = True
SPEED = float('0.02')
TAGS = ['partial_sum']


def partial_sum(multiple, maxvalue):
    """Calculates the n-th partial sum of simple arithmatic series where
    f(i) == ni
    """
    how_many = maxvalue / multiple
    return how_many * (multiple + multiple * how_many) / 2


def calculate(maxvalue):
    """Calculate the sum of all multiples of 3 and 5 below maxvalue quickly"""
    sum3 = partial_sum(3, maxvalue-1)
    sum5 = partial_sum(5, maxvalue-1)
    sum15 = partial_sum(15, maxvalue-1)
    return sum3 + sum5 - sum15


def calculate_brute(maxvalue):
    """Calculate the sum of all multiples of 3 and 5 below maxvalue via brute force"""
    total = 0
    for i in xrange(1, maxvalue):
        if not i % 3 or not i % 5:
            total += i
    return total


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maxvalue = 1000
    if len(sys.argv) > 1:
        maxvalue = int(sys.argv[1])
    print calculate(maxvalue)


if __name__ == '__main__':
    main()
