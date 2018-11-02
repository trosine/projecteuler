#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0057

https://projecteuler.net/problem=57

Square root convergents

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""

import math

PROBLEM = 57
SOLVED = True
SPEED = float('0.35')
TAGS = ['continued_fractions']


def digits(number):
    """Counts the number of digits in a number"""
    return int(math.log10(number))


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    # this continued fraction can be described as:
    # F(n) = 1 + 1 / (1 + F(n-1))
    # 1/(a/b) == b/a, so this is mostly swapping numerators and denominators
    numerator = 3
    denominator = 2
    result = 0
    for _ in xrange(2, 1000):
        # add 1 (to make the new denominator 1 + F(n-1))
        numerator = denominator + numerator
        # flip and add 1
        numerator, denominator = denominator + numerator, numerator
        if digits(numerator) > digits(denominator):
            # print _, ':', numerator, '/', denominator
            result += 1
    print result


if __name__ == '__main__':
    main()
