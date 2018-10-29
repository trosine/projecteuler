#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0053

https://projecteuler.net/problem=53

Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ⁵C₃ = 10.

In general,

ⁿCᵣ = n! / r!(n−r)!

, where r ≤ n, n! = n × (n−1) × ...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million:

²³C₁₀ = 1144066.

How many, not necessarily distinct, values of

ⁿCᵣ, for 1 ≤ n ≤ 100, are greater than one-million?
"""

import math

PROBLEM = 53
SOLVED = True
SPEED = float('0.077')
TAGS = ['combinations']


def choose(objects, picks):
    """Return the number of combinations (nCr)"""
    fact = math.factorial
    return fact(objects) / (fact(picks) * fact(objects-picks))


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    greater = 0
    for objects in xrange(23, 101):
        for picks in xrange(1, objects):
            if choose(objects, picks) > 1000000:
                # print objects, 'C', picks
                greater += 1
    print greater


if __name__ == '__main__':
    main()
