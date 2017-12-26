#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0049

https://projecteuler.net/problem=49

Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import itertools
import math

PROBLEM = 49
SOLVED = True
SPEED = 0.11
TAGS = ['prime_sieve', 'permutations']

def sieve(maximum):
    """Produce a list of primes less than maximum."""
    primes = []
    possible = [True] * maximum
    limit = int(math.sqrt(maximum))
    for candidate in xrange(2, limit):
        if possible[candidate]:
            primes.append(candidate)
            for composite in xrange(candidate**2, maximum, candidate):
                possible[composite] = False
    # every candidate >= sqrt(maximum) is prime
    for candidate in xrange(limit, maximum):
        if possible[candidate]:
            primes.append(candidate)
    return primes


def permuted(base, candidate):
    """Determine if base and candidate are string permutations of each other."""
    base = sorted(list(str(base)))
    candidate = sorted(list(str(candidate)))
    return base == candidate


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    # only interested in 4 digit primes
    primes = [x for x in sieve(10000) if x > 1000]
    for base in primes:
        for permutation in set(itertools.permutations(str(base))):
            permutation = int(''.join(permutation))
            if base < permutation < 6667:
                if permutation not in primes:
                    continue
                diff = permutation - base
                if permutation + diff in primes and permuted(base, permutation+diff):
                    print base, permutation, permutation+diff


if __name__ == '__main__':
    main()
