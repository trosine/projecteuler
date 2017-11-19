#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0005

https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is *evenly divisible* by all of the
numbers from 1 to 20?
"""

import itertools
import math
import sys

PROBLEM = 5
SOLVED = True
SPEED = 0.02
TAGS = ['primes', 'factors', 'lowest_common_multiple']


class Primes(object):
    """Iteratable class that handles prime number generation and testing"""

    # cache of currently known primes
    known_primes = [2, 3]

    def __init__(self, maximum=float('inf'), count=float('inf')):
        self.maximum = maximum
        self.count = count
        self.__iter = 0

    def __iter__(self):
        return self

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Cannot use "%s" as a list index' % type(key))
        while len(self.known_primes) <= key:
            self.next()
        return self.known_primes[key]

    def next(self):
        """Fetch the next prime number"""
        if self.__iter >= self.count:
            # print 'Reached maximum count %d (%d)' % (self.count, self.__iter)
            raise StopIteration()
        if self.__iter < len(self.known_primes):
            if self.known_primes[self.__iter] > self.maximum:
                raise StopIteration()
            key = self.__iter
            self.__iter += 1
            return self.known_primes[key]
        candidate = self.known_primes[-1] + 2
        while True:
            # print 'Checking to see if candidate %d is prime' % candidate
            if candidate > self.maximum:
                raise StopIteration()
            if not self.first_factor(candidate):
                self.known_primes.append(candidate)
                self.__iter += 1
                return candidate
            candidate += 2

    @classmethod
    def first_factor(cls, number):
        """Returns the lowest factor of the number.
        If the number is prime, None is returned instead.
        """
        for prime in cls(maximum=math.sqrt(number)):
            if not number % prime:
                return prime
        return None

    @classmethod
    def factor(cls, number):
        """Returns a list of prime factors that this number is composed of"""
        factors = []
        for prime in cls():
            # print 'Checking to see if %d is a factor of %d' % (prime, number)
            if prime == number:
                factors.append(prime)
                break
            # reduce the total iterations
            if prime > math.sqrt(number):
                factors.append(number)
                break
            while not number % prime:
                number /= prime
                factors.append(prime)
                # case for squares (which are divisible)
                if prime == number:
                    factors.append(prime)
                    break
        return factors


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maxvalue = 20
    if len(sys.argv) > 1:
        maxvalue = int(sys.argv[1])

    primes = set(Primes(maximum=maxvalue))
    non_primes = set(xrange(2, maxvalue+1)) - primes
    non_primes = sorted(non_primes, reverse=True)

    # The lowest common multiple must be a multiple of the product of all of
    # the prime factors
    start = 1
    for prime in primes:
        start *= prime

    # 20 is the maximum that xrange would work before raising
    # OverflowError: Python int too large to convert to C long
    numbers_attempted = itertools.count()
    factors_tested = itertools.count()
    number = start
    while True:
        numbers_attempted.next()
        for factor in non_primes:
            factors_tested.next()
            if number % factor:
                break
        else:
            # result found, break out of while
            break
        number += start
    print 'Numbers Attempted:', numbers_attempted
    print 'Factors Tested:', factors_tested
    print 'Result:', number


if __name__ == '__main__':
    main()
