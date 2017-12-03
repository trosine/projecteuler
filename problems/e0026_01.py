#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0026

https://projecteuler.net/problem=26

Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1 / 2 = 0.5
1 / 3 = 0.(3)
1 / 4 = 0.25
1 / 5 = 0.2
1 / 6 = 0.1(6)
1 / 7 = 0.(142857)
1 / 8 = 0.125
1 / 9 = 0.(1)
1 / 10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1 / 7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1 / d contains the longest recurring cycle
in its decimal fraction part.
"""

PROBLEM = 26
SOLVED = True
SPEED = 0.05
TAGS = ['long_division']


# By appending to a string, this could return the quotient
# Effectively performs long-division to detect the cycle easier
# Float also only has a 17 digit precision
def cycle_length(divisor):
    """Determines the number of digits that are repeated in 1/divisor"""
    moduli = {}
    modulus = 1
    index = 1
    while modulus:
        if modulus in moduli:
            return index - moduli[modulus]
        moduli[modulus] = index
        while modulus <= divisor:
            modulus *= 10
        modulus %= divisor
        index += 1
    return 0  # evenly divisible - no cycle


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = (0, 1)
    for number in xrange(2, 1000):
        length = cycle_length(number)
        if length > maximum[0]:
            maximum = (length, number)
    print maximum


if __name__ == '__main__':
    main()
