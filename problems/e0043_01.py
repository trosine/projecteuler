#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0043

https://projecteuler.net/problem=43

Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d₁ be the 1-st digit, d₂ be the 2-nd digit, and so on. In this way, we note
the following:

d₂d₃d₄=406 is divisible by 2
d₃d₄d₅=063 is divisible by 3
d₄d₅d₆=635 is divisible by 5
d₅d₆d₇=357 is divisible by 7
d₆d₇d₈=572 is divisible by 11
d₇d₈d₉=728 is divisible by 13
d₈d₉d₁₀=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

PROBLEM = 43
SOLVED = True
SPEED = 7.09
TAGS = ['pandigital', 'substring_divisibility']
PRIMES = [2, 3, 5, 7, 11, 13, 17]


def substring_divisible(number):
    """Check to see if the number is divisible by all possible 3 digit substrings."""
    string = str(number)
    for offset in xrange(1, len(string)-2):
        substring = string[offset:offset+3]
        # print '%s / %d' % (substring, PRIMES[offset-1])
        if int(substring) % PRIMES[offset-1]:
            return False
    return True


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    total = 0
    # print substring_divisible(1406357289)
    for permutation in itertools.permutations('0123456789', 10):
        if permutation[0] == '0':
            continue
        string = ''.join(permutation)
        if substring_divisible(string):
            print string
            total += int(string)
    print total


if __name__ == '__main__':
    main()
