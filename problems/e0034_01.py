#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0034

https://projecteuler.net/problem=34

Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

PROBLEM = 34
SOLVED = True
SPEED = 2.88
TAGS = ['factorial', 'digits', 'factorion']
FACTORIALS = [math.factorial(n) for n in range(10)]


# The largest sum would be 7 * 9! = 2540160 (7 digits).
# I don't actually test 7 * 9! since it is clearly not valid.
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    total = 0
    for number in xrange(3, 7*FACTORIALS[9]):
        # This is slower (10.7s) because of all the conversion between str/int.
        # result = sum([FACTORIALS[int(d)] for d in str(number)])
        temporary = number
        result = 0
        # Grab the last digit and add its factorial to result.
        while temporary:
            result += FACTORIALS[temporary % 10]
            temporary /= 10
        if result == number:
            print 'Special:', number
            total += number
    print 'Sum:', total



if __name__ == '__main__':
    main()
