#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0012

https://projecteuler.net/problem=12

Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms
would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

import itertools
import math
import sys

PROBLEM = 12
SOLVED = True
SPEED = 0.76
TAGS = ['prime', 'prime_sieve', 'partial_sum', 'triangular']


class Primes(object):
    """Iteratable class that handles prime number generation and testing"""

    # cache of currently known primes
    known_primes = [2, 3]

    def __init__(self, maximum=None, count=None, sieve=None):
        self.maximum = float('inf')
        self.count = float('inf')
        self.__iter = 0
        if maximum:
            self.maximum = maximum
            sieve = maximum
        if count:
            self.count = count
        if sieve:
            sieve = int(sieve)
            if sieve > self.known_primes[-1]:
                # only re-initialize if we need more
                self.sieve(sieve)

    def __iter__(self):
        return self

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Cannot use "%s" as a list index' % type(key))
        while len(self.known_primes) <= key:
            self.next()
        return self.known_primes[key]

    @classmethod
    def sieve(cls, maximum):
        """Initialize the known list of primes using Eratosthene sieve
        methodology
        """
        cls.known_primes = []
        possible = [True] * maximum
        limit = int(math.sqrt(maximum))
        for candidate in xrange(2, limit):
            if possible[candidate]:
                cls.known_primes.append(candidate)
                # using candidate**2 as start, because all prior have already
                # been marked as False
                # for example, when marking composites of 3, 6 is already marked
                # composites of 5: 10(2), 15(3), 20(2) are already marked
                for composite in xrange(candidate**2, maximum, candidate):
                    possible[composite] = False
        # every candidate >= sqrt(maximum) is prime
        for candidate in xrange(limit, maximum):
            if possible[candidate]:
                cls.known_primes.append(candidate)

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
            if candidate > self.maximum:
                raise StopIteration()
            # print 'Checking to see if candidate %d is prime' % candidate
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
            if prime > number:
                break
            # print 'Checking to see if %d is a factor of %d' % (prime, number)
            # reduce the total iterations
            if prime > math.sqrt(number):
                factors.append(number)
                break
            while not number % prime:
                number /= prime
                factors.append(prime)
        return factors


def partial_sum(maxvalue, multiple=1):
    """Calculates the n-th partial sum of simple arithmatic series where
    f(i) == ni
    """
    how_many = maxvalue / multiple
    return how_many * (multiple + multiple * how_many) / 2


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    target = 500
    if len(sys.argv) > 1:
        target = int(sys.argv[1])
    Primes.sieve(100000)

    max_divisors = 0
    num_with_max = 0
    for number in itertools.imap(partial_sum, itertools.count(2)):
        divisors = 1
        for dummy, group in itertools.groupby(Primes.factor(number)):
            # number of divisors is the product of each (exponent+1)
            # http://primes.utm.edu/glossary/xpage/tau.html
            divisors *= len(list(group)) + 1
        if divisors > max_divisors:
            # print 'Number=%d, Divisors=%d' % (number, divisors)
            max_divisors = divisors
            num_with_max = number
            if max_divisors > target:
                break

    print num_with_max


if __name__ == '__main__':
    main()
