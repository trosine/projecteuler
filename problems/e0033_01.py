#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0033

https://projecteuler.net/problem=33

Digit cancelling fractions

The fraction 49 / 98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49 / 98 = 4 / 8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30 / 50 = 3 / 5 , to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

import itertools
from fractions import gcd

PROBLEM = 33
SOLVED = True
SPEED = 0.03
TAGS = ['gcd', 'cancelling', 'digits']


# The two digits not being cancelled cannot be the same because the result <1.
# The digit to cancel cannot be the same as the numerator because 11/x > 1.
# The digit to cancel cannot be the same as the denominator because nothing should simplify to x/11.
# The cancelling digit must be in a different position in the numerator an denominator
# because ex 62/92 != 6/9.
# It is for these reasons that I am using permutations instead of product.
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    fractions = []
    for num, denom, cancel in itertools.permutations(range(1, 10), 3):
        if num >= denom:
            # print '%d / %d >= 1' % (num, denom)
            continue
        cancelled_fraction = float(num) / denom
        # test nc/cd
        real_num = num * 10 + cancel
        real_denom = cancel * 10 + denom
        if float(real_num) / real_denom == cancelled_fraction:
            print '%d/%d = %f' % (real_num, real_denom, float(real_num)/real_denom)
            fractions.append((num, denom))
        # This doesn't seem to be necessary, but I don't know why.
        # test cn/dc
        real_num = cancel * 10 + num
        real_denom = denom * 10 + cancel
        if float(real_num) / real_denom == cancelled_fraction:
            print '%d/%d = %f' % (real_num, real_denom, float(real_num)/real_denom)
            fractions.append((num, denom))

    numerator = 1
    denominator = 1
    for num, denom in fractions:
        numerator *= num
        denominator *= denom

    print '%d/%d' % (numerator, denominator)
    print denominator / gcd(denominator, numerator)


if __name__ == '__main__':
    main()
