#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0036

https://projecteuler.net/problem=36

Double-base palindromes

The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

import sys

PROBLEM = 36
SOLVED = True
SPEED = 0.25
TAGS = ['palindrome', 'conversion']


def palindrome(number):
    """Returns if the number is a palindrome"""
    word = str(number)
    return word == word[::-1]

# Given the restriction that there may not be leading zeros, binary palindromes must be odd.
# Limiting to odds prevents this issue in both bases.
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1000000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])

    total = 0
    for number in xrange(1, maximum, 2):
        if palindrome(number) and palindrome(bin(number)[2:]):
            # print '{0} => {0:b}'.format(number,)
            total += number
    print 'Sum:', total


if __name__ == '__main__':
    main()
