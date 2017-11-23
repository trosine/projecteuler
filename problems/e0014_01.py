#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0014

https://projecteuler.net/problem=14

Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 ( n is even)

n → 3n + 1 ( n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE:

Once the chain starts the terms are allowed to go above one million.
"""

import sys

PROBLEM = 14
SOLVED = True
SPEED = 1.92
TAGS = ['collatz', 'memoize']


def memoize(func):
    """Decorator that keeps track of previously known values"""
    memo = {}
    def helper(arg):
        # pylint: disable=locally-disabled, missing-docstring
        if arg not in memo:
            memo[arg] = func(arg)
        return memo[arg]
    return helper


@memoize
def collatz(number):
    """Returns the number of steps from the Collatz sequence needed
    to reach 1
    """
    if number == 1:
        return 1
    if number % 2:
        next_number = number * 3 + 1
    else:
        next_number = number / 2
    return collatz(next_number) + 1


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1000000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])

    max_steps = 0
    for number in xrange(1, maximum + 1):
        steps = collatz(number)
        if steps > max_steps:
            max_steps = steps
            longest_number = number

    print 'Number: %d, Steps: %d' % (longest_number, max_steps)


if __name__ == '__main__':
    main()
