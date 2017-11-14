#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0002

https://projecteuler.net/problem=2

Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

import sys

PROBLEM = 2
SOLVED = True
SPEED = float('0.02')
TAGS = ['fibonacci']

def fib(maxvalue):
    """Calculates the sum of all Fibonacci values that are divisible by 2."""
    # pylint: disable=locally-disabled, invalid-name
    total = 0
    a, b = 1, 1
    while b <= maxvalue:
        if not b % 2:
            total += b
        a, b = b, a+b
    return total


def main():
    """Solve problem."""
    maxvalue = 4000000
    if len(sys.argv) > 1:
        maxvalue = int(sys.argv[1])
    print 'Project Euler: %04d' % PROBLEM
    print fib(maxvalue)


if __name__ == '__main__':
    main()
