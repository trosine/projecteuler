#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0056

https://projecteuler.net/problem=56

Powerful digit sum

A googol (10¹⁰⁰) is a massive number: one followed by one-hundred zeros; 100¹⁰⁰
is almost unimaginably large: one followed by two-hundred zeros. Despite their
size, the sum of the digits in each number is only 1.

Considering natural numbers of the form,

aᵇ, where a, b < 100, what is the maximum digital sum?
"""

PROBLEM = 56
SOLVED = True
SPEED = float('0.042')
TAGS = ['digit_sum']


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    sums = []
    # the end result must have a large number of digits, which can only happen
    # with large bases and exponents
    # even with starting both base and exponent at 2, it runs in 0.448 secs
    for base in xrange(90, 100):
        for exponent in xrange(90, 100):
            value = base**exponent
            sums.append(sum([int(digit) for digit in str(value)]))
            # print base, exponent, sums[-1]
    print max(sums)


if __name__ == '__main__':
    main()
