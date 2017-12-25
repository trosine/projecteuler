#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0046

https://projecteuler.net/problem=46

Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1²
15 = 7 + 2×2²
21 = 3 + 2×3²
25 = 7 + 2×3²
27 = 19 + 2×2²
33 = 31 + 2×1²

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

import math

PROBLEM = 46
SOLVED = True
SPEED = 0.06
TAGS = ['prime_sieve', 'goldbach']


def sieve(maximum):
    """Generate a list of primes up to maximum."""
    primes = []
    possible = [True] * maximum
    limit = int(math.sqrt(maximum))
    for candidate in xrange(2, limit):
        if possible[candidate]:
            primes.append(candidate)
            for composite in xrange(candidate**2, maximum, candidate):
                possible[composite] = False
    # remaining True candidates are prime
    for candidate in xrange(limit, maximum):
        if possible[candidate]:
            primes.append(candidate)
    return primes


def twice_squares(maximum):
    """Generate a list of numbers that are two times a sqaure up to maximum."""
    squares = []
    limit = int(math.sqrt(maximum) / 2)
    for number in xrange(1, limit):
        squares.append(2 * number * number)
    return squares


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 100000
    primes = set(sieve(maximum))
    squares = twice_squares(maximum)
    for composite in xrange(9, maximum, 2):
        if composite in primes:
            continue  # not composite
        for square in squares:
            if composite - square in primes:
                break
        else:
            print composite
            break


if __name__ == '__main__':
    main()
