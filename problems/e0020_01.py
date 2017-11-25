#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0020

https://projecteuler.net/problem=20

Factorial digit sum

n! means

n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the
digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math
import sys

PROBLEM = 20
SOLVED = True
SPEED = 0.02
TAGS = ['factorial']


# a more hand-crafted implementation would be to factor each number to create
# the total prime factorization, then remove the factors that result in 10
# (since those don't add anything to the sum of digits)
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    number = 100
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    factorial = str(math.factorial(number))
    print sum(map(int, iter(factorial)))


if __name__ == '__main__':
    main()
