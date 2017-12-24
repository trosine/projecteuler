#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0041

https://projecteuler.net/problem=41

Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import math

PROBLEM = 41
SOLVED = True
# SPEED = 352.13  # when testing 1e9 (not realizing they're divisible by 3)
SPEED = 3.33
TAGS = ['pandigital', 'primes', 'prime_sieve']
PANDIGITAL = list('123456789')


def pandigital(number, digits=None):
    """Returns wether number is n-digit pandigital."""
    string = str(number)
    if not digits:
        digits = len(string)
    digits = min(digits, 9)
    return sorted(string) == PANDIGITAL[:digits]


def pandigital_sieve(maximum):
    """Returns the largest pandigital primes using sieve of Eratosthenes."""
    largest = 0
    maximum = int(maximum)
    limit = int(math.sqrt(maximum))
    print 'Finding primes < %d (limit=%d)' % (maximum, limit)
    possible = [True] * maximum
    print 'Possible list initialized'
    for candidate in xrange(2, limit):
        if possible[candidate]:
            # if pandigital(candidate):
            #     largest = candidate
            for composite in xrange(candidate**2, maximum, candidate):
                possible[composite] = False
    print 'Checking remaining candidates'
    # All candidates >= sqrt(maximum) is prime
    for candidate in xrange(int(limit / 2  * 2 + 1), maximum, 2):
        if possible[candidate] and pandigital(candidate):
            largest = candidate
    return largest


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    # pandigital numbers consisting of 8 or 9 digits are all divisible by 3
    print pandigital_sieve(1e7)


if __name__ == '__main__':
    main()
