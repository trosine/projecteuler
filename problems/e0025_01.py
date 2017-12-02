#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0025

https://projecteuler.net/problem=25

1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n−1) + F(n−2) , where F(1) = 1 and F(2) = 1.

Hence the first 12 terms will be:

F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144

The 12th term, F(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""

import sys

PROBLEM = 25
SOLVED = True
SPEED = 0.04
TAGS = ['Fibonacci']


def fib(digits):
    """Returns the index of the first Fibonacci number to contain digits."""
    # pylint: disable=locally-disabled, invalid-name
    index = 1
    a, b = 1, 1
    while len(str(a)) < digits:
        a, b = b, a+b
        index += 1
    return index


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    digits = 1000
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])
    print fib(digits)


if __name__ == '__main__':
    main()
