#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0021

https://projecteuler.net/problem=21

Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math
import sys

PROBLEM = 21
SOLVED = True
SPEED = 0.11
TAGS = ['memoize', 'amicable_numbers']


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
def sum_of_divisors(number):
    """Calculate the sum of the proper divisors of number."""
    total = 0
    limit = int(math.sqrt(number))
    candidate = 1
    while candidate <= limit:
        if number % candidate == 0:
            # print '%d is divisible by %d' % (number, candidate)
            total += candidate + number/candidate
        candidate += 1
    return total - number


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 10000
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])

    total = 0
    for number in xrange(1, maximum):
        sum1 = sum_of_divisors(number)
        if sum1 > number:
            if number == sum_of_divisors(sum1):
                print 'Amicable numbers: %d, %d' % (number, sum1)
                total += number + sum1

    print total


if __name__ == '__main__':
    main()
