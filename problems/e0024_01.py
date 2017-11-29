#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0024

https://projecteuler.net/problem=24

Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

import math

PROBLEM = 24
SOLVED = True
SPEED = 0.02
TAGS = ['permutation']


# This algorithm makes a few steps to get directly to the answer.
# Since the permutations are ordered, we can start by determining each digit in sequence.
# Each digit is selected to reduce the remaining permutations to the least possible.
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    requested = 1000000 - 1
    available = range(10)
    result = ''
    while available:
        permutations = math.factorial(len(available)-1)
        # determine which remaining digit reduces the permutations the most
        index = requested / permutations
        result += str(available.pop(index))
        requested -= permutations * index
    print result


if __name__ == '__main__':
    main()
