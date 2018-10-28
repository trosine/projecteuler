#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0052

https://projecteuler.net/problem=52

Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

PROBLEM = 52
SOLVED = True
SPEED = float('0.155')
TAGS = ['permutations']


def permutation(integer):
    """Get ordered list of digits in integer"""
    return sorted(str(integer))


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    for digits in xrange(3, 9):
        # we have to make sure n*6 will contain the same number of digits
        maximum = 10 ** digits / 6
        minimum = 10 ** (digits-1)
        print 'Trying numbers between', minimum, 'and', maximum
        for base in xrange(minimum, maximum + 1):
            base_perm = permutation(base)
            for multiple in xrange(2, 7):
                valid = permutation(base*multiple) == base_perm
                # the first invalid multiple breaks this loop
                # causing the next base to be checked
                if not valid:
                    break
            if valid:
                print base, 'and its first 6 multiples contain the same digits'
                return


if __name__ == '__main__':
    main()
