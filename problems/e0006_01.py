#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0006

https://projecteuler.net/problem=6

Sum square difference

The sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import sys

PROBLEM = 6
SOLVED = True
SPEED = 0.02
TAGS = ['partial_sum', 'partial_sum_squares']


def partial_sum(multiple, maxvalue):
    """Calculates the n-th partial sum of simple arithmatic series where
    f(i) == ni
    """
    how_many = maxvalue / multiple
    return how_many * (multiple + multiple * how_many) / 2


def partial_sum_squares(maxvalue):
    """Calculates the n-th partial sum of squares
    https://trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm
    SUM(k**2, k=0, n) = n/6 * (n+1) * (2*n+1)
    """
    # dividing by 6 as last operation to ensure proper result
    return maxvalue * (maxvalue+1) * (2*maxvalue+1) / 6

def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    terms = 100
    if len(sys.argv) > 1:
        terms = int(sys.argv[1])

    square_sum = partial_sum(1, terms) ** 2
    sum_squares = partial_sum_squares(terms)
    print square_sum - sum_squares


if __name__ == '__main__':
    main()
