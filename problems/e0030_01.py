#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0030

https://projecteuler.net/problem=30

Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

As 1 = 1⁴ is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

PROBLEM = 30
SOLVED = True
SPEED = 4.09
TAGS = ['powers']


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    total = 0
    # maximum number of digits will be 6 (n*9^5)
    for number in xrange(2, 1000000):
        powers = sum(int(digit)**5 for digit in str(number))
        if powers == number:
            total += number
            print '%6d is valid, sum=%d' % (number, total)


if __name__ == '__main__':
    main()
