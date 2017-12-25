#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0044

https://projecteuler.net/problem=44

Pentagon numbers

Pentagonal numbers are generated by the formula, P(n) = n(3n−1)/2. The first
ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P(4) + P(7) = 22 + 70 = 92 = P(8). However, their
difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P(j) and P(k), for which their sum and
difference are pentagonal and D = |P(k) − P(j)| is minimised; what is the value
of D?
"""

import itertools

PROBLEM = 44
SOLVED = True
SPEED = 8.35  # 0.77 if using 3000 as the max
TAGS = ['pentagonal']


def pentagonal_value(number):
    """Returns the pentagonal of number."""
    return number * (3*number-1) / 2


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 10000
    forward = []
    # build up a cache of pentagonal numbers
    for number in xrange(maximum):
        pentagonal = pentagonal_value(number)
        forward.append(pentagonal)
    reverse = set(forward)  # sets are faster for `in` tests

    differences = []
    for one, two in itertools.combinations(xrange(1, maximum), 2):
        diff = forward[two] - forward[one]
        total = forward[two] + forward[one]
        if total in reverse and diff in reverse:
            print '%d, %d => %d' % (two, one, diff)
            differences.append(diff)
    print min(differences)


if __name__ == '__main__':
    main()
