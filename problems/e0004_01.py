#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0004

https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools

PROBLEM = 4
SOLVED = True
SPEED = 0.02
TAGS = ['palindrome']


def is_palindrome(number):
    """Returns if the number is a palindrome"""
    word = str(number)
    return word == word[::-1]

def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    print 'Unsolved'
    palindromes = []
    # combinations_with_replacement returns tuples where order does not matter
    # e.g. (1, 2) and (2, 1) are the same
    for ints in itertools.combinations_with_replacement(xrange(900, 1000), 2):
        multiple = ints[0] * ints[1]
        if is_palindrome(multiple):
            palindromes.append(multiple)
    print max(palindromes)


if __name__ == '__main__':
    main()
