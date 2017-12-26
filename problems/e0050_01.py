#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0050

https://projecteuler.net/problem=50

Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-
hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

import math
import sys

PROBLEM = 50
SOLVED = True
SPEED = 1.12
TAGS = ['prime_sieve', 'prime_sum']


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


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1000000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])
    primes = sieve(maximum)
    prime_set = set(primes)
    candidates = []
    for base in xrange(0, min(100, len(primes))):
        total = primes[base]
        for term in xrange(base+1, len(primes)):
            total += primes[term]
            if total in prime_set:
                candidates.append((term - base + 1, total, base, term))
    print max(candidates)


if __name__ == '__main__':
    main()
